Leenkonnect - backend

This is the Django backend for Leenkonnect (service platform). See `core/settings.py` for configuration.

Quick start:

1. Create a virtualenv and install dependencies
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

2. Configure environment variables (DATABASE_URL, DJANGO_SECRET_KEY)
3. Run migrations
	python3 manage.py migrate
4. Run server
	python3 manage.py runserver

