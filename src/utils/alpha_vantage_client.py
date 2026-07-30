
import requests
import logging
import os
import time
from typing import Any, Dict, Optional

from src.config.settings import settings

class AlphaVantageAPIError(Exception):
    """Exception raised for errors in the Alpha Vantage API response."""
    pass

class AlphaVantageClient:
    """
    Client for interacting with the Alpha Vantage API.
    """
    
    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_API_KEY
        self.url = settings.ALPHA_VANTAGE_BASE_URL
        
    def _get(self, params: dict, max_retries: int = 3, backoff_factor: int = 2) -> Dict[str, Any]:
        """Método privado para realizar chamadas HTTP GET com lógica de retentativa."""
        params["apikey"] = self.api_key

        for attempt in range(1, max_retries + 1):
            try:
                response = requests.get(self.base_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                # A Alpha Vantage pode retornar HTTP 200 contendo mensagens de erro no JSON
                if "Error Message" in data:
                    raise AlphaVantageAPIError(f"Erro na API Alpha Vantage: {data['Error Message']}")

                if "Note" in data:
                    # Avisa sobre estouro do rate limit (ex: 5 chamadas/minuto)
                    print(f"⚠️ Alerta de Rate Limit da API: {data['Note']}")

                if "Information" in data:
                    print(f"ℹ️ Informação da API: {data['Information']}")

                return data

            except (requests.RequestException, AlphaVantageAPIError) as err:
                if attempt == max_retries:
                    raise AlphaVantageAPIError(
                        f"Falha ao consultar a API após {max_retries} tentativas. Erro original: {err}"
                    )
                
                wait_time = backoff_factor ** attempt
                print(f"🔄 Tentativa {attempt}/{max_retries} falhou. Aguardando {wait_time}s antes de tentar novamente...")
                time.sleep(wait_time)

        return {}
        
    def fetch_time_series_daily(self, ticker: str, outputsize: str = "compact") -> Dict[str, Any]:
        """Get daily time series data for a given stock symbol from the Alpha Vantage API.
        
        Args:
            ticker (str): Stock ticker.
            outputsize (str) (optional): 'compact' (last 100 days) or full (complete historic).
        """
        params = {
            "apikey": self.api_key,
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "outputsize": outputsize
        }
        return self._get(params)

    def fetch_company_overview(self, symbol: str) -> Dict[str, Any]:
        """Get company overview data for a given stock symbol from the Alpha Vantage API."""
        params = {
            "function": "OVERVIEW",
            "symbol": symbol
        }
        return self._get(params)



# def fetch_alpha_advantage_api(params: dict) -> dict | None:
#     """
#         Fetch data from the Alpha Vantage API.
        
#         Args:
#             params (dict): A dictionary containing the parameters for the API request, without the apikey parameter.
            
#         Returns:
#             dict | None: A dictionary containing the API response data, or None if an error occurred
#     """
#     api_key = settings.ALPHA_VANTAGE_API_KEY
#     url = settings.ALPHA_VANTAGE_BASE_URL
    
#     params["apikey"] = api_key
    
#     try:
#         request = requests.get(url=url, params=params)
#         data = request.json()
#         return data
    
#     except requests.exceptions.RequestException as e:
#         logging.warning(f"Error fetching data from Alpha Vantage API: {e}")
#         return None