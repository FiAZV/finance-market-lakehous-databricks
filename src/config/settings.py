from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    """Centraliza todas as configurações de ambiente, URLs e caminhos do Lakehouse."""
    
    # --------------------------------------------------------------------------
    # Credentials and API Configurations
    # --------------------------------------------------------------------------
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", "")
    ALPHA_VANTAGE_BASE_URL: str = "https://www.alphavantage.co/query"
    
    # --------------------------------------------------------------------------
    # Catalogs and Schemas at Lakehouse
    # --------------------------------------------------------------------------
    CATALOG_NAME: str = os.getenv("DATABRICKS_CATALOG", "wolf_of_wallstreet")
    
    SCHEMA_BRONZE: str = "bronze_finance"
    SCHEMA_SILVER: str = "silver_finance"
    SCHEMA_GOLD: str = "gold_finance"
    
    # --------------------------------------------------------------------------
    # Tables and Volumes at Lakehouse
    # --------------------------------------------------------------------------
    LANDING_VOLUME_PATH: str = f"dbfs:/Volumes/landind"
    
    # Bronze Layer (Raw)
    RAW_STOCK_PRICES_TABLE: str = f"{CATALOG_NAME}.{SCHEMA_BRONZE}.raw_stock_prices"
    RAW_COMPANY_OVERVIEW_TABLE: str = f"{CATALOG_NAME}.{SCHEMA_BRONZE}.raw_company_overview"
    
    # Silver Layer (Clean / Enriched)
    SILVER_STOCK_PRICES_TABLE: str = f"{CATALOG_NAME}.{SCHEMA_SILVER}.fact_stock_prices"
    SILVER_COMPANY_OVERVIEW_TABLE: str = f"{CATALOG_NAME}.{SCHEMA_SILVER}.dim_company_overview"
    
    # Gold Layer (Aggregated / Analytics)
    GOLD_STOCK_PRICES_TABLE: str = f"{CATALOG_NAME}.{SCHEMA_GOLD}.fact_stock_prices"
    
    # --------------------------------------------------------------------------
    # Configurações de Ativos Padrão para Ingestão
    # --------------------------------------------------------------------------
    DEFAULT_TICKERS: list[str] = ["AAPL", "MSFT", "GOOGL", "NVDA"]

# Instância global para ser importada nos scripts
settings = Settings()