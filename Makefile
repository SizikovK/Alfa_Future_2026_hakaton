.DEFAULT_GOAL := help
PYTHON ?= python3
NPM ?= npm
BACKEND_PYTHON := $(CURDIR)/backend/.venv/bin/python

.PHONY: help install install-backend install-frontend check check-backend check-frontend format format-backend format-frontend test

help:
	@echo "make install          Install backend and frontend dependencies"
	@echo "make install-back     Create backend/.venv and install Python dev dependencies"
	@echo "make install-front    Install frontend dependencies from package-lock.json"
	@echo "make check            Check backend and frontend lint, formatting and TypeScript"
	@echo "make format           Format backend and frontend"
	@echo "make test             Run Python tests"

install: install-back install-front

install-back:
	$(PYTHON) -m venv backend/.venv
	$(BACKEND_PYTHON) -m pip install -r backend/requirements-dev.txt

install-front:
	cd frontend && $(NPM) ci

check: check-back check-front

check-back:
	cd backend && $(BACKEND_PYTHON) -m invoke check

check-front:
	cd frontend && $(NPM) run check

format: format-back format-front

format-back:
	cd backend && $(BACKEND_PYTHON) -m invoke format

format-front:
	cd frontend && $(NPM) run format

test:
	cd backend && $(BACKEND_PYTHON) -m invoke test
