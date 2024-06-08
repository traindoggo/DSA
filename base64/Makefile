run:
	python -m src.main

.PHONY: test
test:
	python -m pytest

.PHONY: cov
cov:
	coverage run -m pytest

.PHONY: report
report:
	coverage report -m

.PHONY: html
html:
	coverage html
