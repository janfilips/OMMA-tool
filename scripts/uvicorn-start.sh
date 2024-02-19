#!/bin/sh
poetry run uvicorn backend.main:app --port 8000 --log-level info --reload
