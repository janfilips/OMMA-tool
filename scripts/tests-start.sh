#! /usr/bin/env bash
set -e

export PYTHONPATH=$PYTHONPATH:/usr/src/
python3 -m pytest -v
