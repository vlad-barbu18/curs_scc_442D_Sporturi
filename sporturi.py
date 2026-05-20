"""
Aplicatie Flask pentru tema Sporturi.

Element ales: Inot.

Entry point: creeaza aplicatia Flask si inregistreaza blueprint-urile
corespunzatoare elementelor temei. Logica fiecarui element se afla in
app/routes/<element>.py
"""

from flask import Flask

from app.routes.inot import inot_bp

app = Flask(__name__)

# Inregistram blueprint-ul pentru elementul Inot
app.register_blueprint(inot_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
