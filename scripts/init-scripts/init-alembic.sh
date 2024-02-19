#!/bin/sh
python scripts/set-alembic-url.py
alembic upgrade head

# Execute the original command (start the application)
exec "$@"
