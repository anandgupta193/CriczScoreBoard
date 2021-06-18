.PHONY: lint clean build start install
lint:
	@flake8 .

clean:
	@find . -type f -name '*.pyc' -delete

build:
	@docker-compose up -d

start:
	@python3 src/server.py

install:
	@pip install -r requirements.txt
