#!/bin/sh

echo "Activare venv:"
. .venv/bin/activate

echo "Configurare variabila mediu FLASK_APP"
export FLASK_APP=sporturi

echo "Start server:"
exec flask run -h 0.0.0.0 -p 5012 --reload
