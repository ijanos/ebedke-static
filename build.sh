#!/bin/sh

if ! type poetry > /dev/null; then
  pip3 install -q poetry
  poetry install --no-dev
fi

mkdir -p build
poetry run generator ebedke.json
cp resources/* build/
