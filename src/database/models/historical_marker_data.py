from sqlalchemy import Column, Integer, Numeric, TIMESTAMP, ForeignKey
from src.database.base import Base


class HistoricalMarketData(Base):
    __tablename__ = "historical_market_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, ForeignKey("asset_master.id"), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    price = Column(Numeric)
    volume = Column(Numeric)
    market_cap = Column(Numeric)
    high_24h = Column(Numeric)
    low_24h = Column(Numeric)
