from flask import Flask, redirect

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
        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


@app.route("/")
def index():
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
