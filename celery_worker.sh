#!/bin/bash
source venv/bin/activate
celery -A app.celery worker --loglevel=info
