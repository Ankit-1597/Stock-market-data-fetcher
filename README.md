# Stock Market Data Fetcher

This project fetches historical and daily stock market data for the top 10 companies in India (by market cap) using the Alpha Vantage API and stores it in a SQL database using PySpark.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- Java 8 or later
- Apache Spark (PySpark)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ankit-1597/Stock-market-data-fetcher.git
    cd Stock-market-data-fetcher
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Table Creation

Before running the data ingestion scripts, you need to create the necessary tables in your SQL database.

 **Query to create table and indexes**:
    
    ```sql
    -- SQL script to create daily_data table and also indexes
    CREATE TABLE StockTable (
        Date DATE ,
        Company VARCHAR(50) ,
        Open FLOAT,
        Close FLOAT,
        High FLOAT,
        Low FLOAT,
        Volume INTEGER,
        PRIMARY KEY (Date, Company),
        INDEX idx_date (Date),
        INDEX idx_company (Company)
    );
    ```

## SQL Queries

To analyze the data in your SQL database, you can use the following queries:

1. **Company Wise Daily Variation of Prices**:
    ```sql
    -- SQL query to fetch Company Wise Daily Variation of Prices
    SELECT Company, Date, (High - Low) AS Daily_Variation
    FROM historical_data
    ORDER BY Company, Date;
    ```

2. **Company Wise Daily Volume Change**:
    ```sql
    -- SQL query to fetch Company Wise Daily Volume Change
    SELECT 
        Company, 
        Date, 
        Volume,
        (Volume - LAG(Volume) OVER (PARTITION BY Company ORDER BY Date)) AS Daily_Volume_Change
    FROM 
        daily_data
    ORDER BY 
        Company, Date;
    ```

## Fetch Historical Data

To fetch and ingest historical stock market data from January 1, 2020, to May 31, 2024, run the following script:

```sh
spark-submit historical_dump.py
```
## Fetch Historical Data

To fetch and ingest daily stock market data for the previous day, run the following script:

```sh
spark-submit daily_dump.py
```
