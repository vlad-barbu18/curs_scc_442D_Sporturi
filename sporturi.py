"""
Aplicatie Flask pentru tema Sporturi.
Element ales: biatlon.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_biatlon,
    functie_2_biatlon,
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
                max-width: 1000px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #1d4ed8;
            }}

            h2 {{
                color: #16a34a;
            }}

            p {{
                line-height: 1.6;
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

            img {{
                width: 100%;
                max-width: 700px;
                border-radius: 12px;
                margin-top: 20px;
                margin-bottom: 20px;
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
    """Pagina temei."""

    return pagina(
        "Sporturi",

        """
        <h1>Sporturi</h1>

        <p>
            Sporturile reprezinta activitati fizice importante pentru sanatate,
            dezvoltarea disciplinei si spiritului competitiv.
            Exista numeroase tipuri de sporturi: de vara, de iarna,
            individuale sau de echipa.
        </p>

        <p>
            In cadrul acestui proiect a fost ales sportul
            <b>biatlon</b>, un sport spectaculos de iarna.
        </p>

        <img src="https://tse4.mm.bing.net/th/id/OIP.X5Wqs5MuXp3VbPjMyKP5wgHaFj?rs=1&pid=ImgDetMain&o=7&rm=3">

        <br>

        <a href="/sporturi/biatlon">Acceseaza pagina despre biatlon</a>
        """
    )


@app.route("/sporturi/biatlon")
def sport():
    """Pagina elementului ales."""

    return pagina(
        "Biatlon",

        """
        <h1>Biatlon</h1>

        <p>
            Biatlonul este un sport de iarna care combina schiul fond
            cu tirul sportiv.
        </p>

        <p>
            Sportivii trebuie sa parcurga trasee pe schiuri,
            iar intre probele de viteza trebuie sa traga la tinta.
            Precizia este foarte importanta deoarece ratările
            aduc penalizari.
        </p>

        <img src="data:image/webp;base64,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">

        <br>

        <a href="/sporturi/biatlon/functie_1_biatlon">Informatii generale</a>

        <a href="/sporturi/biatlon/functie_2_biatlon">Competitii si reguli</a>

        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


@app.route("/sporturi/biatlon/functie_1_biatlon")
def ruta_functie_1_biatlon():
    """Ruta 3: afiseaza informatia 1."""

    continut = "<h1>Informatii generale despre biatlon</h1>"

    continut += functie_1_biatlon()

    continut += '<a href="/sporturi/biatlon">Inapoi</a>'

    return pagina("Informatii generale", continut)


@app.route("/sporturi/biatlon/functie_2_biatlon")
def ruta_functie_2_biatlon():
    """Ruta 4: afiseaza informatia 2."""

    continut = "<h1>Competitii si reguli</h1>"

    continut += functie_2_biatlon()

    continut += '<a href="/sporturi/biatlon">Inapoi</a>'

    return pagina("Competitii", continut)


@app.route("/")
def index():
    """Redirect spre pagina temei."""

    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
