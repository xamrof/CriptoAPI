from fastapi import APIRouter, HTTPException, Path, Query
from services.coingecko import get_coingecko_prices
from models.price import PriceResponse
from typing import List
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/coingecko",
    tags=["coingecko"],
    responses={404: {"description": "Not found"}}
)

@router.get("/prices", response_model=List  [PriceResponse], summary="Get prices from CoinGecko", description="Get prices from CoinGecko")
async def get_prices_from_coingecko(coin: List[str] = Query(..., description="List of cryptocurrency symbols"), vs_currency: str = "usd"):
    data = await get_coingecko_prices(coin, vs_currency)

    if data is None:
        logger.warning(f"Could not retrieve price for {coin}-{vs_currency} from Coingecko service via router.")
        raise HTTPException(status_code=404, detail=f"Could not retrieve price data for symbol '{coin}' against '{vs_currency}' from Binance. Check if the pair exists and try again.")

    return data

# @router.get("/price", response_model=PriceResponse, summary="Get price from CoinGecko")
# async def get_price_from_coingecko(symbol: str = Path(..., description="Coin"), vs_currency: str = "usd"):
#     # data = await get_coingecko_prices(symbol, vs_currency)

#     if data is None:
#         logger.warning(f"Could not retrieve price for {symbol}-{vs_currency} from Coingecko service via router.")
#         raise HTTPException(status_code=404, detail=f"Could not retrieve price data for symbol '{symbol}' against '{vs_currency}' from Binance. Check if the pair exists and try again.")

#     return data

