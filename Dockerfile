# Usage:
# docker build github.com/aspose-barcode-cloud/aspose-barcode-cloud-python -t barcode-cloud-python:$(git describe --tags)
# docker run barcode-cloud-python:$(git describe --tags) publish -e "TEST_CONFIGURATION_ACCESS_TOKEN=" -e "TWINE_PASSWORD="

FROM python:3-buster

RUN apt-get update \
	&& apt-get install -y python-pip \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /aspose-barcode-cloud-python
COPY . .

RUN echo '[pypi]\nusername = __token__\npassword = ${TWINE_PASSWORD}' > $HOME/.pypirc

ENTRYPOINT ["make", "publish-docker"]
