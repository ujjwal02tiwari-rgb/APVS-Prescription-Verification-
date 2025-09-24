import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./pharmbot.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    OCR_MODEL_PATH: str = os.getenv("OCR_MODEL_PATH", "./ml_models/ocr_model_v1")
    NLP_MODEL_PATH: str = os.getenv("NLP_MODEL_PATH", "./ml_models/nlp_model_v1")
    QUICK_COMMERCE_API_KEYS: dict = {
        "blinkit": os.getenv("BLINKIT_API_KEY", "dummy"),
        "zepto": os.getenv("ZEPTO_API_KEY", "dummy")
    }

settings = Settings()
