"""
Aplicatie pentru rugby.
"""


from flask import Flask, redirect
from app.lib.biblioteca_rugby import (
    reguli_rugby as info_reguli_rugby,
    echipament_rugby as info_echipament_rugby,
)

app = Flask(__name__)
def pagina(titlu: str, continut: str) -> str:
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Verdana, sans-serif;
                background: linear-gradient(135deg, #f0fdf4, #dcfce7);
                margin: 0;
                padding: 40px;
            }}

            .card {{
                background-color: #ffffff;
                max-width: 850px;
                margin: auto;
                padding: 35px;
                border-radius: 18px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
            }}

            h1 {{
                color: #166534;
                border-bottom: 3px solid #22c55e;
                padding-bottom: 10px;
            }}

            h2 {{
                color: #15803d;
                margin-top: 25px;
            }}

            p {{
                font-size: 17px;
                line-height: 1.7;
                color: #1f2937;
            }}

            .info {{
                background-color: #f0fdf4;
                border-left: 5px solid #22c55e;
                padding: 15px;
                margin: 20px 0;
                border-radius: 8px;
            }}

            a {{
                background-color: #16a34a;
                color: white;
                padding: 11px 18px;
                text-decoration: none;
                border-radius: 10px;
                display: inline-block;
                margin: 8px 5px 0 0;
                font-weight: bold;
            }}

            a:hover {{
                background-color: #15803d;
            }}
        </style>
    </head>


    <body>
        <div class="card">
            {continut}
        </div>
    </body>
    </html>
    """


@app.route("/")
def index():
    return redirect("/sporturi")


@app.route("/sporturi")
def sporturi():
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>

        <p>
        Aceasta aplicatie prezinta informatii despre un sport ales in cadrul
        proiectului de Servicii Cloud si Containerizare.
        </p>

        <div class="info">
            <h2>Sportul ales: Rugby</h2>
            <p>
            Rugby-ul este un sport de echipa bazat pe forta, strategie,
            viteza si colaborare intre jucatori.
            </p>
        </div>

        <a href="/sporturi/rugby">Deschide pagina Rugby</a>
        """
    )


@app.route("/sporturi/rugby")
def rugby():
    return pagina(
        "Rugby",
        """
        <h1>Rugby</h1>

        <p>
        Rugby-ul este un sport practicat de doua echipe, in care jucatorii
        incearca sa avanseze cu mingea ovala spre terenul de tinta al adversarilor.
        Spre deosebire de alte sporturi, pasele inainte nu sunt permise,
        iar jocul pune accent pe disciplina, contact fizic si lucru in echipa.
        </p>

        <div class="info">
            <h2>Informatii disponibile</h2>
            <p>
            Mai jos pot fi accesate doua pagini cu informatii specifice despre rugby:
            cateva reguli de baza si echipamentele necesare.
            </p>
        </div>

        <a href="/sporturi/rugby/reguli">Reguli Rugby</a>
        <a href="/sporturi/rugby/echipament">Echipament Rugby</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


@app.route("/sporturi/rugby/echipament")
def ruta_echipament_rugby():
    """Ruta pentru echipamentul folosit in rugby."""
    continut = "<h1>Echipament Rugby</h1>"
    continut += info_echipament_rugby()
    continut += '<a href="/sporturi/rugby">Inapoi la Rugby</a>'
    continut += '<a href="/sporturi">Inapoi la Sporturi</a>'
    return pagina("Echipament Rugby", continut)


@app.route("/sporturi/rugby/reguli")
def ruta_reguli_rugby():
    """Ruta pentru regulile sportului rugby."""
    continut = "<h1>Reguli Rugby</h1>"
    continut += info_reguli_rugby()
    continut += '<a href="/sporturi/rugby">Inapoi la Rugby</a>'
    continut += '<a href="/sporturi">Inapoi la Sporturi</a>'
    return pagina("Reguli Rugby", continut)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011, debug=True)
