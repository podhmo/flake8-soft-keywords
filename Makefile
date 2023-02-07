run-example:
	poetry run flake8 -v --enable-extension flake8-soft-keywords _examples/*.py
.PHONY: run-example