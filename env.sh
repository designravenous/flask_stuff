#!/usr/bin/bash
source venv/bin/activate
export FLASK_APP=main_app.py
export FLASK_ENV=development
echo $FLASK_APP
echo $FLASK_ENV