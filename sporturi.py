"""
Aplicatie Flask pentru proiectul SCC - Sporturi.
Dezvoltator: Verde Mihai Gabriel
Element ales: sailing.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    competitii_sailing,
    echipament_sailing,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML cu stil personalizat pentru sailing."""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                margin: 0;
                font-family: Georgia, 'Times New Roman', serif;
                background: linear-gradient(135deg, #06283D, #1363DF, #47B5FF);
                min-height: 100vh;
                color: #f8fafc;
            }}

            .page {{
                max-width: 1000px;
                margin: 0 auto;
                padding: 40px 20px;
            }}

            .container {{
                background: rgba(255, 255, 255, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.25);
                backdrop-filter: blur(8px);
                padding: 35px;
                border-radius: 24px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
            }}

            .badge {{
                display: inline-block;
                padding: 7px 14px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.18);
                color: #e0f2fe;
                font-size: 14px;
                letter-spacing: 1px;
                text-transform: uppercase;
                margin-bottom: 15px;
            }}

            h1 {{
                font-size: 42px;
                margin: 10px 0 20px 0;
                color: #ffffff;
                border-bottom: 2px solid rgba(255, 255, 255, 0.25);
                padding-bottom: 12px;
            }}

            h2 {{
                color: #bae6fd;
                margin-top: 25px;
                font-size: 28px;
            }}

            p, li {{
                font-size: 18px;
                line-height: 1.8;
                color: #eef6ff;
            }}

            ul {{
                padding-left: 25px;
            }}

            b {{
                color: #ffffff;
            }}

            a {{
                border: 2px solid #ffffff;
                color: #ffffff;
                padding: 12px 18px;
                text-decoration: none;
                border-radius: 999px;
                display: inline-block;
                margin: 8px 6px 0 0;
                font-weight: bold;
                transition: 0.2s;
                background: transparent;
            }}

            a:hover {{
                background: #ffffff;
                color: #0f172a;
            }}

            .footer {{
                margin-top: 30px;
                font-size: 14px;
                color: #dbeafe;
                text-align: right;
            }}
        </style>
    </head>
    <body>
        <div class="page">
            <div class="container">
                <span class="badge">Proiect SCC - Sailing</span>
                {continut}
                <div class="footer">Verde Mihai Gabriel | Sport ales: Sailing</div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/sporturi")
def sporturi():
    """Pagina principala a temei."""
    return pagina(
        "Sporturi",
        """
        <h1>Proiect SCC - Sporturi</h1>
        <p>
            Aceasta aplicatie web prezinta informatii despre sportul ales
            pentru proiect: sailing.
        </p>
        <a href="/sporturi/sailing">Sailing</a>
        """,
    )


@app.route("/sporturi/sailing")
def sailing():
    """Pagina elementului ales."""
    return pagina(
        "Sailing",
        """
        <h1>Sailing</h1>
        <p>
            Sailing-ul este un sport nautic in care deplasarea ambarcatiunii
            se realizeaza cu ajutorul vantului, prin utilizarea velelor.
            Sportivii trebuie sa controleze directia, viteza si pozitia
            barcii in functie de vant, curenti si traseul competitiei.
        </p>
        <a href="/sporturi/sailing/competitii_sailing">Competitii sailing</a>
        <a href="/sporturi/sailing/echipament_sailing">Echipament sailing</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """,
    )


@app.route("/sporturi/sailing/competitii_sailing")
def ruta_competitii_sailing():
    """Afiseaza competitiile importante de sailing."""
    continut = "<h1>Competitii de sailing</h1>"
    continut += competitii_sailing()
    continut += '<a href="/sporturi/sailing">Inapoi</a>'
    return pagina("Competitii sailing", continut)


@app.route("/sporturi/sailing/echipament_sailing")
def ruta_echipament_sailing():
    """Afiseaza echipamentul folosit in sailing."""
    continut = "<h1>Echipament de sailing</h1>"
    continut += echipament_sailing()
    continut += '<a href="/sporturi/sailing">Inapoi</a>'
    return pagina("Echipament sailing", continut)


@app.route("/")
def index():
    """Redirect spre pagina principala."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
