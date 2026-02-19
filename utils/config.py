import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    """Configuration settings for the application."""

    # API keys
    anthropic_api_key: str
    fred_api_key: str
    alpha_vantage_api_key: Optional[str] = None

    # MongoDB
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "credit_agent"

    # Agent configuration
    max_iterations: int = 10
    cache_ttl_hours: int = 1
    enable_caching: bool = True

    # LLM configuration
    model_name: str = "claude-sonnet-4-20250514"
    max_tokens: int = 4096
    temperature: float = 0.0

    # API Rate Limits
    fred_rate_limit: int = 120 # requests per minute
    yahoo_rate_limit: int = 2000 # requests per hour

    class Config:
        env_file = ".env"
        case_sensitive = True

