#!/bin/bash
export PYTHONPATH="${PYTHONPATH}:${PWD}"
pipenv run python-lambda-local \
-f lambda_handler \
-e local/local-environment-variables.json \
src/main/lambdas/driver.py \
local/local-event.json