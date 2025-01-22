SRC=./aspose_barcode_cloud

.PHONY: all
all: format lint test-tox

.PHONY: check_git
check_git:
	git fetch origin
	git diff origin/main --exit-code

.PHONY: clean-git
clean-git:
	git clean -dfx --exclude='tests/configuration*.json'

.PHONY: clean-pyc
clean-pyc:
	find . -type f -name '*.pyc' -delete

.PHONY: dist
dist:
	python setup.py sdist bdist_wheel --universal

.PHONY: format
format:
	black --line-length=120 -v $(SRC) tests/ scripts/ snippets/ *.py

.PHONY: format_doc
format_doc:
	# Trim white space
	sed -i -e 's_[[:space:]]*$$__' README.md
	# Replace true->True false->False: sed -e "s/\b\(false\|true\)/\u\1/g"
	find . -type f -iname '*.md' -exec sed -i -e 's_\b\(false\|true\)_\u\1_g' '{}' \;

.PHONY: init
init:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt -r lint-requirements.txt -r test-requirements.txt

.PHONY: init-docker
init-docker:
	python -m pip install -r publish-requirements.txt -r requirements.txt

.PHONY: lint
lint:
	# stop the build if there are Python syntax errors or undefined names
	python -m flake8 aspose_barcode_cloud --count --select=E9,F63,F7,F82 --show-source --statistics --extend-exclude '.*'
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	python -m flake8 aspose_barcode_cloud --count --exit-zero --max-line-length=127 --statistics --extend-ignore=E501 --extend-exclude '.*'

.PHONY: publish
publish: check_git test-tox dist
	python -m twine upload dist/*

.PHONY: publish-docker
publish-docker: init-docker unittest dist
	python -m twine upload dist/* --verbose

.PHONY: test
test:
	python -m pytest --cov=aspose_barcode_cloud tests/
	./scripts/run_snippets.sh

.PHONY: cover
cover:
	python -Werror -m pytest --cov-report html:coverage --cov=aspose_barcode_cloud tests/

.PHONY: unittest
unittest:
	python -Werror -m unittest discover -v

.PHONY: test-example
test-example:
	python -Werror example.py

.PHONY: test-tox
test-tox:
	python -m tox $(SRC)

.PHONY: insert-examples
insert-examples:
	./scripts/insert-example.bash

.PHONY: add-warnings
add-warnings:
	./scripts/add-deprecation-warnings.bash

.PHONY: after-gen
after-gen: format insert-examples add-warnings format_doc

.PHONY: update
update:
	echo "Not implemented"
