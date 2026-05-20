"""
Aplicatie Flask pentru proiectul SCC.
Tema: sporturi
Element ales: ski

Pagina /sporturi ramane pagina generala a proiectului de grupa.
Sectiunea personala pentru ski incepe de la /sporturi/ski.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    program_partie_ski,
    tarife_skipass_ski,
    tabel_inchirieri_ski,
    reguli_partie_ski,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str, mod_ski: bool = False) -> str:
    """Creeaza o pagina HTML cu stil comun."""
    fundal = "linear-gradient(135deg, #f8fafc 0%, #e0f2fe 50%, #dbeafe 100%)"

    nav_links = """
        <a href="/sporturi">Sporturi</a>
        <a href="/sporturi/ski">Ski</a>
    """

    if mod_ski:
        fundal = """
            linear-gradient(rgba(4, 16, 35, 0.68), rgba(4, 16, 35, 0.82)),
            url('https://images.unsplash.com/photo-1551698618-1dfe5d97d256?auto=format&fit=crop&w=1600&q=80')
        """

        nav_links = """
            <a href="/sporturi">Sporturi</a>
            <a href="/sporturi/ski">Ski</a>
            <a href="/sporturi/ski/functie_1_ski">Program</a>
            <a href="/sporturi/ski/functie_2_ski">Skipass</a>
            <a href="/sporturi/ski/inchirieri">Inchirieri</a>
            <a href="/sporturi/ski/contact">Contact</a>
        """

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
                min-height: 100vh;
                font-family: Arial, sans-serif;
                background: {fundal};
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                background-repeat: no-repeat;
                color: #0f172a;
            }}

            .navbar {{
                background: rgba(15, 23, 42, 0.94);
                padding: 16px 42px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 6px 24px rgba(0, 0, 0, 0.24);
                position: sticky;
                top: 0;
                z-index: 10;
            }}

            .logo {{
                color: white;
                font-size: 21px;
                font-weight: bold;
                letter-spacing: 0.5px;
            }}

            .nav-links a {{
                color: #dbeafe;
                text-decoration: none;
                margin-left: 18px;
                font-size: 14px;
                font-weight: bold;
            }}

            .nav-links a:hover {{
                color: #38bdf8;
            }}

            .page {{
                max-width: 1100px;
                margin: 40px auto;
                padding: 0 20px 45px;
            }}

            .hero {{
                background: rgba(255, 255, 255, 0.94);
                border-radius: 26px;
                padding: 45px;
                box-shadow: 0 22px 55px rgba(0, 0, 0, 0.22);
                border: 1px solid rgba(226, 232, 240, 0.8);
            }}

            .ski-hero {{
                background:
                    linear-gradient(rgba(255, 255, 255, 0.93), rgba(240, 249, 255, 0.96));
                position: relative;
                overflow: hidden;
            }}

            .ski-hero::after {{
                content: "";
                position: absolute;
                right: -90px;
                bottom: -100px;
                width: 280px;
                height: 280px;
                background: rgba(56, 189, 248, 0.18);
                border-radius: 50%;
            }}

            .badge {{
                display: inline-block;
                background: #dbeafe;
                color: #1d4ed8;
                padding: 8px 14px;
                border-radius: 999px;
                font-size: 14px;
                font-weight: bold;
                margin-bottom: 12px;
            }}

            h1 {{
                font-size: 42px;
                margin: 8px 0 14px;
                color: #0f172a;
            }}

            h2 {{
                color: #0369a1;
                margin-top: 0;
            }}

            h3 {{
                color: #0f172a;
            }}

            p {{
                font-size: 18px;
                line-height: 1.7;
                color: #334155;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
                gap: 18px;
                margin-top: 24px;
            }}

            .card {{
                background: rgba(255, 255, 255, 0.96);
                border-radius: 18px;
                padding: 24px;
                box-shadow: 0 12px 30px rgba(15, 23, 42, 0.15);
                border: 1px solid rgba(148, 163, 184, 0.25);
            }}

            .card h3 {{
                margin-top: 0;
            }}

            .card p {{
                font-size: 16px;
                margin-bottom: 0;
            }}

            .btn {{
                display: inline-block;
                background: #0284c7;
                color: white;
                padding: 12px 18px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                margin: 8px 8px 0 0;
                transition: 0.2s;
            }}

            .btn:hover {{
                background: #0369a1;
                transform: translateY(-2px);
            }}

            .btn.secondary {{
                background: #334155;
            }}

            .btn.secondary:hover {{
                background: #1e293b;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                overflow: hidden;
                border-radius: 14px;
                background: white;
                margin-top: 18px;
            }}

            th {{
                background: #0f172a;
                color: white;
                text-align: left;
                padding: 14px;
            }}

            td {{
                padding: 14px;
                border-bottom: 1px solid #e2e8f0;
                color: #334155;
            }}

            tr:last-child td {{
                border-bottom: none;
            }}

            .price {{
                font-weight: bold;
                color: #0284c7;
            }}

            .notice {{
                background: #ecfeff;
                border-left: 5px solid #06b6d4;
                padding: 16px;
                border-radius: 12px;
                margin-top: 20px;
                color: #155e75;
            }}

            ul {{
                line-height: 1.8;
                color: #334155;
                font-size: 17px;
            }}

            @media (max-width: 760px) {{
                .navbar {{
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 12px;
                    padding: 16px 24px;
                }}

                .nav-links a {{
                    margin-left: 0;
                    margin-right: 12px;
                    display: inline-block;
                    margin-bottom: 8px;
                }}

                h1 {{
                    font-size: 32px;
                }}

                .hero {{
                    padding: 28px;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="navbar">
            <div class="logo">Sporturi SCC</div>
            <div class="nav-links">
                {nav_links}
            </div>
        </div>

        <main class="page">
            {continut}
        </main>
    </body>
    </html>
    """


@app.route("/")
def index():
    """Redirect spre pagina principala a temei."""
    return redirect("/sporturi")


@app.route("/sporturi")
def sporturi():
    """Pagina generala a temei sporturi."""
    continut = """
    <section class="hero">
        <span class="badge">Proiect de grupa</span>
        <h1>Sporturi</h1>

        <p>
            Aceasta pagina reprezinta sectiunea generala a proiectului de grupa.
            Fiecare student poate adauga aici un sport diferit, cu o ruta proprie.
        </p>

        <p>
            Pentru componenta mea, sportul ales este ski-ul, prezentat sub forma
            unui site informativ despre o partie de ski.
        </p>

        <a class="btn" href="/sporturi/ski">Deschide pagina Ski</a>
    </section>

    <section class="grid">
        <div class="card">
            <h3>Ski</h3>
            <p>Pagina dedicata unei partii de ski, cu program, skipass si inchirieri.</p>
            <a class="btn" href="/sporturi/ski">Vezi sportul</a>
        </div>

        <div class="card">
            <h3>Alte sporturi</h3>
            <p>
                Aceasta zona poate fi completata ulterior cu paginile colegilor
                din proiectul de grupa.
            </p>
        </div>
    </section>
    """

    return pagina("Sporturi", continut, mod_ski=False)


@app.route("/sporturi/ski")
def ski():
    """Pagina principala pentru sportul ales: ski."""
    continut = """
    <section class="hero ski-hero">
        <span class="badge">Sport ales: Ski</span>
        <h1>Partia Alpine Ski</h1>

        <p>
            Partia Alpine Ski este o pagina demonstrativa pentru un centru de ski.
            Vizitatorii pot consulta programul, starea partiei, tarifele pentru
            skipass, urcarile individuale si preturile pentru inchirierea echipamentului.
        </p>

        <a class="btn" href="/sporturi/ski/functie_1_ski">Program si stare partie</a>
        <a class="btn" href="/sporturi/ski/functie_2_ski">Skipass si urcari</a>
        <a class="btn" href="/sporturi/ski/inchirieri">Inchirieri echipament</a>
        <a class="btn secondary" href="/sporturi">Inapoi la Sporturi</a>
    </section>

    <section class="grid">
        <div class="card">
            <h3>Lungime partie</h3>
            <p>1.8 km de traseu amenajat, potrivit pentru nivel incepator si mediu.</p>
        </div>

        <div class="card">
            <h3>Diferenta de nivel</h3>
            <p>Aproximativ 420 m, cu zone de coborare si viraje largi.</p>
        </div>

        <div class="card">
            <h3>Nocturna</h3>
            <p>Disponibila in weekend, in functie de vreme si stratul de zapada.</p>
        </div>
    </section>
    """

    return pagina("Partia Alpine Ski", continut, mod_ski=True)


@app.route("/sporturi/ski/functie_1_ski")
def ruta_program_ski():
    """Ruta 3: afiseaza programul si starea partiei."""
    continut = f"""
    <section class="hero ski-hero">
        <span class="badge">Program</span>
        <h1>Program si stare partie</h1>

        {program_partie_ski()}

        <div class="notice">
            Programul poate fi modificat in functie de vreme, stratul de zapada
            si reviziile instalatiilor de transport.
        </div>

        <a class="btn" href="/sporturi/ski">Inapoi la pagina Ski</a>
    </section>
    """

    return pagina("Program partie", continut, mod_ski=True)


@app.route("/sporturi/ski/functie_2_ski")
def ruta_skipass_ski():
    """Ruta 4: afiseaza tarife pentru skipass si urcari individuale."""
    continut = f"""
    <section class="hero ski-hero">
        <span class="badge">Tarife</span>
        <h1>Skipass si urcari individuale</h1>

        {tarife_skipass_ski()}

        <div class="notice">
            Preturile sunt orientative si au rol demonstrativ pentru proiect.
        </div>

        <a class="btn" href="/sporturi/ski/inchirieri">Vezi inchirieri</a>
        <a class="btn secondary" href="/sporturi/ski">Inapoi la pagina Ski</a>
    </section>
    """

    return pagina("Skipass si urcari", continut, mod_ski=True)


@app.route("/sporturi/ski/inchirieri")
def inchirieri():
    """Pagina cu preturi pentru inchirierea echipamentului."""
    continut = f"""
    <section class="hero ski-hero">
        <span class="badge">Echipament</span>
        <h1>Inchirieri echipament ski</h1>

        <p>
            Centrul de inchirieri pune la dispozitie echipamente pentru adulti
            si copii, potrivite pentru diferite niveluri de experienta.
        </p>

        {tabel_inchirieri_ski()}

        <a class="btn" href="/sporturi/ski/functie_2_ski">Vezi skipass</a>
        <a class="btn secondary" href="/sporturi/ski">Inapoi la pagina Ski</a>
    </section>
    """

    return pagina("Inchirieri ski", continut, mod_ski=True)


@app.route("/sporturi/ski/contact")
def contact():
    """Pagina cu reguli si informatii de contact."""
    continut = f"""
    <section class="hero ski-hero">
        <span class="badge">Informatii utile</span>
        <h1>Reguli si contact</h1>

        {reguli_partie_ski()}

        <div class="card">
            <h3>Contact partie</h3>
            <p><b>Telefon:</b> 0722 000 000</p>
            <p><b>Email:</b> contact@alpineski.ro</p>
            <p><b>Locatie:</b> Zona montana Alpine, Romania</p>
        </div>

        <a class="btn secondary" href="/sporturi/ski">Inapoi la pagina Ski</a>
    </section>
    """

    return pagina("Contact partie", continut, mod_ski=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)