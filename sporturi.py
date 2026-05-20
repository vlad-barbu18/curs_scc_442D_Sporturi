"""
Aplicatie Flask pentru tema sporturi.
Element ales: tenis de camp.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_tenis,
    functie_2_tenis,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial;
                background: #eaf4ff;
                padding: 30px;
            }}

            .container {{
                background: white;
                max-width: 900px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
            }}

            h1 {{
                color: #1d4ed8;
            }}

            h2 {{
                color: #1643a3;
            }}

            a {{
                background: #2563eb;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin: 5px;
            }}

            p, li {{
                font-size: 17px;
                line-height: 1.5;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            {continut}
        </div>
    </body>
    </html>
    """


@app.route("/sporturi")
def tema():
    """Pagina principala a temei."""
    continut = """
    <h1>Tema: Sporturi</h1>

    <p>Sporturile reprezinta activitati fizice organizate, practicate individual sau in echipa,
    avand rol important in mentinerea sanatatii, dezvoltarea disciplinei si imbunatatirea conditiei fizice.</p>

    <p>Elementul ales pentru acest proiect este <b>tenisul de camp</b>.</p>

    <a href="/sporturi/tenis">Tenis de camp</a>
    """

    return pagina("Sporturi", continut)


@app.route("/sporturi/tenis")
def tenis():
    """Pagina elementului ales."""
    continut = """
    <h1>Tenis de camp</h1>

    <p>Tenisul de camp este un sport elegant, dinamic si competitiv, practicat pe diferite tipuri de suprafete:
    zgura, iarba sau hard. Acesta solicita viteza, coordonare, strategie si rezistenta fizica.</p>

    <a href="/sporturi/tenis/functie_1_tenis">Informatii generale</a>
    <a href="/sporturi/tenis/functie_2_tenis">Tehnici importante</a>
    <a href="/sporturi">Inapoi la tema</a>
    """

    return pagina("Tenis de camp", continut)


@app.route("/sporturi/tenis/functie_1_tenis")
def ruta_functie_1_tenis():
    """Ruta 3: afiseaza informatiile din functia 1."""
    continut = "<h1>Informatii despre tenis de camp</h1>"
    continut += functie_1_tenis()
    continut += '<a href="/sporturi/tenis">Inapoi</a>'

    return pagina("Informatii generale", continut)


@app.route("/sporturi/tenis/functie_2_tenis")
def ruta_functie_2_tenis():
    """Ruta 4: afiseaza informatiile din functia 2."""
    continut = "<h1>Tehnici in tenis de camp</h1>"
    continut += functie_2_tenis()
    continut += '<a href="/sporturi/tenis">Inapoi</a>'

    return pagina("Tehnici tenis", continut)


@app.route("/")
def index():
    """Redirect catre pagina principala a temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)