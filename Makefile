start:
	poetry run uvicorn src.main:app --reload --port 8080

hooks:
	poetry run pre-commit run --all-files
