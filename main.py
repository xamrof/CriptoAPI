from fastapi import FastAPI, Query
import httpx
import os
from typing import List
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="Cryptop API", description="API for fetching crypto prices from CoinGecko", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/price/coingecko")
async def get_price_from_coingecko(crypto_ids: str = Query(...), vs_currency: str = "usd"):
    ids_list = crypto_ids.split(",")
    ids = ",".join(ids_list)

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={vs_currency}"    
    final_data = {}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)
            for crypto_id, values in data.items():
                if vs_currency in values:
                    final_data[crypto_id] = {"source": "CoinGecko", "price": values[vs_currency]}
                else:
                    print(f"Missing {vs_currency} price for {crypto_id}")

            return final_data

        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
