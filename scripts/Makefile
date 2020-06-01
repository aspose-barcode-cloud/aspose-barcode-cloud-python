ROOT=..
SRC=$(ROOT)/aspose_barcode_cloud

.PHONY: all
all: format test

.PHONY: format
format:
	black --line-length=120 --target-version=py27 -v $(SRC)
	sed -i -e 's_[[:space:]]*$$__' $(ROOT)/README.md

.PHONY: test
test:
	tox $(SRC)

.PHONY: dist
dist: format test
	cd $(ROOT) && python3 setup.py sdist bdist_wheel

.PHONY: upload
upload: dist
	cd $(ROOT) && python3 -m twine upload --repository testpypi dist/*

.PHONY: clean
clean:
	cd $(ROOT) && git clean -dfx
