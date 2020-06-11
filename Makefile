SRC=./aspose_barcode_cloud

.PHONY: all
all: format test

.PHONY: format
format:
	black --line-length=120 --target-version=py27 -v $(SRC)
	sed -i -e 's_[[:space:]]*$$__' README.md

.PHONY: test
test:
	tox $(SRC)

.PHONY: clean
clean:
	git clean -dfx --exclude='tests/configuration*.json'

.PHONY: dist
dist: clean
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish: format test dist
	python3 -m twine upload dist/*
