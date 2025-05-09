from core.config import settings
from typing import List
import httpx
import logging

logger = logging.getLogger(__name__)

async def get_coingecko_prices(symbols: List[str], vs_currency: str = "usd") -> dict | None:
    api_key = settings.COINGECKO_API_KEY.get_secret_value() if settings.COINGECKO_API_KEY else None
    base_url = settings.COINGECKO_API_URL
    endpoint = "/simple/price"
    final_data = []

    if not api_key:
        print("Warning: COINGECKO API KEY NOT FOUND")
        return None
    
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": api_key
    }

    ids = ",".join(symbols)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{base_url}{endpoint}?ids={ids}&vs_currencies={vs_currency}", headers=headers)
            response.raise_for_status()
            data = response.json()
            logger.info(data)
            for crypto_id, values in data.items():
                if vs_currency in values:
                    final_data.append({"source": "CoinGecko", "symbol": crypto_id, "currency": vs_currency, "price": values[vs_currency]})
                else:
                    print(f"Missing {vs_currency} price for {crypto_id}")
            logger.info(final_data)
            return final_data

        except Exception as e:
            return {"error": str(e)}