"""
Aplicatie Flask pentru proiectul SCC.
Tema: Sporturi
Element ales: Minifotbal
dezvoltator: Lazar Iulian
"""

from flask import Flask, redirect
# Importul aliniat perfect cu structura ta din folderul app
from app.lib.biblioteca_sporturi import (
    functie_1_sport,
    functie_2_sport,
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
                font-family: Arial, sans-serif;
                background: #f0f7f4;
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
                color: #15803d;
                border-bottom: 2px solid #bbf7d0;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #1d4ed8;
            }}
            p {{
                line-height: 1.6;
                color: #374151;
            }}
            ul {{
                line-height: 1.8;
                color: #374151;
            }}
            a {{
                background: #16a34a;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin: 5px;
                font-weight: bold;
            }}
            a:hover {{
                background: #15803d;
            }}
            .btn-back {{
                background: #4b5563;
            }}
            .btn-back:hover {{
                background: #374151;
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
            aplicatii web am ales sa prezint <strong>minifotbalul</strong>, o activitate 
            dinamica derivata din fotbalul clasic, care promoveaza spiritul de echipa, 
            conditia fizica si fair-play-ul.
        </p>
        <p>
            Aplicatia este realizata folosind Flask si contine pagini separate
            pentru tema principala, elementul ales (Minifotbal) si doua categorii de informatii.
        </p>
        <a href="/sporturi/minifotbal">Minifotbal</a>
        """,
    )


@app.route("/sporturi/minifotbal")
def minifotbal():
    """Pagina elementului ales: Minifotbal."""
    return pagina(
        "Minifotbal",
        """
        <h1>Minifotbal</h1>
        <p>
            Minifotbalul este o varianta populara a fotbalului clasic, jucata de obicei pe teren 
            redus (adesea sintetic) si cu porti mai mici. Este un sport accesibil tuturor varstelor, 
            caracterizat prin faze rapide de joc, intensitate ridicata si un numar mai mic de jucatori.
        </p>
        <p>
            In acest proiect sunt prezentate doua aspecte importante despre acest sport: 
            regulile de baza si echipamentul necesar pentru desfasurarea unui meci in siguranta.
        </p>
        
        <a href="/sporturi/minifotbal/functie_1_sport">Informatia 1</a>
        <a href="/sporturi/minifotbal/functie_2_sport">Informatia 2</a>
        <br><br>
        <a href="/sporturi" class="btn-back">Inapoi la Sporturi</a>
        """,
    )


@app.route("/sporturi/minifotbal/functie_1_sport")
def ruta_functie_1_sport():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Informatia 1 despre sport</h1>"
    continut += functie_1_sport()
    continut += '<br><br><a href="/sporturi/minifotbal" class="btn-back">Inapoi</a>'
    return pagina("Informatia 1", continut)


@app.route("/sporturi/minifotbal/functie_2_sport")
def ruta_functie_2_sport():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Informatia 2 despre sport</h1>"
    continut += functie_2_sport()
    continut += '<br><br><a href="/sporturi/minifotbal" class="btn-back">Inapoi</a>'
    return pagina("Informatia 2", continut)


@app.route("/")
def index():
    """Redirect catre pagina principala."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
