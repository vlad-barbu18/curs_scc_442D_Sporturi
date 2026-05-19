from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_padel,
    functie_2_padel,
)

app = Flask(__name__)

def pagina(titlu: str, continut: str) -> str:
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


@app.route("/sporturi")
def sporturi():
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>Tema proiectului este sporturi. Elementul ales este padel.</p>
        <a href="/sporturi/padel">Padel</a>
        """
    )


@app.route("/sporturi/padel")
def padel():
    return pagina(
        "Padel",
        """
        <h1>Padel</h1>
        <p>
            Padelul este un sport de racheta asemanator cu tenisul,
            jucat de obicei la dublu, pe un teren inchis cu pereti de sticla.
        </p>
        <p>
            Este un sport rapid, accesibil si popular datorita combinatiei
            dintre tehnica, strategie si lucru in echipa.
        </p>

        <a href="/sporturi/padel/functie_1_padel">Informatia 1</a>
        <a href="/sporturi/padel/functie_2_padel">Informatia 2</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )

@app.route("/sporturi/padel/functie_1_padel")
def ruta_functie_1_padel():
    continut = "<h1>Informatia 1 despre padel</h1>"
    continut += functie_1_padel()
    continut += '<a href="/sporturi/padel">Inapoi la Padel</a>'
    return pagina("Informatia 1", continut)


@app.route("/sporturi/padel/functie_2_padel")
def ruta_functie_2_padel():
    continut = "<h1>Informatia 2 despre padel</h1>"
    continut += functie_2_padel()
    continut += '<a href="/sporturi/padel">Inapoi la Padel</a>'
    return pagina("Informatia 2", continut)

@app.route("/")
def index():
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
