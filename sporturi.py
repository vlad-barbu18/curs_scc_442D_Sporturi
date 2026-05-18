"""
Aplicatie Flask pentru proiectul SCC.
Tema: Sporturi
Element ales: Balet
Dezvoltator: Borza Iustin
"""

from flask import Flask, redirect

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5eafa;
                padding: 30px;
            }}
            .container {{
                background: white;
                max-width: 900px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.12);
            }}
            h1 {{
                color: #7e22ce;
            }}
            h2 {{
                color: #be185d;
            }}
            p {{
                line-height: 1.6;
            }}
            a {{
                background: #9333ea;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin: 5px;
            }}
            a:hover {{
                background: #7e22ce;
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
    """Pagina principala a temei Sporturi."""
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>
            Tema proiectului este reprezentata de sporturi. In cadrul acestei
            aplicatii web am ales sa prezint baletul, o activitate care imbina
            miscarea fizica, disciplina, expresia artistica si coordonarea.
        </p>
        <p>
            Aplicatia este realizata folosind Flask si contine pagini separate
            pentru tema principala, elementul ales si doua categorii de informatii.
        </p>
        <a href="/sporturi/balet">Balet</a>
        """,
    )


@app.route("/sporturi/balet")
def balet():
    """Pagina elementului ales: Balet."""
    return pagina(
        "Balet",
        """
        <h1>Balet</h1>
        <p>
            Baletul este o forma de dans scenic care presupune tehnica,
            eleganta, control corporal si expresivitate. Acesta poate fi
            considerat atat arta, cat si activitate fizica, deoarece necesita
            antrenament constant, forta, flexibilitate si coordonare.
        </p>
        <p>
            In acest proiect sunt prezentate doua aspecte importante:
            stilurile de balet si echipamentul folosit de balerini.
        </p>
        <a href="/sporturi/balet/stiluri_balet">Stiluri de balet</a>
        <a href="/sporturi/balet/echipament_balet">Echipament de balet</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """,
    )


@app.route("/")
def index():
    """Redirect catre pagina principala."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
