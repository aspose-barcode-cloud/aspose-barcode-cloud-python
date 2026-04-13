# Snippet and example map

Use this reference when you want the closest existing Python pattern before writing new SDK code or when updating docs, snippets, and examples.

## Small end-user examples

- `example.py`: compact generate-then-recognize flow using `ApiClient(Configuration(...))`.
- `snippets/manual_fetch_token.py`: manual OAuth client-credentials token fetch without using the SDK.

## Generate patterns

- `snippets/generate/save/generate_get.py`: simple `generate()` and save-to-file flow.
- `snippets/generate/save/generate_body.py`: `generate_body()` with `GenerateParams`.
- `snippets/generate/save/generate_multipart.py`: multipart generation flow.
- `snippets/generate/set_text/*`: `EncodeData` and `EncodeDataType` examples.
- `snippets/generate/set_size/*`: width, height, resolution, and units examples.
- `snippets/generate/set_colorscheme/*`: foreground and background color examples.
- `snippets/generate/appearance/*`: richer `BarcodeImageParams` examples.

## Recognize and scan patterns

- `snippets/read/set_source/recognize_get.py`: recognize from a public URL.
- `snippets/read/set_source/recognize_multipart.py`: recognize from a local file stream.
- `snippets/read/set_source/recognize_body.py`: recognize from base64 bytes.
- `snippets/read/set_source/scan_get.py`: auto-scan from a public URL.
- `snippets/read/set_source/scan_multipart.py`: auto-scan from a local file stream.
- `snippets/read/set_source/scan_body.py`: auto-scan from base64 bytes.
- `snippets/read/set_target_types/*`: choosing a single `DecodeBarcodeType` or a list for `RecognizeBase64Request.barcode_types`.
- `snippets/read/set_quality/*`: `RecognitionMode` examples.
- `snippets/read/set_image_kind/*`: `RecognitionImageKind` examples.

## Tests worth copying

- `tests/test_generate_and_recognize.py`: generate a barcode, save it locally, and recognize it end to end.
- `tests/test_generate_api.py`: generate via GET, body, and multipart variants.
- `tests/test_recognize_api.py`: recognize via base64 body, multipart, and public URL.
- `tests/test_scan_api.py`: scan via base64 body, multipart, and public URL.
- `tests/test_auth.py`: client credential flow, external token flow, and unauthorized failures.
- `tests/test_headers.py`: custom `ApiClient` header override behavior.
- `tests/test_exception.py`: error and exception behavior.
- `tests/test_load_configuration.py`: config-file and environment loading behavior.
