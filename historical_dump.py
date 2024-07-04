"""
Author : Ankit Thakur
Version : 1.0
Description : This Python file provides the script for historical data dump.
File Name : historical_dump.py
"""

# Third party imports
from pyspark.sql.functions import col, explode, udf

# Local application imports
import config
from utils import (
    create_spark_session,
    fetch_and_filter_data,
    get_historical_schema,
    write_to_db,
)


def run_historical_dump():
    """
    Runs the historical data dump process, fetching and processing historical stock data.

    """
    spark = create_spark_session("HistoricalDump")
    fetch_historical_udf = udf(lambda symbol: fetch_and_filter_data(symbol, config.HISTORICAL_DATE_RANGE, config.API_KEY), get_historical_schema())

    data = config.COMPANIES
    df = spark.createDataFrame(data)
    df = df.withColumn("parsed_response", explode(fetch_historical_udf(col("Company"))))

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
    write_to_db(df,"StockTable","overwrite")

if __name__ == "__main__":
    run_historical_dump()
