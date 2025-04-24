from pydantic import BaseModel, Field
from typing import Dict

class PriceResponse(BaseModel):
    source: str
    symbol: str
    currency: str
    price: float
    
