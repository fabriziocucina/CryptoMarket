import time
from src.clients import CoinGeckoClient
from src.database import init_db, SessionLocal, MarketDataRepository
from src.services import AlertEngine


def main():
    print("Luxor Crypto Data Collector starting...")

    init_db()

    client = CoinGeckoClient()
    alert_engine = AlertEngine(output_path="alerts.txt")

    db = SessionLocal()
    repo = MarketDataRepository(db=db)

    while True:
        try:
            market_data_list = client.fetch_all()
            print("data received")

            for dto in market_data_list:
                repo.insert_market_data(dto)

                alerts = alert_engine.evaluate(dto)
                for a in alerts:
                    print(f"⚠ {a}")

            time.sleep(15)

        except KeyboardInterrupt:
            print("\n Stopping gracefully...")
            break

        except Exception as e:
            print(f" Error in loop: {e}")
            time.sleep(2)

    db.close()


if __name__ == "__main__" or __name__ == "src.main":
    main()
