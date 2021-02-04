# Usage:
# docker build github.com/aspose-barcode-cloud/aspose-barcode-cloud-python -t barcode-cloud-python:$(git describe --tags)
# docker run barcode-cloud-python:$(git describe --tags) publish -e "TEST_CONFIGURATION_ACCESS_TOKEN=" -e "TWINE_PASSWORD="

FROM python:latest

WORKDIR /aspose-barcode-cloud-python
COPY . .

RUN pip install -r publish-requirements.txt

ENTRYPOINT ["make"]
CMD ["publish", "--username=__token__"]
