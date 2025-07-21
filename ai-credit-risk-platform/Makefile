# AI-Powered Credit Risk Assessment Platform - Makefile
# Professional DevOps Makefile with comprehensive commands

.PHONY: help install test build deploy clean docker-build docker-push k8s-deploy terraform-apply security-scan compliance-check

# Default target
help: ## Show this help message
	@echo "AI-Powered Credit Risk Assessment Platform - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Development Commands
install: ## Install all dependencies
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	@echo "Installing pre-commit hooks..."
	pre-commit install

dev-setup: ## Set up development environment
	@echo "Setting up development environment..."
	make install
	make docker-build
	make k8s-setup-local
	@echo "Development environment ready!"

run-dev: ## Run development server
	@echo "Starting development server..."
	uvicorn applications.api_gateway.main:app --reload --host 0.0.0.0 --port 8000

# Testing Commands
test: ## Run all tests
	@echo "Running all tests..."
	pytest tests/ -v --cov=applications --cov-report=html --cov-report=term

test-unit: ## Run unit tests only
	@echo "Running unit tests..."
	pytest tests/unit/ -v

test-integration: ## Run integration tests only
	@echo "Running integration tests..."
	pytest tests/integration/ -v

test-security: ## Run security tests only
	@echo "Running security tests..."
	pytest tests/security/ -v

test-coverage: ## Run tests with coverage report
	@echo "Running tests with coverage..."
	pytest tests/ -v --cov=applications --cov-report=html --cov-report=term --cov-report=xml

# Code Quality Commands
lint: ## Run all linting checks
	@echo "Running linting checks..."
	flake8 applications/ tests/
	black --check applications/ tests/
	isort --check-only applications/ tests/
	mypy applications/

format: ## Format code with black and isort
	@echo "Formatting code..."
	black applications/ tests/
	isort applications/ tests/

# Docker Commands
docker-build: ## Build all Docker images
	@echo "Building Docker images..."
	docker build -t ai-credit-risk-platform:latest .
	docker build -t ai-credit-risk-platform:dev -f docker/Dockerfile.dev .

docker-push: ## Push Docker images to registry
	@echo "Pushing Docker images..."
	docker tag ai-credit-risk-platform:latest $(REGISTRY)/ai-credit-risk-platform:latest
	docker push $(REGISTRY)/ai-credit-risk-platform:latest

docker-clean: ## Clean Docker images and containers
	@echo "Cleaning Docker resources..."
	docker system prune -f
	docker image prune -f

# Kubernetes Commands
k8s-setup-local: ## Set up local Kubernetes environment
	@echo "Setting up local Kubernetes..."
	kind create cluster --name fintech-dev --config infrastructure/kubernetes/kind-config.yaml
	kubectl apply -f infrastructure/kubernetes/namespaces/
	kubectl apply -f infrastructure/kubernetes/storage/

k8s-deploy-dev: ## Deploy to development environment
	@echo "Deploying to development environment..."
	kubectl apply -f infrastructure/kubernetes/development/
	kubectl set image deployment/ai-credit-risk-platform ai-credit-risk-platform=ai-credit-risk-platform:latest -n development

k8s-deploy-prod: ## Deploy to production environment
	@echo "Deploying to production environment..."
	kubectl apply -f infrastructure/kubernetes/production/
	kubectl set image deployment/ai-credit-risk-platform ai-credit-risk-platform=ai-credit-risk-platform:latest -n production

k8s-clean: ## Clean up Kubernetes resources
	@echo "Cleaning Kubernetes resources..."
	kubectl delete -f infrastructure/kubernetes/development/ --ignore-not-found=true
	kubectl delete -f infrastructure/kubernetes/production/ --ignore-not-found=true

# Terraform Commands
terraform-init: ## Initialize Terraform
	@echo "Initializing Terraform..."
	cd infrastructure/terraform && terraform init

terraform-plan: ## Plan Terraform changes
	@echo "Planning Terraform changes..."
	cd infrastructure/terraform && terraform plan

terraform-apply: ## Apply Terraform changes
	@echo "Applying Terraform changes..."
	cd infrastructure/terraform && terraform apply -auto-approve

terraform-destroy: ## Destroy Terraform infrastructure
	@echo "Destroying Terraform infrastructure..."
	cd infrastructure/terraform && terraform destroy -auto-approve

# Security Commands
security-scan: ## Run all security scans
	@echo "Running security scans..."
	make trivy-scan
	make snyk-scan
	make zap-scan

trivy-scan: ## Run Trivy vulnerability scanner
	@echo "Running Trivy scan..."
	trivy fs --format sarif --output trivy-results.sarif .

snyk-scan: ## Run Snyk vulnerability scanner
	@echo "Running Snyk scan..."
	snyk test --severity-threshold=high

zap-scan: ## Run OWASP ZAP security scan
	@echo "Running OWASP ZAP scan..."
	# Placeholder for ZAP scan against running application

# Compliance Commands
compliance-check: ## Run compliance checks
	@echo "Running compliance checks..."
	python scripts/compliance/check_pci_dss.py
	python scripts/compliance/check_gdpr.py
	python scripts/compliance/check_sox.py

# Monitoring Commands
monitoring-setup: ## Set up monitoring stack
	@echo "Setting up monitoring stack..."
	kubectl apply -f monitoring/prometheus/
	kubectl apply -f monitoring/grafana/
	kubectl apply -f monitoring/elk/

monitoring-clean: ## Clean up monitoring stack
	@echo "Cleaning monitoring stack..."
	kubectl delete -f monitoring/prometheus/ --ignore-not-found=true
	kubectl delete -f monitoring/grafana/ --ignore-not-found=true
	kubectl delete -f monitoring/elk/ --ignore-not-found=true

# Database Commands
db-migrate: ## Run database migrations
	@echo "Running database migrations..."
	python scripts/database/migrate.py

db-seed: ## Seed database with test data
	@echo "Seeding database..."
	python scripts/database/seed.py

db-backup: ## Create database backup
	@echo "Creating database backup..."
	python scripts/database/backup.py

# CI/CD Commands
ci-test: ## Run CI pipeline tests
	@echo "Running CI pipeline tests..."
	make lint
	make test
	make security-scan
	make compliance-check

ci-build: ## Run CI pipeline build
	@echo "Running CI pipeline build..."
	make docker-build
	make docker-push

ci-deploy: ## Run CI pipeline deployment
	@echo "Running CI pipeline deployment..."
	make k8s-deploy-dev

# Git and GitHub Commands
git-push: ## Push to GitHub with interactive commit message and branch
	@echo "🚀 Interactive Git Push to GitHub"
	@echo ""
	@read -p "Enter commit message (e.g., 'feat: add FastAPI health endpoint'): " commit_msg; \
	read -p "Enter branch name (default: main): " branch_name; \
	branch_name=$${branch_name:-main}; \
	echo ""; \
	echo "📝 Commit message: $$commit_msg"; \
	echo "🌿 Branch: $$branch_name"; \
	echo ""; \
	read -p "Proceed with commit and push? (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		echo "✅ Proceeding with commit and push..."; \
		git add .; \
		git commit -m "$$commit_msg"; \
		if git remote get-url origin > /dev/null 2>&1; then \
			if git push origin $$branch_name; then \
				echo "✅ Successfully pushed to GitHub!"; \
			else \
				echo "❌ Failed to push to GitHub. Check your remote URL and permissions."; \
				echo "💡 Run: git remote -v to check your remote configuration"; \
			fi; \
		else \
			echo "❌ No remote 'origin' configured!"; \
			echo "💡 To add remote origin, run:"; \
			echo "   git remote add origin <your-github-repo-url>"; \
			echo "💡 Then run: make git-push again"; \
		fi; \
	else \
		echo "❌ Push cancelled."; \
	fi

git-status: ## Show git status and recent commits
	@echo "📊 Git Status:"
	@git status --short
	@echo ""
	@echo "📝 Recent Commits:"
	@git log --oneline -5

git-setup: ## Set up git repository with initial commit
	@echo "🔧 Setting up Git repository..."
	@if [ ! -d .git ]; then \
		git init; \
		echo "✅ Git repository initialized"; \
	else \
		echo "ℹ️  Git repository already exists"; \
	fi
	@echo ""
	@echo "📝 Creating initial commit..."
	@git add .
	@git commit -m "feat: initial project setup - AI Credit Risk Assessment Platform"
	@echo "✅ Initial commit created!"
	@echo ""
	@echo "🌐 To connect to GitHub:"
	@echo "   1. Create a new repository on GitHub"
	@echo "   2. Run: git remote add origin <your-github-repo-url>"
	@echo "   3. Run: make git-push"

git-remote-setup: ## Set up GitHub remote origin
	@echo "🌐 Setting up GitHub remote origin..."
	@read -p "Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): " repo_url; \
	if [ -n "$$repo_url" ]; then \
		git remote add origin "$$repo_url"; \
		echo "✅ Remote origin added: $$repo_url"; \
		echo "💡 You can now run: make git-push"; \
	else \
		echo "❌ No repository URL provided"; \
	fi

git-remote-check: ## Check current remote configuration
	@echo "🔍 Checking remote configuration..."
	@echo "Current remotes:"
	@git remote -v
	@echo ""
	@if git remote get-url origin > /dev/null 2>&1; then \
		echo "✅ Remote 'origin' is configured"; \
	else \
		echo "❌ No remote 'origin' configured"; \
		echo "💡 Run: make git-remote-setup to add it"; \
	fi

git-push-parent: ## Push entire project structure from parent directory
	@echo "🚀 Pushing entire project structure to GitHub"
	@echo ""
	@read -p "Enter commit message (e.g., 'feat: add AI credit risk platform project'): " commit_msg; \
	read -p "Enter branch name (default: main): " branch_name; \
	branch_name=$${branch_name:-main}; \
	echo ""; \
	echo "📝 Commit message: $$commit_msg"; \
	echo "🌿 Branch: $$branch_name"; \
	echo ""; \
	read -p "Proceed with commit and push from parent directory? (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		echo "✅ Proceeding with commit and push from parent directory..."; \
		cd ..; \
		git add .; \
		git commit -m "$$commit_msg"; \
		if git remote get-url origin > /dev/null 2>&1; then \
			if git push origin $$branch_name; then \
				echo "✅ Successfully pushed entire project structure to GitHub!"; \
			else \
				echo "❌ Failed to push to GitHub. Check your remote URL and permissions."; \
				echo "💡 Run: git remote -v to check your remote configuration"; \
			fi; \
		else \
			echo "❌ No remote 'origin' configured in parent directory!"; \
			echo "💡 To add remote origin, run from parent directory:"; \
			echo "   cd .. && git remote add origin <your-github-repo-url>"; \
			echo "💡 Then run: make git-push-parent again"; \
		fi; \
	else \
		echo "❌ Push cancelled."; \
	fi

# Utility Commands
clean: ## Clean all build artifacts
	@echo "Cleaning build artifacts..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage htmlcov/ .pytest_cache/

logs: ## Show application logs
	@echo "Showing application logs..."
	kubectl logs -f deployment/ai-credit-risk-platform -n development

status: ## Show application status
	@echo "Showing application status..."
	kubectl get pods -n development
	kubectl get services -n development

# Documentation Commands
docs-build: ## Build documentation
	@echo "Building documentation..."
	mkdocs build

docs-serve: ## Serve documentation locally
	@echo "Serving documentation..."
	mkdocs serve

# Backup and Recovery Commands
backup: ## Create full system backup
	@echo "Creating system backup..."
	make db-backup
	kubectl get all -n development -o yaml > backup/$(shell date +%Y%m%d_%H%M%S)_k8s_backup.yaml

restore: ## Restore from backup
	@echo "Restoring from backup..."
	@echo "Please specify backup file: make restore BACKUP_FILE=backup/YYYYMMDD_HHMMSS_k8s_backup.yaml"
	@if [ -n "$(BACKUP_FILE)" ]; then kubectl apply -f $(BACKUP_FILE); else echo "No backup file specified"; fi

# Environment Variables
export REGISTRY ?= ghcr.io
export KUBECONFIG ?= ~/.kube/config
export AWS_REGION ?= us-west-2
export ENVIRONMENT ?= development 