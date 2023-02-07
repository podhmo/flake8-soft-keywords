run-example:
	poetry run flake8 -v _examples/*.py
	# poetry run flake8 -v --enable-extension SK0 _examples/*.py
.PHONY: run-example