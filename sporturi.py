import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
# Importăm funcțiile tale din folderul app/lib
from app.lib.f1_logic import primii_trei_piloti, detalii_circuit

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Sistem Monitorizare Formula 1</h1><p>Accesati /formula1 pentru detalii.</p>"

@app.route('/formula1')
def formula1():
    piloti = primii_trei_piloti()
    # Verificăm dacă este listă; dacă nu, afișăm direct obiectul pentru a nu da eroare
    if isinstance(piloti, list) and len(piloti) >= 3:
        return f"<h2>Podium F1:</h2><ul><li>{piloti[0]}</li><li>{piloti[1]}</li><li>{piloti[2]}</li></ul>"
    else:
        return f"<h2>Date Formula 1:</h2><p>{piloti}</p>"

@app.route('/circuit/<nume>')
def circuit(nume):
    descriere = detalii_circuit(nume)
    return f"<h2>Detalii Circuit {nume}:</h2><p>{descriere}</p>"

if __name__ == '__main__':
    # Rulăm pe 0.0.0.0 pentru a fi accesibil din afara containerului
    app.run(host='0.0.0.0', port=5000)
