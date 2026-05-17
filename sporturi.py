"""
Aplicatie Flask pentru tema Sporturi.
Element ales: biliard.
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    functie_1_biliard,
    functie_2_biliard,
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
                color: #16a34a;
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
        </style>
    </head>
    <body>
        <div class="container">
            {continut}
        </div>
    </body>
    </html>
    """
@app.route("/sporturi/biliard/functie_1_biliard")
def ruta_functie_1_biliard():
    """Ruta 3: afiseaza informatii generale despre biliard."""
    continut = "<h1>Informatii generale despre biliard</h1>"
    continut += functie_1_biliard()
    continut += '<a href="/sporturi/biliard">Inapoi la Biliard</a>'
    return pagina("Informatii generale", continut)


@app.route("/sporturi/biliard/functie_2_biliard")
def ruta_functie_2_biliard():
    """Ruta 4: afiseaza regulile de baza despre biliard."""
    continut = "<h1>Reguli de baza despre biliard</h1>"
    continut += functie_2_biliard()
    continut += '<a href="/sporturi/biliard">Inapoi la Biliard</a>'
    return pagina("Reguli de baza", continut)

@app.route("/sporturi")
def sporturi():
    """Pagina temei."""
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>Tema proiectului este Sporturi. Elementul ales pentru acest proiect este biliardul.</p>
        <a href="/sporturi/biliard">Biliard</a>
        """,
    )


@app.route("/sporturi/biliard")
def biliard():
    """Pagina elementului ales."""
    return pagina(
        "Biliard",
        """
        <h1>Biliard</h1>
        <p>Biliardul este un sport de precizie practicat pe o masa speciala, folosind bile si tacuri.</p>
        <p>In cadrul proiectului sunt prezentate informatii generale despre biliard si reguli de baza.</p>
        <a href="/sporturi/biliard/functie_1_biliard">Informatii generale</a>
        <a href="/sporturi/biliard/functie_2_biliard">Reguli de baza</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """,
    )


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
