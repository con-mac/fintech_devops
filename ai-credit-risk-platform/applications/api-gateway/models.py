"""
Pydantic models for the API Gateway
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class HealthCheck(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Health status")
    version: str = Field(..., description="Application version")
    environment: str = Field(..., description="Environment name")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Check timestamp")


class UserBase(BaseModel):
    """Base user model"""
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="User email")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")
    is_active: bool = Field(default=True, description="User active status")


class UserCreate(UserBase):
    """User creation model"""
    password: str = Field(..., min_length=8, description="User password")


class User(UserBase):
    """User response model"""
    id: int = Field(..., description="User ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Authentication token model"""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")


class TokenData(BaseModel):
    """Token data model"""
    username: Optional[str] = None


class CreditRiskRequest(BaseModel):
    """Credit risk assessment request model"""
    applicant_id: str = Field(..., description="Unique applicant identifier")
    income: float = Field(..., gt=0, description="Annual income")
    credit_score: int = Field(..., ge=300, le=850, description="Credit score")
    debt_ratio: float = Field(..., ge=0, le=1, description="Debt-to-income ratio")
    employment_years: int = Field(..., ge=0, description="Years of employment")
    loan_amount: float = Field(..., gt=0, description="Requested loan amount")
    loan_purpose: str = Field(..., description="Purpose of the loan")
    
    class Config:
        schema_extra = {
            "example": {
                "applicant_id": "APP123456",
                "income": 75000.0,
                "credit_score": 720,
                "debt_ratio": 0.35,
                "employment_years": 5,
                "loan_amount": 250000.0,
                "loan_purpose": "MORTGAGE"
            }
        }


class CreditRiskResponse(BaseModel):
    """Credit risk assessment response model"""
    applicant_id: str = Field(..., description="Applicant identifier")
    risk_score: int = Field(..., ge=0, le=100, description="Calculated risk score")
    risk_level: str = Field(..., description="Risk level (LOW/MEDIUM/HIGH)")
    recommendation: str = Field(..., description="Recommendation (APPROVE/REVIEW/DECLINE)")
    assessment_date: datetime = Field(..., description="Assessment timestamp")
    assessor: str = Field(..., description="Assessor username")
    confidence_score: Optional[float] = Field(None, ge=0, le=1, description="Model confidence")
    factors: Optional[List[str]] = Field(None, description="Key risk factors")
    
    class Config:
        schema_extra = {
            "example": {
                "applicant_id": "APP123456",
                "risk_score": 25,
                "risk_level": "LOW",
                "recommendation": "APPROVE",
                "assessment_date": "2024-01-15T10:30:00Z",
                "assessor": "system",
                "confidence_score": 0.85,
                "factors": ["Good credit score", "Stable income"]
            }
        }


class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    status_code: int = Field(..., description="HTTP status code")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    request_id: Optional[str] = Field(None, description="Request identifier for tracking")


class AuditLog(BaseModel):
    """Audit log entry model"""
    id: int = Field(..., description="Log entry ID")
    user_id: Optional[int] = Field(None, description="User ID")
    action: str = Field(..., description="Action performed")
    resource: str = Field(..., description="Resource accessed")
    ip_address: str = Field(..., description="Client IP address")
    user_agent: Optional[str] = Field(None, description="User agent string")
    timestamp: datetime = Field(..., description="Event timestamp")
    details: Optional[dict] = Field(None, description="Additional details")
    
    class Config:
        from_attributes = True


class ComplianceCheck(BaseModel):
    """Compliance check model"""
    check_type: str = Field(..., description="Type of compliance check")
    status: str = Field(..., description="Check status")
    details: dict = Field(..., description="Check details")
    timestamp: datetime = Field(..., description="Check timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "check_type": "PCI_DSS",
                "status": "PASS",
                "details": {
                    "card_data_encrypted": True,
                    "access_logs_enabled": True
                },
                "timestamp": "2024-01-15T10:30:00Z"
            }
        } 