SRC=./aspose_barcode_cloud

.PHONY: all
all: format test

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

.PHONY: test
test:
	tox $(SRC)

.PHONY: clean
clean:
	git clean -dfx --exclude='tests/configuration*.json'

.PHONY: dist
dist:
	python3 setup.py sdist bdist_wheel --universal

.PHONY: check_git
check_git:
	git fetch origin
	git diff origin/master --exit-code

.PHONY: publish
publish: check_git test clean dist
	python3 -m twine upload dist/*

.PHONY: init-docker
init-docker:
	python3 -m pip install -r publish-requirements.txt

.PHONY: publish-docker
publish-docker: init-docker test dist
	python3 -m twine upload dist/*

.PHONY: update
update:
	echo "Not implemented"
