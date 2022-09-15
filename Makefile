SRC=./aspose_barcode_cloud

.PHONY: all
all: format lint test-tox

.PHONY: check_git
check_git:
	git fetch origin
	git diff origin/main --exit-code

.PHONY: clean
clean:
	git clean -dfx --exclude='tests/configuration*.json'

.PHONY: dist
dist:
	python3 setup.py sdist bdist_wheel --universal

.PHONY: format
format: format_code format_doc

.PHONY: format_code
format_code:
	python3 -m black --line-length=120 -v $(SRC) tests

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
	python3 -m pip install -r publish-requirements.txt

.PHONY: lint
lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --extend-exclude '.*'
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-line-length=127 --statistics --extend-ignore=E501 --extend-exclude '.*'

.PHONY: publish
publish: check_git test-tox clean dist
	python3 -m twine upload dist/*

.PHONY: publish-docker
publish-docker: init-docker test-tox dist
	python3 -m twine upload dist/* --verbose

.PHONY: test
test:
	python -Werror -m pytest --cov tests/

.PHONY: test-example
test-example:
	python -Werror example.py

.PHONY: test-tox
test-tox:
	tox $(SRC)

.PHONY: update
update:
	echo "Not implemented"
