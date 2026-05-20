"""
Aplicatie Flask pentru tema sporturi.
Element ales: tenis de camp.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_tenis,
    functie_2_tenis,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """pagina HTML"""
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>{titlu}</title>

        <style>

            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: 'Segoe UI', Arial, sans-serif;
                background:
                    radial-gradient(circle at top left, #38bdf8 0, transparent 30%),
                    radial-gradient(circle at bottom right, #1d4ed8 0, transparent 28%),
                    #020617;

                color: #e5e7eb;
            }}

            .page {{
                min-height: 100vh;
                padding: 40px 20px;
            }}

            .container {{
                max-width: 1150px;
                margin: auto;
            }}

            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;

                padding: 18px 24px;
                margin-bottom: 28px;

                border-radius: 22px;

                background: rgba(15, 23, 42, 0.78);
                border: 1px solid rgba(148, 163, 184, 0.25);

                backdrop-filter: blur(14px);
            }}

            .logo {{
                font-weight: 800;
                letter-spacing: 1px;
                color: #7dd3fc;
            }}

            .tag {{
                color: #cbd5e1;
                font-size: 14px;
            }}

            .hero {{
                background:
                    linear-gradient(
                        135deg,
                        rgba(37, 99, 235, 0.92),
                        rgba(14, 165, 233, 0.75)
                    );

                padding: 42px;

                border-radius: 30px;

                box-shadow:
                    0 25px 70px rgba(14, 165, 233, 0.25);

                border:
                    1px solid rgba(255, 255, 255, 0.22);

                margin-bottom: 24px;
            }}

            .badge {{
                display: inline-block;

                background: rgba(255, 255, 255, 0.18);

                color: white;

                padding: 8px 16px;

                border-radius: 999px;

                font-size: 14px;
                font-weight: 700;

                margin-bottom: 18px;
            }}

            h1 {{
                font-size: 48px;
                margin: 0 0 16px 0;
                color: white;
            }}

            h2 {{
                color: #7dd3fc;
                margin-top: 0;
            }}

            p, li {{
                font-size: 18px;
                line-height: 1.75;
                color: #dbeafe;
            }}

            ul {{
                padding-left: 24px;
            }}

            .grid {{
                display: grid;

                grid-template-columns:
                    repeat(auto-fit, minmax(240px, 1fr));

                gap: 18px;

                margin: 22px 0;
            }}

            .card {{
                background: rgba(15, 23, 42, 0.82);

                border:
                    1px solid rgba(148, 163, 184, 0.25);

                border-radius: 24px;

                padding: 24px;

                box-shadow:
                    0 18px 45px rgba(0, 0, 0, 0.25);

                backdrop-filter: blur(12px);

                transition: 0.25s;
            }}

            .card:hover {{
                transform: translateY(-4px);

                border-color:
                    rgba(56, 189, 248, 0.7);
            }}

            .metric {{
                font-size: 34px;
                font-weight: 800;
                color: #38bdf8;
                margin-bottom: 6px;
            }}

            .metric-label {{
                color: #cbd5e1;
                font-size: 15px;
            }}

            .section {{
                margin-top: 26px;
            }}

            a {{
                display: inline-block;

                margin: 12px 10px 0 0;

                padding: 13px 20px;

                border-radius: 14px;

                text-decoration: none;

                font-weight: 700;

                color: #020617;

                background:
                    linear-gradient(
                        135deg,
                        #7dd3fc,
                        #38bdf8
                    );

                box-shadow:
                    0 12px 28px rgba(56, 189, 248, 0.25);

                transition: 0.2s;
            }}

            a:hover {{
                transform: translateY(-2px);

                box-shadow:
                    0 18px 34px rgba(56, 189, 248, 0.35);
            }}

            .back {{
                background: #cbd5e1;
            }}

            footer {{
                margin-top: 28px;
                text-align: center;
                color: #94a3b8;
                font-size: 14px;
            }}

        </style>

    </head>

    <body>

        <div class="page">

            <div class="container">

                <div class="navbar">
                    <div class="logo">
                        TENIS DE CÂMP
                    </div>

                    <div class="tag">
                        Sport • Strategie • Precizie • Performanță
                    </div>
                </div>

                {continut}

                <footer>
                    Proiect SCC.
                </footer>

            </div>

        </div>

    </body>
    </html>
    """


@app.route("/sporturi")
def tema():
    """Pagina principala a temei."""

    continut = """
    <div class="hero">

        <span class="badge">
            Sport ales
        </span>

        <h1>
            Tenis de câmp
        </h1>

        <p>
            Tenisul de câmp este un sport elegant, rapid și strategic,
            practicat pe un teren împărțit de un fileu.
            Acesta dezvoltă coordonarea, viteza de reacție,
            concentrarea și rezistența fizică.
        </p>

        <a href="/sporturi/tenis">
            Descoperă sportul
        </a>

    </div>


    <div class="grid">

        <div class="card">

            <div class="metric">
                1 vs 1
            </div>

            <div class="metric-label">
                Meci simplu
            </div>

            <p>
                Un jucător concurează împotriva altui jucător
                pe terenul de tenis.
            </p>

        </div>


        <div class="card">

            <div class="metric">
                2 vs 2
            </div>

            <div class="metric-label">
                Meci de dublu
            </div>

            <p>
                Două echipe formate din câte doi jucători
                joacă pe același teren.
            </p>

        </div>


        <div class="card">

            <div class="metric">
                3
            </div>

            <div class="metric-label">
                Suprafețe principale
            </div>

            <p>
                Zgură, iarbă și hard.
                Fiecare suprafață influențează viteza jocului.
            </p>

        </div>

    </div>


    <div class="card section">

        <h2>
            Caracteristicile sportului
        </h2>

        <p>
            Tenisul combină partea fizică și partea tactică.
            Jucătorii trebuie să controleze direcția și viteza mingii,
            să anticipeze mișcările adversarului și să ia decizii rapide
            în timpul fiecărui schimb de mingi.
        </p>

        <p>
            Acest sport este practicat atât la nivel recreativ,
            cât și profesionist, existând competiții importante
            precum Wimbledon, Roland Garros, US Open și Australian Open.
        </p>

    </div>
    """

    return pagina("Sporturi", continut)


@app.route("/sporturi/tenis")
def tenis():
    """Pagina elementului ales."""

    continut = """
    <div class="hero">

        <span class="badge">
            Prezentare sport
        </span>

        <h1>
            Tenis de câmp
        </h1>

        <p>
            Tenisul de câmp este un sport în care mingea este lovită
            cu ajutorul unei rachete peste fileu,
            scopul fiind ca adversarul să nu poată returna mingea corect.
        </p>

        <a href="/sporturi/tenis/functie_1_tenis">
            Informații generale
        </a>

        <a href="/sporturi/tenis/functie_2_tenis">
            Tehnici importante
        </a>

        <a class="back" href="/sporturi">
            Înapoi
        </a>

    </div>


    <div class="grid">

        <div class="card">

            <h2>
                Reguli de bază
            </h2>

            <p>
                Mingea trebuie trimisă peste fileu și să cadă
                în terenul adversarului.
                Punctul se câștigă atunci când adversarul greșește
                sau nu poate returna mingea.
            </p>

        </div>


        <div class="card">

            <h2>
                Echipament
            </h2>

            <p>
                Pentru practicarea tenisului sunt necesare:
                rachetă, mingi speciale,
                încălțăminte adecvată și teren marcat.
            </p>

        </div>


        <div class="card">

            <h2>
                Calități dezvoltate
            </h2>

            <p>
                Tenisul dezvoltă viteza de reacție,
                coordonarea, rezistența fizică,
                concentrarea și strategia de joc.
            </p>

        </div>

    </div>


    <div class="card section">

        <h2>
            Importanța strategiei
        </h2>

        <p>
            În tenis, fiecare punct poate fi construit strategic.
            Jucătorii încearcă să controleze ritmul jocului,
            să plaseze mingea în zone dificile și
            să își surprindă adversarul prin variații de viteză și efect.
        </p>

    </div>
    """

    return pagina("Tenis de camp", continut)


@app.route("/sporturi/tenis/functie_1_tenis")
def ruta_functie_1_tenis():
    """Ruta 3: afiseaza informatiile din functia 1."""

    continut = f"""
    <div class="hero">

        <span class="badge">
            Informații generale
        </span>

        <h1>
            Despre tenisul de câmp
        </h1>

        <p>
            Această secțiune prezintă informații generale
            despre tenisul de câmp și elementele sale principale.
        </p>

    </div>


    <div class="card section">

        {functie_1_tenis()}

    </div>


    <div class="card section">

        <h2>
            Rolul pregătirii
        </h2>

        <p>
            Pentru a performa în tenis,
            jucătorii trebuie să combine pregătirea fizică,
            tehnica și concentrarea mentală.
            Antrenamentele regulate contribuie la îmbunătățirea
            reflexelor și preciziei loviturilor.
        </p>

    </div>


    <a class="back" href="/sporturi/tenis">
        Înapoi la tenis
    </a>
    """

    return pagina("Informatii generale", continut)


@app.route("/sporturi/tenis/functie_2_tenis")
def ruta_functie_2_tenis():
    """Ruta 4: afiseaza informatiile din functia 2."""

    continut = f"""
    <div class="hero">

        <span class="badge">
            Tehnici de joc
        </span>

        <h1>
            Tehnici importante în tenis
        </h1>

        <p>
            Tehnica influențează foarte mult performanța unui jucător.
            Loviturile corecte oferă control,
            precizie și stabilitate în timpul jocului.
        </p>

    </div>


    <div class="card section">

        {functie_2_tenis()}

    </div>


    <div class="grid">

        <div class="card">

            <h2>
                Serviciul
            </h2>

            <p>
                Serviciul reprezintă începutul fiecărui punct
                și poate oferi avantaj imediat jucătorului.
            </p>

        </div>


        <div class="card">

            <h2>
                Forehand
            </h2>

            <p>
                Forehand-ul este una dintre cele mai utilizate
                lovituri și permite control și forță.
            </p>

        </div>


        <div class="card">

            <h2>
                Backhand
            </h2>

            <p>
                Backhand-ul este important pentru apărare
                și pentru schimburile rapide de mingi.
            </p>

        </div>

    </div>


    <a class="back" href="/sporturi/tenis">
        Înapoi la tenis
    </a>
    """

    return pagina("Tehnici tenis", continut)


@app.route("/")
def index():
    """Redirect catre pagina principala a temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)