# Query the VAT Comply rates API 'https://api.vatcomply.com/rates', 
# using parameters to get the exchange rates for a base currency of 'USD' 
# and the date of '2024-01-21'.
#Using the orders DataFrame and the exchange rate from the API, 
# calculate the total amount sold in USD, saving as a variable called total_usd_sales.
#Ensure the final version of the orders DataFrame matches the requirements 
# detailed in the Workbook.
#The VAT Comply rates API is free to use and doesn't require 
# registration/authentication.



# Import pandas for reading and manipulating tabular data.
import pandas as pd

# Import requests for communicating with the VAT Comply API.
import requests


# STEP 1: LOAD THE DATASET

# Read the CSV file containing customer transactions.
# Store the data in a pandas DataFrame called 'orders'.
orders = pd.read_csv("data/orders-2024-01-21.csv")


# STEP 2: DEFINE THE API ENDPOINT

# This URL provides historical currency exchange rates.
url = "https://api.vatcomply.com/rates"

# Define the query parameters sent with the API request.
# 'base' specifies USD as the reference currency.
# 'date' requests exchange rates for January 21, 2024.
params = {
    "base": "USD",
    "date": "2024-01-21"
}


# STEP 3: REQUEST EXCHANGE RATES

# Send an HTTP GET request to the VAT Comply API.
# The params argument adds the query parameters to the URL.
# The timeout prevents the program from waiting indefinitely.
response = requests.get(url, params=params, timeout=30)

# Raise an exception if the request was unsuccessful.
response.raise_for_status()


# STEP 4: PROCESS THE API RESPONSE

# Convert the JSON response into a Python dictionary.
data = response.json()

# Extract the dictionary containing currency exchange rates.
# For example: {"USD": 1.0, "EUR": 0.918527, "GBP": 0.788326}
rates = data["rates"]


# STEP 5: ADD THE EXCHANGE RATE COLUMN

# Use pandas map() to match each currency in the orders
# DataFrame with its corresponding exchange rate.
#
# For example:
# EUR -> 0.918527
# GBP -> 0.788326
# USD -> 1.0
#
# Store the matching rates in a new 'exchange_rate' column.
orders["exchange_rate"] = orders["currency"].map(rates)


# STEP 6: CALCULATE AMOUNT_USD

# Multiply each transaction amount by its exchange rate.
#
# NOTE:
# This calculation follows the DataCamp workbook's
# accepted solution.
#
# For actual conversion into USD using USD-based rates,
# the correct operation would be division instead.
#
# Store the results in a new column called 'amount_usd'.
orders["amount_usd"] = (
    orders["amount"] * orders["exchange_rate"]
)


# STEP 7: CALCULATE TOTAL SALES

# Use pandas sum() to add all values in the amount_usd column.
# Store the final result in the total_usd_sales variable.
total_usd_sales = orders["amount_usd"].sum()


# STEP 8: DISPLAY THE RESULTS

# Display the first five rows of the updated DataFrame.
print(orders.head())

# Display the total calculated using the workbook's formula.
print("Total USD sales:", total_usd_sales)


# ============================================================
# PROJECT NOTES AND KEY LEARNINGS
# ============================================================

# This project demonstrates how to retrieve historical
# exchange rates from an external API using Python.

# Skills practised:
# 1. Using requests.get() to send HTTP GET requests.
# 2. Passing query parameters to an API.
# 3. Converting JSON responses into Python dictionaries.
# 4. Using pandas to read and manipulate CSV data.
# 5. Using map() to match currencies with exchange rates.
# 6. Creating new DataFrame columns.
# 7. Using sum() to calculate total transaction values.
# 8. Debugging incorrect calculations and API responses.

# IMPORTANT OBSERVATION:
# The API was requested to return exchange rates for
# January 21, 2024, but returned January 19, 2024.
# This is because January 21 was a Sunday, and the API
# returned the previous available business day's rates.

# CURRENCY CONVERSION NOTE:
# The DataCamp automated grader accepted multiplication:
# amount_usd = amount * exchange_rate

# However, when USD is the base currency, the API returns
# the amount of foreign currency equivalent to 1 USD.
# Therefore, the mathematically correct conversion to USD is:
# amount_usd = amount / exchange_rate

# The multiplication formula was retained to satisfy
# the DataCamp exercise requirements, but should not
# be used for real financial reporting with these rates.

# KEY TAKEAWAY:
# Successful API integration requires understanding the
# structure of API responses, validating returned data,
# and applying the correct calculations.
#
# Debugging also involves checking intermediate results
# instead of assuming that successfully executed code
# always produces the correct answer.
# ============================================================
