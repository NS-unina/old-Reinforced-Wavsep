COMPOSE = docker-compose
MVN = mvn
build:
	$(MVN) package
	$(COMPOSE) build

up: build
	$(COMPOSE) up

down: 
	$(COMPOSE) down
