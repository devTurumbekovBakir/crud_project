# Variables
DOCKER_COMPOSE = docker-compose -f docker-compose.yaml
DOCKER_COMPOSE_PROD = docker-compose -f docker-compose.prod.yaml
PROJECT_NAME = crud_project

# Targets
.PHONY: help start stop logs test clean collec-tstatic

help:
	@echo "Available commands:"
	@echo "  make start         - Start the development environment"
	@echo "  make stop          - Stop all running containers"
	@echo "  make logs          - Tail logs for the Django service"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Clean up containers and volumes"
	@echo "  make collect-static - Collect static files for production"

# Start containers
start:
	$(DOCKER_COMPOSE) up --build -d

start-prod:
	$(DOCKER_COMPOSE_PROD) up --build -d

# Stop containers
stop:
	$(DOCKER_COMPOSE) down

stop-prod:
	$(DOCKER_COMPOSE_PROD) down

# View logs
logs:
	$(DOCKER_COMPOSE) logs -f django

logs-prod:
	$(DOCKER_COMPOSE) logs -f django

## Run tests
#test:
#	$(DOCKER_COMPOSE) exec django python manage.py test
#
#test:
#	$(DOCKER_COMPOSE_PROD) exec django python manage.py test

# Clean up containers and volumes
clean:
	$(DOCKER_COMPOSE) down -v
	$(DOCKER_COMPOSE_PROD) down -v

# Collect static files for production
collect-static:
	$(DOCKER_COMPOSE) exec django python manage.py collectstatic --noinput

collect-static-prod:
	$(DOCKER_COMPOSE_PROD) exec django python manage.py collectstatic --noinput

# Create Django superuser
create-admin:
	@echo "Creating Django superuser..."
	$(DOCKER_COMPOSE) exec django python manage.py createsuperuser

create-admin-prod:
	@echo "Creating Django superuser..."
	$(DOCKER_COMPOSE_PROD) exec django python manage.py createsuperuser