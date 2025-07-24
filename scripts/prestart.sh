#! /usr/bin/env bash

set -e
set -x

# # Let the DB start
# python app/backend_pre_start.py

# # Run migrations
# alembic upgrade head

# Create initial data in DB
find .
find /data
python -m app.initial_data