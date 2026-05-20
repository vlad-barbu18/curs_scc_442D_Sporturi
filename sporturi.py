import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
# Importăm funcțiile tale din folderul app/lib
from app.lib.f1_logic import primii_trei_piloti, detalii_circuit

app = Flask(__name__)

BUTTON_STYLE = """
<style>
    .button {
        background-color: #e10600; /* Rosu F1 */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        font-family: sans-serif;
    }
</style>
"""

@app.route('/')
def home():
    return f"""
    {BUTTON_STYLE}
    <h1>Formula 1</h1>
    <p>Alege o sectiune de mai jos:</p>
    <a href="/formula1" class="button">Vezi Podium Actual</a>
    <a href="/circuit/Monaco" class="button">Detalii Circuit Monaco</a>
    <a href="/circuit/Spa" class="button">Detalii Circuit Spa</a>
    """

@app.route('/formula1')
def formula1():
    try:
        piloti = primii_trei_piloti()
        lista_html = "".join([f"<li>{p}</li>" for p in piloti])
        return f"""
        {BUTTON_STYLE}
        <h2>Podium F1</h2>
        <ul>{lista_html}</ul>
        <a href="/" class="button">Inapoi la Home</a>
        """
    except Exception as e:
        return f"Eroare: {str(e)}"

@app.route('/circuit/<nume>')
def circuit(nume):
    try:
        descriere = detalii_circuit(nume)
        return f"""
        {BUTTON_STYLE}
        <h2>Circuit: {nume}</h2>
        <p>{descriere}</p>
        <a href="/" class="button">Inapoi la Home</a>
        """
    except Exception as e:
        return f"Eroare: {str(e)}"

if __name__ == '__main__':
    # Rulăm pe 0.0.0.0 pentru a fi accesibil din afara containerului
    app.run(host='0.0.0.0', port=5000)
