from sqlalchemy.orm import Session
from .models import AssetMaster, HistoricalMarketData
from src.dtos.market_data_dto import MarketDataDTO


class MarketDataRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_asset_id(self, coingecko_id: str) -> int:
        asset = (
            self.db.query(AssetMaster)
            .filter(AssetMaster.coingecko_id == coingecko_id)
            .first()
        )

        if asset:
            return asset.id

        new_asset = AssetMaster(coingecko_id=coingecko_id)
        self.db.add(new_asset)
        self.db.commit()
        self.db.refresh(new_asset)
        return new_asset.id

    def insert_market_data(self, dto: MarketDataDTO):
        asset_id = self.get_asset_id(dto.coingecko_id)

        entry = HistoricalMarketData(
            asset_id=asset_id,
            timestamp=dto.timestamp,
            price=dto.price,
            volume=dto.volume,
            market_cap=dto.market_cap,
            high_24h=dto.high_24h,
            low_24h=dto.low_24h,
        )

        self.db.add(entry)
        self.db.commit()
