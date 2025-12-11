#!/bin/bash
set -e
source /var/app/venv/*/bin/activate
cd /var/app/current
python manage.py migrate || echo "Migration failed - check RDS connectivity and credentials"
