.PHONY: clean-pyc clean-build test

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr src/*.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

release: sdist
	twine check dist/*
	twine upload dist/*

sdist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

flake8:
	flake8 .

black:
	black --skip-string-normalization --line-length 120 .

