import os
import requests
import json
import pandas as pandas
from dotenv import load_dotenv
from datetime import date

load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

crypto_id = ["bitcoin", "ethereum", "tether", "usdt", "binancecoin", "cardano"]
vs_currency = "usd"

ids = ",".join(crypto_id)
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currency}"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": COINGECKO_API_KEY
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print("Data received from the API")
    print(json.dumps(data, indent=4))

    records = []
    extraction_date = date.today().strftime("%Y-%m-%d")
    
    for crypto_id, values in data.items():
        if vs_currency in values:
            records.append({
                'crypto_id': crypto_id,
                'price_usd': values[vs_currency],
                'extraction_date': extraction_date
            })
        else:
            print(f"Missing {vs_currency} price for {crypto_id}")

    # I NEED TO UPDATE WITH A DB LIKE SQLITE, THEN I NEED A UI TO DISPLAY THE DATA
    df = pandas.DataFrame(records)
    print("\nDataFrame:")
    print(df)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
