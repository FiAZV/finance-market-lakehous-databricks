import requests
from pprint import pprint

from src.config.settings import settings

api_key = settings.ALPHA_VANTAGE_API_KEY
print(f"API Key: {api_key}")  # Print the
url = 'https://www.alphavantage.co/query'
params = {
   "apikey": api_key,
   "function": "TIME_SERIES_DAILY",
   "symbol": "AAPL",
   "outputsize": "compact",
   "data_type": "json",
}
request = requests.get(url=url, params=params)
data = request.json()
pprint(data)