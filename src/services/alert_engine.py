from src.dtos import MarketDataDTO
from datetime import datetime


class AlertEngine:

    def __init__(self, output_path="alerts.txt"):
        self.price_history = {}
        self.volume_history = {}
        self.output_path = output_path
        self.window_size = 300
        self.threshold = 0.02

    def _write_alert(self, msg: str):
        timestamp = datetime.utcnow().isoformat()
        with open(self.output_path, "a") as f:
            f.write(f"{timestamp} - {msg}\n")

    def _safe_add(self, history: list, value):
        if value is not None:
            history.append(value)
            if len(history) > self.window_size:
                history.pop(0)

    def _percent_diff(self, current, avg):
        if current is None or avg is None or avg == 0:
            return None
        return abs(current - avg) / avg

    def evaluate(self, dto: MarketDataDTO):
        asset = dto.coingecko_id

        if asset not in self.price_history:
            self.price_history[asset] = []
            self.volume_history[asset] = []

        self._safe_add(self.price_history[asset], dto.price)
        self._safe_add(self.volume_history[asset], dto.volume)

        alerts = []

        if len(self.price_history[asset]) > 1:
            avg_price = sum(self.price_history[asset]) / len(self.price_history[asset])
            diff = self._percent_diff(dto.price, avg_price)

            if diff is not None and diff > self.threshold:
                msg = (
                    f"[PRICE ALERT] {asset.upper()} deviated > 2% "
                    f"(current={dto.price}, avg_5m={round(avg_price, 2)})"
                )
                alerts.append(msg)
                self._write_alert(msg)

        if len(self.volume_history[asset]) > 1:
            avg_vol = sum(self.volume_history[asset]) / len(self.volume_history[asset])
            diff = self._percent_diff(dto.volume, avg_vol)

            if diff is not None and diff > self.threshold:
                msg = (
                    f"[VOLUME ALERT] {asset.upper()} deviated > 2% "
                    f"(current={dto.volume}, avg_5m={round(avg_vol, 2)})"
                )
                alerts.append(msg)
                self._write_alert(msg)

        return alerts
