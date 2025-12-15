from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import db_settings

DATABASE_URL = (
    f"postgresql+psycopg2://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}"
    f"@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
