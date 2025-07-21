"""
Configuration settings for the API Gateway
"""

import os
from typing import List
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "AI-Powered Credit Risk Assessment Platform"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/fintech_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # External APIs
    OPEN_BANKING_API_URL: str = "https://api.openbanking.org"
    OPEN_BANKING_API_KEY: str = ""
    
    # Monitoring
    PROMETHEUS_ENABLED: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Compliance
    AUDIT_LOG_ENABLED: bool = True
    DATA_RETENTION_DAYS: int = 2555  # 7 years for financial data
    
    @validator("SECRET_KEY", pre=True)
    def validate_secret_key(cls, v):
        if v == "your-secret-key-change-in-production" and os.getenv("ENVIRONMENT") == "production":
            raise ValueError("SECRET_KEY must be set in production")
        return v
    
    @validator("ALLOWED_ORIGINS", pre=True)
    def validate_allowed_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @validator("ALLOWED_HOSTS", pre=True)
    def validate_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings() 