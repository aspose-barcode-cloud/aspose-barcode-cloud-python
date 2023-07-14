#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SRC_DIR="$( cd "${SCRIPT_DIR}/../aspose_barcode_cloud" &> /dev/null && pwd )"

find "${SRC_DIR}" -name "*.py" -exec python "${SCRIPT_DIR}/add-deprecation-warning.py" "{}" \;
