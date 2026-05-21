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
    """Creeaza o pagina HTML cu stil comun."""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Trebuchet MS, Arial, sans-serif;
                background: linear-gradient(135deg, #fff7ed, #ffedd5, #fef3c7);
                padding: 40px;
                margin: 0;
            }}

            .container {{
                background: #ffffff;
                max-width: 1000px;
                margin: auto;
                padding: 38px;
                border-radius: 24px;
                box-shadow: 0 8px 25px rgba(120, 53, 15, 0.18);
            }}

            h1 {{
                color: #9a3412;
                border-bottom: 4px solid #f97316;
                padding-bottom: 12px;
                font-size: 36px;
            }}

            h2 {{
                color: #7c2d12;
                margin-top: 25px;
            }}

            p {{
                font-size: 18px;
                line-height: 1.7;
                color: #374151;
            }}

            .hero {{
                background: linear-gradient(135deg, #fed7aa, #fde68a);
                padding: 22px;
                border-radius: 18px;
                margin: 20px 0;
                border-left: 7px solid #ea580c;
            }}

            .info {{
                background-color: #fff7ed;
                border-left: 6px solid #fb923c;
                padding: 16px;
                border-radius: 14px;
                margin: 20px 0;
            }}

            .imagine {{
                width: 100%;
                max-height: 360px;
                object-fit: cover;
                border-radius: 20px;
                margin: 22px 0;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.20);
            }}

            .carduri {{
                display: flex;
                gap: 18px;
                margin-top: 22px;
                flex-wrap: wrap;
            }}

            .card {{
                flex: 1;
                min-width: 230px;
                background: #fffbeb;
                padding: 18px;
                border-radius: 18px;
                border-top: 5px solid #f59e0b;
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
            }}

            .card h2 {{
                margin-top: 0;
                color: #92400e;
            }}

            .btn {{
                color: white;
                padding: 12px 18px;
                text-decoration: none;
                border-radius: 12px;
                display: inline-block;
                margin: 8px 6px 0 0;
                font-weight: bold;
                transition: 0.2s;
            }}

            .btn:hover {{
                transform: translateY(-2px);
                opacity: 0.9;
            }}

            .btn-main {{
                background-color: #ea580c;
            }}

            .btn-reguli {{
                background-color: #2563eb;
            }}

            .btn-echipament {{
                background-color: #16a34a;
            }}

            .btn-back {{
                background-color: #6b7280;
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

        <div class="hero">
            <h2>Sport ales: Badminton</h2>
            <p>
            Badmintonul este un sport rapid si spectaculos, practicat cu rachete
            si fluturas. Jocul pune accent pe viteza, reflexe, precizie si
            capacitatea de a anticipa miscarile adversarului.
            </p>
        </div>

        <img class="imagine" src="/static/images/badminton.png" alt="Imagine badminton">

        <p>
        In cadrul acestui proiect este prezentata tema Badminton printr-o aplicatie
        web realizata in Flask. Aplicatia include o pagina de prezentare, o pagina
        cu reguli de baza si o pagina dedicata echipamentului necesar.
        </p>

        <div class="carduri">
            <div class="card">
                <h2>Viteza</h2>
                <p>
                Schimburile sunt rapide, iar jucatorii trebuie sa reactioneze
                imediat la directia fluturasului.
                </p>
            </div>

            <div class="card">
                <h2>Precizie</h2>
                <p>
                Loviturile trebuie controlate atent pentru a trimite fluturasul
                in zone greu de aparat.
                </p>
            </div>

            <div class="card">
                <h2>Coordonare</h2>
                <p>
                Badmintonul necesita miscare continua, echilibru si coordonare
                intre pozitionare si executia loviturii.
                </p>
            </div>
        </div>

        <a class="btn btn-main" href="/badminton/prezentare">Deschide prezentarea</a>
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
        Badmintonul poate fi jucat la simplu sau la dublu. Scopul jocului este
        trimiterea fluturasului peste fileu astfel incat acesta sa cada in terenul
        adversarului sau sa nu poata fi returnat corect.
        </p>

        <div class="info">
            <h2>Caracteristici generale</h2>
            <p>
            Spre deosebire de tenis, badmintonul foloseste un fluturas, nu o minge.
            Acesta are o traiectorie diferita, iar jocul devine foarte rapid si
            imprevizibil. Jucatorii trebuie sa fie atenti la pozitionare, timing
            si la alegerea loviturii potrivite.
            </p>
        </div>

        <div class="carduri">
            <div class="card">
                <h2>Joc simplu</h2>
                <p>
                Se joaca intre doi jucatori. Fiecare incearca sa controleze terenul
                si sa forteze adversarul sa greseasca.
                </p>
            </div>

            <div class="card">
                <h2>Joc dublu</h2>
                <p>
                Se joaca intre doua echipe de cate doi jucatori. Comunicarea si
                sincronizarea sunt foarte importante.
                </p>
            </div>

            <div class="card">
                <h2>Strategie</h2>
                <p>
                Jucatorii alterneaza lovituri scurte, lungi, rapide sau plasate
                pentru a castiga punctul.
                </p>
            </div>
        </div>

        <a class="btn btn-reguli" href="/badminton/prezentare/reguli_badminton">Reguli badminton</a>
        <a class="btn btn-echipament" href="/badminton/prezentare/echipament_badminton">Echipament badminton</a>
        <a class="btn btn-back" href="/badminton">Inapoi la Badminton</a>
        """
    )


@app.route("/badminton/prezentare/reguli_badminton")
def ruta_reguli_badminton():
    """Ruta 3: afiseaza regulile pentru badminton."""
    continut = "<h1>Reguli de badminton</h1>"
    continut += """
    <p>
    Regulile de baza definesc modul in care se executa serviciul, cum se castiga
    punctele si ce actiuni nu sunt permise in timpul jocului.
    </p>
    """
    continut += reguli_badminton()
    continut += '<a class="btn btn-back" href="/badminton/prezentare">Inapoi la Prezentare</a>'
    continut += '<a class="btn btn-main" href="/badminton">Inapoi la Badminton</a>'
    return pagina("Reguli Badminton", continut)


@app.route("/badminton/prezentare/echipament_badminton")
def ruta_echipament_badminton():
    """Ruta 4: afiseaza echipamentul pentru badminton."""
    continut = "<h1>Echipament de badminton</h1>"
    continut += """
    <p>
    Pentru practicarea badmintonului sunt necesare cateva elemente importante,
    precum racheta, fluturasul, fileul, incaltamintea potrivita si terenul
    delimitat corect.
    </p>
    """
    continut += echipament_badminton()
    continut += '<a class="btn btn-back" href="/badminton/prezentare">Inapoi la Prezentare</a>'
    continut += '<a class="btn btn-main" href="/badminton">Inapoi la Badminton</a>'
    return pagina("Echipament Badminton", continut)


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/badminton")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
