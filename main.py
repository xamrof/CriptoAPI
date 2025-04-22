from fastapi import FastAPI, Query
import httpx
import os
from dotenv import load_dotenv
import uvicorn
from services.coingecko import get_coingecko_prices

load_dotenv()

app = FastAPI(title="Cryptop API", description="API for fetching crypto prices from CoinGecko", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/price/coingecko")
async def get_price_from_coingecko(crypto_ids: str = Query(...), vs_currency: str = "usd"):
    return await get_coingecko_prices(crypto_ids, vs_currency)
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
