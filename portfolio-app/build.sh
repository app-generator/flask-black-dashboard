#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt
pip install waitress
waitress-serve --port=5005 wsgi:app
