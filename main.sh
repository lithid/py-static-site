#!/usr/bin/env bash

# -e: immediately exit if any command [1] has a non-zero exit status
# -u: a reference to any variable you haven't previously defined is an error
# -o pipefail: if a pipeline fails, that return code will be used as the return code of the whole pipeline
# -x: commands are printed to the terminal
set -euo pipefail

python3 src/main.py
cd docs && python3 -m http.server 8888
