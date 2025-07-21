import pytest
from fastapi.testclient import TestClient
from applications.api_gateway.main import app

client = TestClient(app, headers={"Host": "localhost"})


class TestHealthEndpoint:
    """Test cases for the health check endpoint."""
    
    def test_health_endpoint_returns_200(self):
        """Test that the health endpoint returns a 200 status code."""
        response = client.get("/health")
        assert response.status_code == 200
    
    def test_health_endpoint_returns_json(self):
        """Test that the health endpoint returns JSON data."""
        response = client.get("/health")
        assert response.headers["content-type"] == "application/json"
    
    def test_health_endpoint_contains_required_fields(self):
        """Test that the health response contains required fields."""
        response = client.get("/health")
        data = response.json()
        
        assert "status" in data
        assert "version" in data
        assert "environment" in data
        assert "timestamp" in data
    
    def test_health_status_is_healthy(self):
        """Test that the health status is 'healthy'."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"
    
    def test_health_version_matches_expected(self):
        """Test that the version matches the expected value."""
        response = client.get("/health")
        data = response.json()
        assert data["version"] == "1.0.0"


class TestRootEndpoint:
    """Test cases for the root endpoint."""
    
    def test_root_endpoint_returns_200(self):
        """Test that the root endpoint returns a 200 status code."""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_root_endpoint_returns_json(self):
        """Test that the root endpoint returns JSON data."""
        response = client.get("/")
        assert response.headers["content-type"] == "application/json"
    
    def test_root_endpoint_contains_required_fields(self):
        """Test that the root response contains required fields."""
        response = client.get("/")
        data = response.json()
        
        assert "message" in data
        assert "version" in data
        assert "docs" in data
        assert "health" in data
    
    def test_root_message_contains_expected_text(self):
        """Test that the message contains expected text."""
        response = client.get("/")
        data = response.json()
        assert "AI-Powered Credit Risk Assessment Platform" in data["message"] 