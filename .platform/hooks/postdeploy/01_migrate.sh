#!/bin/bash
# Migrations are skipped during initial deployment debugging
# To run migrations manually, SSH into the instance and run:
# source /var/app/venv/*/bin/activate
# cd /var/app/current
# python manage.py migrate
echo "Postdeploy: Skipping migrations (can be run manually later)"
exit 0
