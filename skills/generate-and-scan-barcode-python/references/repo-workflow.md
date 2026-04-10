# Python submodule workflow

Use this reference when the task edits SDK source, tests, snippets, package metadata, or generated files inside `submodules/python`.

## Layout

- `aspose_barcode_cloud/api`: generated API clients such as `generate_api.py`, `recognize_api.py`, and `scan_api.py`.
- `aspose_barcode_cloud/models`: generated request and response models plus enums.
- `aspose_barcode_cloud/configuration.py`, `api_client.py`, `rest.py`, and `exceptions.py`: auth, HTTP transport, and runtime behavior.
- `docs`: generated endpoint and model docs.
- `tests`: unittest coverage for configuration, auth, headers, generate, recognize, scan, exceptions, and end-to-end flows.
- `snippets`: runnable documentation snippets grouped by generate/read scenario.
- `scripts`: snippet runners and post-generation helpers such as example insertion and deprecation-warning injection.
- `README.md` and `example.py`: user-facing usage examples.

## Validation

On Windows, run repo scripts and Make targets through WSL.

From `submodules/python`:

- `make init` or `make venv` to install dependencies.
- `make format`
- `make lint`
- `make test`
- `make test-example`
- `make test-tox`

`make test` does more than unit tests:

- runs `pytest --cov=aspose_barcode_cloud tests/`
- runs `./scripts/run_snippets.sh`

`run_snippets.sh` creates `snippets_test`, symlinks the local `aspose_barcode_cloud` package into it, injects credentials into each snippet, and executes every snippet. Treat snippet failures as consumer-facing regressions, not just sample breakage.

`make after-gen` is the post-processing pipeline used by code generation. It runs:

- `make format`
- `make insert-examples`
- `make add-warnings`
- `make format_doc`

## Test configuration

- Tests load `tests/configuration.json` first and then fall back to `TEST_CONFIGURATION_*` environment variables.
- `tests/load_configuration.py` maps constructor parameter names from `Configuration.__init__` directly to env vars.
- Useful names include `TEST_CONFIGURATION_CLIENT_ID`, `TEST_CONFIGURATION_CLIENT_SECRET`, `TEST_CONFIGURATION_ACCESS_TOKEN`, `TEST_CONFIGURATION_HOST`, and `TEST_CONFIGURATION_TOKEN_URL`.
- `tests/configuration.example.json` still shows an older v3.0 host, but `Configuration` defaults to `https://api.aspose.cloud/v4.0`. Match the surrounding file when editing repo code and prefer the runtime default for new examples.

## Regenerated code workflow

If you change generated SDK code in this mono-repo:

1. Make the intended SDK edit in `submodules/python` so the target behavior is clear.
2. Mirror the change in the matching template under `codegen/Templates/python` when the file is generated.
3. Stage the Python submodule changes.
4. From the repo root, run `make python` through WSL.
5. Ensure `submodules/python` has no new unstaged diffs after regeneration.
6. If regeneration reintroduces old code, keep fixing templates or post-generation helpers until the generated output matches the intended SDK change.

## Useful anchors

- `aspose_barcode_cloud/__init__.py`: public exports from the package.
- `tests/load_configuration.py`: how test config is discovered.
- `tests/test_generate_and_recognize.py`: end-to-end generate then recognize flow.
- `scripts/run_snippets.sh` and `scripts/run_snippet.sh`: snippet harness.
- `Makefile`: local validation and post-generation entry points.
