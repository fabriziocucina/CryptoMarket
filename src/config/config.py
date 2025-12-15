from pydantic_settings import BaseSettings


class Coins(BaseSettings):
    BTC: str = "bitcoin"
    ETH: str = "ethereum"
    ZEC: str = "zcash"


class DatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


coins = Coins()
db_settings = DatabaseSettings()
