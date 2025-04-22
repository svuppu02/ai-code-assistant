import os
from pydantic_settings import BaseSettings
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "AI Code Assistant"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # LLM Settings
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")  # openai, anthropic, etc.
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    #ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gpt-4")

    # Vector DB Settings
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "./chroma_db")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "development_secret_key")

    class Config:
        case_sensitive = True


settings = Settings()