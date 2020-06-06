.PHONY = help run-web

PYTHON=$(which python3 | grep "python3")

.DEFAULT: help

help:
	@echo "make help - (all guide instructions for Makefile)"

run-env:
	pipenv shell

run-web:
	PYTHON app/application.py