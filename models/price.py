from pydantic import BaseModel, Field

class PriceResponse(BaseModel):
    crypto_id: str = Field(..., description="ID of the cryptocurrency")
    price: float = Field(..., description="Price of the cryptocurrency in USD")
    source: str = Field(..., description="Source of the price data")