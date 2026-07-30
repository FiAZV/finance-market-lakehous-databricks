import logging
import json

from src.utils.alpha_vantage_client import AlphaVantageClient
from src.config.settings import settings

if __name__ == "__main__":

    # Logging configuration
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Get tickers list from settings
    tickers = settings.DEFAULT_TICKERS
    path = settings.LANDING_VOLUME_PATH

    all_data = []
    
    for ticker in tickers:
        logging.info(f'Starting ingestion for ticker: {ticker}')
        data = AlphaVantageClient().fetch_time_series_daily(ticker=ticker)
        all_data.append(data)

    with open(VOLUME_PATH, "w", encoding="utf-8") as f:
            json.dump(dados_crus, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em: {VOLUME_PATH}")