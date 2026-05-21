"""
Aplicatie Flask pentru tema Badminton.
Element ales: badminton.
"""

from flask import Flask, redirect

from app.lib.biblioteca_badminton import (
    reguli_badminton,
    echipament_badminton,
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
                font-family: Verdana, sans-serif;
                background: linear-gradient(135deg, #ecfeff, #dbeafe);
                padding: 40px;
                margin: 0;
            }}

            .container {{
                background: white;
                max-width: 850px;
                margin: auto;
                padding: 35px;
                border-radius: 18px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
            }}

            h1 {{
                color: #0f766e;
                border-bottom: 3px solid #14b8a6;
                padding-bottom: 10px;
            }}

            h2 {{
                color: #1d4ed8;
                margin-top: 25px;
            }}

            p {{
                font-size: 18px;
                line-height: 1.6;
                color: #1f2937;
            }}

            .info {{
                background-color: #f0fdfa;
                border-left: 5px solid #14b8a6;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }}

            a {{
                background-color: #0f766e;
                color: white;
                padding: 11px 16px;
                text-decoration: none;
                border-radius: 9px;
                display: inline-block;
                margin: 6px;
                font-weight: bold;
            }}

            a:hover {{
                background-color: #115e59;
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


@app.route("/badminton")
def badminton():
    """Pagina temei."""
    return pagina(
        "Badminton",
        """
        <h1>Badminton</h1>

        <p>
        Tema proiectului este <b>Badminton</b>. Aceasta pagina prezinta
        pe scurt sportul ales si ofera acces catre pagina de prezentare.
        </p>

        <div class="info">
            <h2>Element ales: Badminton</h2>
            <p>
            Badmintonul este un sport rapid, practicat cu rachete si fluturas,
            in care conteaza reflexele, precizia si viteza de reactie.
            </p>
        </div>

        <a href="/badminton/prezentare">Deschide prezentarea</a>
        """
    )


@app.route("/badminton/prezentare")
def prezentare_badminton():
    """Pagina elementului ales."""
    return pagina(
        "Prezentare Badminton",
        """
        <h1>Prezentare Badminton</h1>

        <p>
        Badmintonul poate fi jucat la simplu sau la dublu. Jucatorii lovesc
        fluturasul peste fileu, incercand sa il trimita in terenul adversarului
        astfel incat acesta sa nu il poata returna corect.
        </p>

        <div class="info">
            <h2>Caracteristici principale</h2>
            <p>
            Sportul combina viteza, coordonarea, rezistenta si strategia.
            Este diferit de tenis prin folosirea fluturasului si prin ritmul
            foarte rapid al schimburilor.
            </p>
        </div>

        <a href="/badminton/prezentare/reguli_badminton">Reguli badminton</a>
        <a href="/badminton/prezentare/echipament_badminton">Echipament badminton</a>
        <a href="/badminton">Inapoi la Badminton</a>
     """
    )


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/badminton")

@app.route("/badminton/prezentare/reguli_badminton")
def ruta_reguli_badminton():
    """Ruta 3: afiseaza regulile pentru badminton."""
    continut = "<h1>Reguli de badminton</h1>"
    continut += reguli_badminton()
    continut += '<a href="/badminton/prezentare">Inapoi</a>'
    return pagina("Reguli Badminton", continut)


@app.route("/badminton/prezentare/echipament_badminton")
def ruta_echipament_badminton():
    """Ruta 4: afiseaza echipamentul pentru badminton."""
    continut = "<h1>Echipament de badminton</h1>"
    continut += echipament_badminton()
    continut += '<a href="/badminton/prezentare">Inapoi</a>'
    return pagina("Echipament Badminton", continut)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
