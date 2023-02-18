start:
	poetry run uvicorn src.main:app --reload --port 8080

hooks:
	poetry run pre-commit run --all-files

test:
	poetry run pytest -vv

compose-test:
	docker compose -f docker-compose.test.yml -p testing up -d
