"""
AI-Powered Credit Risk Assessment Platform - API Gateway
Main FastAPI application entry point
"""

import os
import time
from contextlib import asynccontextmanager
from typing import Dict, Any
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import structlog

from .config import settings
from .auth import get_current_user
from .models import HealthCheck, User

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Prometheus metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

# Security
security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    logger.info("Starting AI Credit Risk Assessment Platform API Gateway")
    
    # Add startup tasks here (database connections, etc.)
    
    yield
    
    # Shutdown
    logger.info("Shutting down AI Credit Risk Assessment Platform API Gateway")
    # Add cleanup tasks here

# Create FastAPI app
app = FastAPI(
    title="AI-Powered Credit Risk Assessment Platform",
    description="Enterprise-grade FinTech platform for credit risk assessment using AI/ML",
    version="1.0.0",
    docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
    lifespan=lifespan
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

class MetricsMiddleware(BaseHTTPMiddleware):
    """Middleware to collect Prometheus metrics"""
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()
        
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(duration)
        
        return response

app.add_middleware(MetricsMiddleware)

# Health check endpoint
@app.get("/health", response_model=HealthCheck, tags=["Health"])
async def health_check() -> HealthCheck:
    """Health check endpoint"""
    return HealthCheck(
        status="healthy",
        version="1.0.0",
        environment=settings.ENVIRONMENT
    )

# Metrics endpoint for Prometheus
@app.get("/metrics", tags=["Monitoring"])
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "AI-Powered Credit Risk Assessment Platform API Gateway",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

# Protected endpoint example
@app.get("/api/v1/me", response_model=User, tags=["User"])
async def get_current_user_info(
    current_user: User = Depends(get_current_user)
) -> User:
    """Get current user information"""
    return current_user

# Credit risk assessment endpoint (placeholder for Phase 1)
@app.post("/api/v1/credit-risk/assess", tags=["Credit Risk"])
async def assess_credit_risk(
    request: Request,
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Assess credit risk for a given application
    This is a placeholder implementation for Phase 1 MVP
    """
    try:
        # Placeholder implementation - will be enhanced in later phases
        data = await request.json()
        
        # Simple rule-based risk assessment for MVP
        income = data.get("income", 0)
        credit_score = data.get("credit_score", 0)
        debt_ratio = data.get("debt_ratio", 0)
        
        # Basic risk calculation
        risk_score = 0
        if income < 30000:
            risk_score += 30
        if credit_score < 650:
            risk_score += 25
        if debt_ratio > 0.4:
            risk_score += 20
            
        risk_level = "LOW" if risk_score < 30 else "MEDIUM" if risk_score < 60 else "HIGH"
        
        logger.info(
            "Credit risk assessment completed",
            user_id=current_user.id,
            risk_score=risk_score,
            risk_level=risk_level
        )
        
        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "recommendation": "APPROVE" if risk_level == "LOW" else "REVIEW" if risk_level == "MEDIUM" else "DECLINE",
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "assessor": current_user.username
        }
        
    except Exception as e:
        logger.error("Credit risk assessment failed", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to assess credit risk"
        )

# Test endpoint without authentication
@app.post("/api/v1/credit-risk/test", tags=["Credit Risk"])
async def test_credit_risk_assessment(
    request: Request
) -> Dict[str, Any]:
    """
    Test credit risk assessment endpoint (no authentication required)
    This is for testing purposes only
    """
    try:
        data = await request.json()
        
        # Simple rule-based risk assessment for MVP
        income = data.get("income", 0)
        credit_score = data.get("credit_score", 0)
        debt_ratio = data.get("debt_ratio", 0)
        
        # Basic risk calculation
        risk_score = 0
        if income < 30000:
            risk_score += 30
        if credit_score < 650:
            risk_score += 25
        if debt_ratio > 0.4:
            risk_score += 20
            
        risk_level = "LOW" if risk_score < 30 else "MEDIUM" if risk_score < 60 else "HIGH"
        
        logger.info(
            "Test credit risk assessment completed",
            risk_score=risk_score,
            risk_level=risk_level
        )
        
        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "recommendation": "APPROVE" if risk_level == "LOW" else "REVIEW" if risk_level == "MEDIUM" else "DECLINE",
            "assessment_date": datetime.now(timezone.utc).isoformat(),
            "assessor": "test-system"
        }
        
    except Exception as e:
        logger.error("Test credit risk assessment failed", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to assess credit risk"
        )

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions"""
    logger.warning(
        "HTTP exception occurred",
        path=request.url.path,
        status_code=exc.status_code,
        detail=exc.detail
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions"""
    logger.error(
        "Unexpected error occurred",
        path=request.url.path,
        error=str(exc),
        exc_info=True
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True if settings.ENVIRONMENT == "development" else False
    ) 