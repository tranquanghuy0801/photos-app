.PHONY = help run-web run-env

PYTHON=$(which python3 | grep "python3")

.DEFAULT: help

help:
	@echo "make help - (all guide instructions for Makefile)"
	@echo "make run-env - (run virtual environments)"
	@echo "make run-web - (run web using unicorn)"

run-env:
	pipenv shell

run-web:
	gunicorn wsgi:application --timeout 300