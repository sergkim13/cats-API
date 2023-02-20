install:
	poetry install

start:
	poetry run uvicorn src.main:app --reload --port 8080

hooks:
	poetry run pre-commit run --all-files

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov-report term-missing --cov=src --cov-report xml

compose:
	docker compose --env-file .env.example -p cats_api up -d

stop:
	docker compose --env-file .env.example -p cats_api down

compose-test:
	docker compose --env-file .env.example -f docker-compose.test.yml -p testing up -d

test-stop:
	docker compose  --env-file .env.example -f docker-compose.test.yml -p testing down
