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
    git clone https://github.com/your-username/stock-market-data-fetcher.git
    cd stock-market-data-fetcher
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

1. Run the SQL script for table creation script in database.Use the appropriate command or database client to run the `create_tables.sql` script.

## Fetch Historical Data

To fetch historical stock market data from January 1, 2020, to May 31, 2024, run the following script:

```sh
spark-submit fetch_historical_data.py
