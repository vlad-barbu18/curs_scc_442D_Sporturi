"""
Aplicatie Flask pentru proiectul SCC.
Tema: sporturi
Element ales: ski
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

            p {{
                font-size: 18px;
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

            a:hover {{
                background: #1e40af;
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


@app.route("/")
def index():
    """Redirect spre pagina principala a temei."""
    return redirect("/sporturi")


@app.route("/sporturi")
def sporturi():
    """Pagina principala a temei sporturi."""
    continut = """
    <h1>Sporturi</h1>

    <p>
        Tema proiectului este sporturi, iar sportul ales pentru prezentare
        este ski-ul.
    </p>

    <p>
        Aplicatia prezinta informatii generale despre acest sport si poate fi
        extinsa ulterior cu pagini suplimentare, teste automate si rulare in Docker.
    </p>

    <a href="/sporturi/ski">Vezi pagina despre ski</a>
    """

    return pagina("Sporturi", continut)


@app.route("/sporturi/ski")
def ski():
    """Pagina elementului ales: ski."""
    continut = """
    <h1>Ski</h1>

    <p>
        Ski-ul este un sport de iarna practicat pe zapada, care presupune
        deplasarea pe partii cu ajutorul schiurilor.
    </p>

    <p>
        Acest sport combina echilibrul, viteza, coordonarea si controlul
        miscarii, fiind practicat atat recreativ, cat si la nivel competitiv.
    </p>

    <a href="/sporturi">Inapoi la Sporturi</a>
    """

    return pagina("Ski", continut)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)