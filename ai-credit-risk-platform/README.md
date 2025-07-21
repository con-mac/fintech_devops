# AI-Powered Credit Risk Assessment Platform

An enterprise-grade FinTech platform for credit risk assessment using AI/ML, built with FastAPI and modern DevOps practices.

## 🚀 Project Overview

This platform demonstrates modern DevOps practices in the FinTech industry, featuring:

- **FastAPI** - High-performance API framework
- **Microservices Architecture** - Scalable and maintainable design
- **Security First** - DevSecOps practices with comprehensive scanning
- **Compliance Ready** - PCI-DSS, GDPR, SOX compliance features
- **Monitoring & Observability** - Prometheus, Grafana, structured logging
- **Container Orchestration** - Kubernetes deployment ready
- **Infrastructure as Code** - Terraform for cloud deployment

## 📋 Phase 1 MVP Features

- ✅ Basic FastAPI service with authentication
- ✅ Simple credit risk calculation (rule-based)
- ✅ Docker containerization
- ✅ Local development environment
- ✅ Basic security scanning
- ✅ Health checks and monitoring
- ✅ Professional Makefile for automation

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   API Gateway   │    │  User Service   │    │ Banking Service │
│   (FastAPI)     │    │   (Future)      │    │   (Future)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │  AI/ML Service  │
                    │   (Future)      │
                    └─────────────────┘
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **Python 3.11** - Latest stable Python version
- **Pydantic** - Data validation and settings
- **SQLAlchemy** - Database ORM
- **Alembic** - Database migrations

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Local development
- **Kubernetes** - Orchestration (Phase 2)
- **Terraform** - Infrastructure as Code (Phase 2)

### Security & Compliance
- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - bcrypt for security
- **CORS Protection** - Cross-origin security
- **Security Scanning** - Trivy, Snyk, OWASP ZAP

### Monitoring & Observability
- **Prometheus** - Metrics collection
- **Grafana** - Visualization dashboard
- **Structured Logging** - structlog for observability
- **Health Checks** - Application monitoring

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Make (for automation)

### Development Setup

1. **Clone and navigate to the project:**
   ```bash
   cd ai-credit-risk-platform
   ```

2. **Set up development environment:**
   ```bash
   make dev-setup
   ```

3. **Start the application:**
   ```bash
   make run-dev
   ```

4. **Or use Docker Compose:**
   ```bash
   docker-compose up -d
   ```

### Available Commands

```bash
# Development
make install          # Install dependencies
make run-dev         # Run development server
make test            # Run all tests
make lint            # Run code quality checks

# Docker
make docker-build    # Build Docker images
make docker-push     # Push to registry

# Security
make security-scan   # Run all security scans
make compliance-check # Run compliance checks

# Monitoring
make monitoring-setup # Set up monitoring stack

# Help
make help            # Show all available commands
```

## 📊 API Endpoints

### Health & Monitoring
- `GET /health` - Health check
- `GET /metrics` - Prometheus metrics
- `GET /docs` - API documentation (Swagger UI)

### Authentication
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/me` - Get current user info

### Credit Risk Assessment
- `POST /api/v1/credit-risk/assess` - Assess credit risk

### Example Usage

```bash
# Get health status
curl http://localhost:8000/health

# Get API documentation
curl http://localhost:8000/docs

# Assess credit risk (requires authentication)
curl -X POST http://localhost:8000/api/v1/credit-risk/assess \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "applicant_id": "APP123456",
    "income": 75000.0,
    "credit_score": 720,
    "debt_ratio": 0.35,
    "employment_years": 5,
    "loan_amount": 250000.0,
    "loan_purpose": "MORTGAGE"
  }'
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Application
ENVIRONMENT=development
SECRET_KEY=your-secret-key-change-in-production
DEBUG=true

# Database
DATABASE_URL=postgresql://fintech_user:fintech_password@localhost:5432/fintech_db
REDIS_URL=redis://localhost:6379/0

# Security
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
ALLOWED_HOSTS=localhost,127.0.0.1

# External APIs
OPEN_BANKING_API_URL=https://api.openbanking.org
OPEN_BANKING_API_KEY=your-api-key
```

## 🧪 Testing

### Run Tests
```bash
make test              # Run all tests
make test-unit         # Run unit tests only
make test-integration  # Run integration tests only
make test-security     # Run security tests only
make test-coverage     # Run tests with coverage
```

### Test Coverage
The project includes comprehensive test coverage for:
- Unit tests for all business logic
- Integration tests for API endpoints
- Security tests for authentication and authorization
- Performance tests for critical paths

## 🔒 Security Features

### Authentication & Authorization
- JWT token-based authentication
- Password hashing with bcrypt
- Role-based access control (RBAC)
- Session management

### Security Scanning
- **Trivy** - Container vulnerability scanning
- **Snyk** - Dependency vulnerability scanning
- **OWASP ZAP** - Web application security testing
- **Bandit** - Python security linting

### Compliance Features
- Audit logging for all operations
- Data retention policies
- GDPR compliance features
- PCI-DSS ready infrastructure

## 📈 Monitoring & Observability

### Metrics
- Prometheus metrics collection
- Custom business metrics
- Application performance monitoring
- Error tracking and alerting

### Logging
- Structured JSON logging
- Request/response logging
- Error tracking with context
- Performance profiling

### Dashboards
- Grafana dashboards for monitoring
- Real-time application metrics
- Business KPIs visualization
- Alert management

## 🚀 Deployment

### Local Development
```bash
docker-compose up -d
```

### Production Deployment
```bash
# Build and push images
make docker-build
make docker-push

# Deploy to Kubernetes
make k8s-deploy-prod
```

## 📚 Documentation

- [Architecture Documentation](docs/architecture/)
- [Deployment Guide](docs/deployment/)
- [Security Guidelines](docs/security/)
- [Compliance Documentation](docs/compliance/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the troubleshooting guide

## 🔮 Roadmap

### Phase 2 (Enhanced)
- [ ] Kubernetes orchestration
- [ ] Microservices architecture
- [ ] Redis caching integration
- [ ] Open Banking API integration
- [ ] Advanced monitoring

### Phase 3 (Production Ready)
- [ ] Multi-cloud deployment
- [ ] Advanced AI/ML integration
- [ ] Comprehensive security scanning
- [ ] Compliance automation
- [ ] Disaster recovery

### Phase 4 (Enterprise)
- [ ] Framework migration capability
- [ ] Advanced compliance features
- [ ] Performance optimization
- [ ] GitOps implementation
- [ ] MLOps integration

---

**Built with ❤️ for modern DevOps practices in FinTech** 