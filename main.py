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
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
