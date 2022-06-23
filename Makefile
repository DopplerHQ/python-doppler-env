SHELL=/bin/bash
VENVDIR?=${HOME}/.virtualenvs
WORKDIR?=$(shell basename "$$PWD")
VENV?=$(VENVDIR)/$(WORKDIR)/bin
PYTHON?=$(VENV)/python
ACTIVATE?=$(VENV)/activate

.PHONY: create-virtual-env activate clean-pyc clean-build test

create-virtual-env:
	mkdir -p ~/.virtualenvs && \
	python3 -m venv $(VENVDIR)/$(WORKDIR) && \
	. $(ACTIVATE) && \
	pip install --upgrade pip setuptools && \
	pip install -r requirements.txt

activate:
	. $(ACTIVATE)

build:
	. $(ACTIVATE) && python -m build .

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr src/*.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

flake8:
	. $(ACTIVATE) && flake8 .

black:
	. $(ACTIVATE) && black --skip-string-normalization --line-length 120 .

