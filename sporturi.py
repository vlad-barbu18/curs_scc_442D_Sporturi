"""
Aplicatie Flask pentru tema sporturi.
Element ales: baschet.
"""

from flask import Flask, redirect

app = Flask(
    __name__,
    static_folder="app/static",
    static_url_path="/static",
)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e5e7eb;
                margin: 0;
                padding: 0;
            }}

            header {{
                background: #f97316;
                padding: 20px;
                text-align: center;
                color: white;
            }}

            nav {{
                background: #1e293b;
                padding: 15px;
                text-align: center;
            }}

            nav a {{
                color: #e5e7eb;
                margin: 0 15px;
                text-decoration: none;
                font-weight: bold;
            }}

            section {{
                padding: 40px;
                max-width: 900px;
                margin: auto;
            }}

            .card {{
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                margin-top: 20px;
            }}

            a.button {{
                background: #f97316;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin: 8px 8px 8px 0;
                font-weight: bold;
            }}

            img {{
                width: 100%;
                max-width: 500px;
                border-radius: 12px;
                margin: 12px 0 25px 0;
                display: block;
            }}

            li {{
                margin-bottom: 10px;
            }}
        </style>
    </head>

    <body>
        <header>
            <h1>{titlu}</h1>
            <p>Aplicatie web despre baschet</p>
        </header>

        <nav>
            <a href="/sporturi">Acasa</a>
            <a href="/sporturi/baschet">Baschet</a>
            <a href="/sporturi/baschet/functie_1_sport">Competitii</a>
            <a href="/sporturi/baschet/functie_2_sport">Echipamente</a>
        </nav>

        <section>
            {continut}
        </section>
    </body>
    </html>
    """


@app.route("/")
def index():
    """Redirect spre pagina principala."""
    return redirect("/sporturi")


@app.route("/sporturi")
def sporturi():
    """Ruta 1: pagina temei."""
    continut = """
    <div class="card">
        <h2>Tema proiectului: Sporturi</h2>
        <p>
            Aceasta aplicatie prezinta informatii despre un sport ales.
            Pentru proiect, sportul ales este baschetul.
        </p>
    </div>

    <div class="card">
        <h2>Element ales: Baschet</h2>
        <p>
            Baschetul este un sport de echipa in care doua formatii incearca
            sa inscrie puncte prin aruncarea mingii in cosul advers.
        </p>

        <a class="button" href="/sporturi/baschet">Mergi la Baschet</a>
    </div>
    """

    return pagina("Sporturi", continut)


@app.route("/sporturi/baschet")
def baschet():
    """Ruta 2: pagina elementului ales."""
    continut = """
    <div class="card">
        <h2>Baschet</h2>
        <p>
            Baschetul este un sport popular, practicat atat la nivel amator,
            cat si la nivel profesionist. Jocul pune accent pe coordonare,
            viteza, precizie si lucru in echipa.
        </p>
    </div>

    <div class="card">
        <h2>Informatii disponibile</h2>
        <p>Alege una dintre cele doua categorii:</p>

        <a class="button" href="/sporturi/baschet/functie_1_sport">
            Competitii de baschet
        </a>

        <a class="button" href="/sporturi/baschet/functie_2_sport">
            Echipamente de baschet
        </a>

        <a class="button" href="/sporturi">
            Inapoi la Sporturi
        </a>
    </div>
    """

    return pagina("Baschet", continut)


@app.route("/sporturi/baschet/functie_1_sport")
def ruta_functie_1_sport():
    """Ruta 3: pagina cu competitii de baschet."""
    continut = """
    <div class="card">
        <h2>Competitii importante de baschet</h2>

        <h3>NBA</h3>
        <p>
            NBA este cea mai cunoscuta competitie de baschet din lume,
            desfasurata in Statele Unite ale Americii.
        </p>
        <img src="/static/pictures/nba.jpg" alt="NBA">

        <h3>EuroLeague</h3>
        <p>
            EuroLeague este una dintre cele mai importante competitii
            de baschet din Europa, la nivel de cluburi.
        </p>

        <h3>Campionatul Mondial FIBA</h3>
        <p>
            Campionatul Mondial FIBA este o competitie internationala
            organizata intre echipele nationale de baschet.
        </p>
        <img src="/static/pictures/poza2.jpeg" alt="Campionatul Mondial FIBA">

        <h3>Jocurile Olimpice</h3>
        <p>
            Baschetul este inclus ca sport olimpic, fiind disputat intre
            echipe nationale.
        </p>

        <a class="button" href="/sporturi/baschet">
            Inapoi la Baschet
        </a>
    </div>
    """

    return pagina("Competitii de baschet", continut)


@app.route("/sporturi/baschet/functie_2_sport")
def ruta_functie_2_sport():
    """Ruta 4: pagina cu echipamente de baschet."""
    continut = """
    <div class="card">
        <h2>Echipamente folosite in baschet</h2>

        <img src="/static/pictures/poza1.jpeg" alt="Echipament de baschet">

        <ul>
            <li>
                <b>Minge de baschet:</b>
                Este elementul principal al jocului si este folosita pentru pase,
                dribling si aruncari la cos.
            </li>

            <li>
                <b>Cos de baschet:</b>
                Este format din panou, inel si plasa, iar scopul jocului este
                introducerea mingii in cos.
            </li>

            <li>
                <b>Echipament sportiv:</b>
                Jucatorii poarta tricou, sort si incaltaminte speciala pentru baschet.
            </li>

            <li>
                <b>Pantofi de baschet:</b>
                Sunt proiectati pentru aderenta, stabilitate si protectia gleznelor
                in timpul jocului.
            </li>

            <li>
                <b>Tabela de scor:</b>
                Este folosita pentru afisarea punctajului, timpului ramas si a altor
                informatii despre meci.
            </li>
        </ul>

        <a class="button" href="/sporturi/baschet">
            Inapoi la Baschet
        </a>
    </div>
    """

    return pagina("Echipamente de baschet", continut)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5030)
