"""
Author : Ankit Thakur
Version : 1.0
Description : This Python file provides all the configuration settings used throughout the code.
File Name : config.py
"""

# Standard library imports
from datetime import datetime, timedelta

API_KEY = '59054V0OI6W98R9W'                                        # Alpha Vantage API Key

HISTORICAL_DATE_RANGE = ["2020-01-01", "2024-05-31"]                # Date Filters for Historical Data

DAILY_DATE = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')   # Date Filter for Daily Data    

# Stock API url
BASE_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'

# List of companies to fetch data for
COMPANIES = [
    {"company": "RELIANCE.BSE"},
    {"company": "TCS.BSE"},
    {"company": "HDFCBANK.BSE"},
    {"company": "ICICIBANK.BSE"},
    {"company": "INFY.BSE"},
    {"company": "HINDUNILVR.BSE"},
    {"company": "SBIN.BSE"},
    {"company": "HDFCBANK.BSE"},
    {"company": "BHARTIARTL.BSE"},
    {"company": "BAJFINANCE.BSE"}
]         

                                                       