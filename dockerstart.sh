#!/bin/sh

echo "Activare venv"
. .venv/bin/activate

echo "Configurare FLASK_APP"
export FLASK_APP=sporturi

echo "Pornire aplicatie Flask"
exec flask run -h 0.0.0.0 -p 5000 --reload
