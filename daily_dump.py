"""
Author : Ankit Thakur
Version : 1.0
Description : This Python file provides the script for daily data dump.
File Name : daily_dump.py
"""

# Third party imports
from pyspark.sql.functions import col, udf

#Local application imports
import config
from utils import create_spark_session, fetch_daily_data, get_daily_schema,write_to_db


def run_daily_dump():
    """
    Runs the daily data dump process, fetching and processing daily stock data.

    """
    spark = create_spark_session("DailyDump")
    fetch_daily_udf = udf(lambda symbol: fetch_daily_data(symbol, config.DAILY_DATE, config.API_KEY), get_daily_schema())
    

    data = config.COMPANIES
    df = spark.createDataFrame(data)
    df = df.withColumn("parsed_response", fetch_daily_udf(col("Company")))

    df = df.select(
        col("Company"),
        col("parsed_response.Date").alias("Date"),
        col("parsed_response.Open").alias("Open"),
        col("parsed_response.Close").alias("Close"),
        col("parsed_response.High").alias("High"),
        col("parsed_response.Low").alias("Low"),
        col("parsed_response.Volume").alias("Volume")
    )
    
    df.show(truncate=False)
    write_to_db(df,"StockTable","append")
    

if __name__ == "__main__":
    run_daily_dump()
