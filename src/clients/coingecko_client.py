import requests
from datetime import datetime
from src.dtos import MarketDataDTO
from src.config import coins


class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"

    def __init__(self, timeout=10):
        self.timeout = timeout

    def fetch_all(self) -> list[MarketDataDTO]:

        params = {
            "vs_currency": "usd",
            "ids": f"{coins.BTC},{coins.ETH},{coins.ZEC}",
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.timeout)
        response.raise_for_status()

        assets = response.json()

        result = []
        for item in assets:
            dto = MarketDataDTO(
                coingecko_id=item["id"],
                timestamp=datetime.utcnow(),
                price=item.get("current_price"),
                volume=item.get("total_volume"),
                market_cap=item.get("market_cap"),
                high_24h=item.get("high_24h"),
                low_24h=item.get("low_24h"),
            )
            result.append(dto)

        return result
