.PHONY: install test run ci

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest -q

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

ci: install test
