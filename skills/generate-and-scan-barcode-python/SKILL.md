---
name: generate-and-scan-barcode-python
description: Write or update Python code that uses the Aspose.BarCode Cloud SDK (`aspose_barcode_cloud`; pip package `aspose-barcode-cloud`) to generate, recognize, or scan barcodes through Aspose's cloud REST API. Use this skill whenever the user wants barcode work in Python, touches files under `submodules/python`, or mentions `GenerateApi`, `RecognizeApi`, `ScanApi`, `ApiClient`, `Configuration`, `GenerateParams`, `RecognizeBase64Request`, or `ScanBase64Request`. The SDK has several easy-to-miss idioms, including constructing APIs from `ApiClient(Configuration(...))`, reading generate results from `.data`, using public `file_url` values for GET recognize and scan methods, base64-encoding body payloads yourself, and remembering that the install and import names differ.
---

# Generate and scan barcode in Python

The Python SDK is a thin generated client over the Aspose BarCode Cloud REST API. Most tasks come down to choosing the right API class (`GenerateApi`, `RecognizeApi`, or `ScanApi`), choosing the right transport variant (GET, base64 body, or multipart), and wiring `Configuration` into `ApiClient` correctly.

The package name and import name differ. Install `aspose-barcode-cloud`, then import from `aspose_barcode_cloud`.

## Quick start

Use these imports in most Python examples:

```python
from aspose_barcode_cloud import (
    ApiClient,
    Configuration,
    GenerateApi,
    RecognizeApi,
    ScanApi,
)
```

Prefer constructing API classes from one shared `ApiClient`:

```python
config = Configuration(
    client_id=client_id,
    client_secret=client_secret,
)
api_client = ApiClient(configuration=config)

generate_api = GenerateApi(api_client=api_client)
recognize_api = RecognizeApi(api_client=api_client)
scan_api = ScanApi(api_client=api_client)
```

If the task is repo maintenance inside `submodules/python`, read `references/repo-workflow.md`. If the task needs the closest existing example or snippet, read `references/snippet-map.md`.

## Authentication

Use one of these two patterns:

1. Let the SDK fetch an access token lazily from client credentials.

```python
config = Configuration(
    client_id=client_id,
    client_secret=client_secret,
)
```

2. Inject a pre-fetched bearer token.

```python
config = Configuration(
    access_token=token,
    host="https://api.aspose.cloud/v4.0",
)
```

`Configuration.access_token` fetches a token automatically when `_access_token` is empty but `client_id`, `client_secret`, and `token_url` are present.

Inside this repo, tests load `tests/configuration.json` first and then fall back to `TEST_CONFIGURATION_*` environment variables. Snippets usually check `TEST_CONFIGURATION_ACCESS_TOKEN` first, then fall back to client credentials. Mirror the surrounding file when editing existing repo code.

`Configuration` defaults to `host="https://api.aspose.cloud/v4.0"` and `token_url="https://id.aspose.cloud/connect/token"`. Some older repo artifacts still mention the v3.0 host; prefer the runtime default unless you are intentionally matching older behavior in that file.

## Choose the right API shape

Pick the operation first:

- `GenerateApi`: create a barcode image.
- `RecognizeApi`: decode one or more known barcode types and optionally tune recognition.
- `ScanApi`: auto-detect barcode types with the smallest API surface.

Then pick the transport variant based on what the caller has:

- Public internet URL to an image: use `recognize()` or `scan()`. `file_url` must be a public URL, not a local path.
- Local file object or stream: use `recognize_multipart()` or `scan_multipart()`.
- Raw bytes already in memory: base64-encode them yourself and use `recognize_base64()` or `scan_base64()`.
- Simple text plus query parameters for generation: use `generate()`.
- Structured generate payload: use `generate_body()`.
- Multipart-form generation: use `generate_multipart()` when the caller explicitly needs that shape.

Key method names:

- `generate`
- `generate_body`
- `generate_multipart`
- `recognize`
- `recognize_base64`
- `recognize_multipart`
- `scan`
- `scan_base64`
- `scan_multipart`

## Non-obvious SDK rules

1. Install `aspose-barcode-cloud`, but import from `aspose_barcode_cloud`.
2. Construct APIs as `GenerateApi(ApiClient(Configuration(...)))` or by reusing a shared `ApiClient`. Passing `Configuration` directly to an API class is the wrong shape for this SDK.
3. `generate()`, `generate_body()`, and `generate_multipart()` return an `ApiResponse`. The image bytes are in `response.data`, not in a model object or file path.
4. Recognize and scan methods return `BarcodeResponseList`. Iterate `result.barcodes` and read `barcode_value`, `type`, `region`, and `checksum`.
5. `recognize_base64()` and `scan_base64()` expect a base64 string in the request model. The SDK does not call `base64.b64encode()` for you.
6. `recognize()` and `recognize_multipart()` take one `DecodeBarcodeType`, but `RecognizeBase64Request.barcode_types` accepts a list.
7. `ScanApi` auto-detects barcode types and does not take a barcode-type filter or the recognition tuning parameters exposed by `RecognizeApi`.
8. GET-based recognize and scan methods only work with remote files reachable by URL. For local files, use multipart or base64.
9. `ApiClient` supports header override through `header_name` and `header_value`; tests use this to customize `x-aspose-client`.
10. Set `config.debug = True` when you need SDK and `urllib3` request logging.

## Common patterns

Generate and save a QR code:

```python
from aspose_barcode_cloud import (
    ApiClient,
    CodeLocation,
    Configuration,
    EncodeBarcodeType,
    GenerateApi,
)

config = Configuration(client_id=client_id, client_secret=client_secret)
api = GenerateApi(ApiClient(config))

response = api.generate(
    EncodeBarcodeType.QR,
    "hello from Python",
    text_location=CodeLocation.NONE,
)

with open("qr.png", "wb") as fh:
    fh.write(response.data)
```

Recognize a local file stream:

```python
from aspose_barcode_cloud import ApiClient, Configuration, DecodeBarcodeType, RecognizeApi

config = Configuration(client_id=client_id, client_secret=client_secret)
api = RecognizeApi(ApiClient(config))

with open("qr.png", "rb") as fh:
    result = api.recognize_multipart(DecodeBarcodeType.QR, fh)

for barcode in result.barcodes:
    print(barcode.barcode_value)
```

Auto-scan bytes already in memory:

```python
import base64

from aspose_barcode_cloud import ApiClient, Configuration, ScanApi, ScanBase64Request

config = Configuration(client_id=client_id, client_secret=client_secret)
api = ScanApi(ApiClient(config))

with open("unknown.png", "rb") as fh:
    payload = base64.b64encode(fh.read()).decode("utf-8")

result = api.scan_base64(ScanBase64Request(file_base64=payload))
```

## Working in this repo

Read `references/repo-workflow.md` when the task changes SDK source, tests, snippets, package metadata, or generated code in `submodules/python`.

Read `references/snippet-map.md` when the task needs example code, README-aligned snippets, or the closest existing pattern for generate, recognize, or scan scenarios.

## Final checklist

1. Use the correct package and import pair: `aspose-barcode-cloud` for install, `aspose_barcode_cloud` for imports.
2. Build API classes from `ApiClient(Configuration(...))`.
3. Choose GET only for public URLs, multipart for local files, and base64 request models for bytes already in memory.
4. Base64-encode request payloads yourself before calling `recognize_base64()` or `scan_base64()`.
5. Treat generate responses as `response.data` bytes and recognize/scan responses as `result.barcodes`.
6. When changing the repo, validate with the submodule workflow in `references/repo-workflow.md`.
