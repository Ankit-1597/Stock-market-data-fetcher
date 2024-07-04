"""
Author : Ankit Thakur
Version : 1.0
Description : This Python file provides utility functions used throughout the code.
File Name : utils.py
"""

# Standard library imports

# Third party imports
import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    ArrayType,
    FloatType,
    LongType,
    StringType,
    StructField,
    StructType,
)

import config
from constants import DBCONSTANTS


def fetch_and_filter_data(symbol, date_filter, api_key):
    """
    Fetches and filters historical stock data for a given symbol within a specified date range.

    Args:
        symbol (str): The stock symbol to fetch data for.
        date_filter (list): A list containing the start and end dates for filtering data.
        api_key (str): The API key for accessing Alpha Vantage.

    Returns:
        list: A list of dictionaries containing the filtered stock data.
    """

    url = config.BASE_URL.format(symbol=symbol, api_key=api_key)
    response = requests.get(url)
    data = response.json()
    time_series = data.get("Time Series (Daily)", {})
    records = []
    start_date, end_date = date_filter

    for date, values in time_series.items():
        if start_date <= date <= end_date:
            record = {
                "Date": date,
                "Open": float(values.get("1. open", 0)),
                "Close": float(values.get("4. close", 0)),
                "High": float(values.get("2. high", 0)),
                "Low": float(values.get("3. low", 0)),
                "Volume": int(values.get("5. volume", 0))
            }
            records.append(record)
    return records

def fetch_daily_data(symbol, date_filter, api_key):
    """
    Fetches the daily stock data for a given symbol for a specified date.

    Args:
        symbol (str): The stock symbol to fetch data for.
        date_filter (str): The specific date to fetch data for.
        api_key (str): The API key for accessing Alpha Vantage.

    Returns:
        dict: A dictionary containing the stock data for the specified date.
    """

    url = config.BASE_URL.format(symbol=symbol, api_key=api_key)
    response = requests.get(url)
    data = response.json()
    time_series = data.get("Time Series (Daily)", {})
    values = time_series[date_filter]
    record = {
        'Date': date_filter,
        'Company': symbol,
        'Open': float(values['1. open']),
        'Close': float(values['4. close']),
        'High': float(values['2. high']),
        'Low': float(values['3. low']),
        'Volume': int(values['5. volume'])
    }
    return record

def get_historical_schema():
    """
    Returns the schema for the historical stock data.

    Returns:
        pyspark.sql.types.ArrayType: The schema for the historical stock data.
    """

    return ArrayType(StructType([
        StructField("Date", StringType(), True),
        StructField("Open", FloatType(), True),
        StructField("Close", FloatType(), True),
        StructField("High", FloatType(), True),
        StructField("Low", FloatType(), True),
        StructField("Volume", LongType(), True)
    ]))

def get_daily_schema():
    """
    Returns the schema for the daily stock data.

    Returns:
        pyspark.sql.types.StructType: The schema for the daily stock data.
    """

    return StructType([
        StructField("Date", StringType(), True),
        StructField("Open", FloatType(), True),
        StructField("Close", FloatType(), True),
        StructField("High", FloatType(), True),
        StructField("Low", FloatType(), True),
        StructField("Volume", LongType(), True)
    ])


def write_to_db(df,tablename,mode):
    """
    Writes Dataframe in database

    Args:
        df (dataframe): Spark dataframe to be ingested
        tablename (str): name of target table
        mode (str): mode of writing
    """    
    df.write.format('jdbc').options(
                url=DBCONSTANTS.JDBCURL,
                driver=DBCONSTANTS.DRIVER,
                dbtable=tablename,
                user=DBCONSTANTS.USERNAME,
                password=DBCONSTANTS.PASSWORD).mode(mode).save()

def create_spark_session(name):
    """
    Creates and returns the Spark session

    Args:
        name (str): name of spark application

    Returns:
        pyspark.sql.SparkSession: Spark session
    """
   
    spark = SparkSession \
        .builder \
        .appName(name) \
        .enableHiveSupport().getOrCreate()
    return spark