from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MarketDataDTO(BaseModel):
    coingecko_id: str
    timestamp: datetime
    price: Optional[float]
    volume: Optional[float]
    market_cap: Optional[float]
    high_24h: Optional[float]
    low_24h: Optional[float]
