from sqlalchemy import Column, Integer, String
from src.database.base import Base


class AssetMaster(Base):
    __tablename__ = "asset_master"

    id = Column(Integer, primary_key=True, autoincrement=True)
    coingecko_id = Column(String, unique=True, nullable=False)
