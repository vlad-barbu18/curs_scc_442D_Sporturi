"""
Aplicatie Flask pentru proiectul SCC.
Tema: Sporturi
Element ales: Minifotbal
Cel mai top dezvoltator: Lazar Iulian
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
        <a href="/sporturi/minifotbal/reguli">Reguli de joc</a>
        <a href="/sporturi/minifotbal/echipament">Echipament necesar</a>
        <br><br>
        <a href="/sporturi" class="btn-back">Inapoi la Sporturi</a>
        """,
    )


@app.route("/sporturi/minifotbal/reguli")
def reguli():
    """Prima categorie: Reguli de joc."""
    return pagina(
        "Reguli de joc - Minifotbal",
        """
        <h1>Reguli de Joc la Minifotbal</h1>
        <p>Minifotbalul se ghideaza dupa un set de reguli menite sa pastreze jocul rapid si dinamic:</p>
        <ul>
            <li><strong>Numarul de jucatori:</strong> Se joaca de obicei in format de 5+1 (5 jucatori de camp si un portar).</li>
            <li><strong>Durata meciului:</strong> In mod oficial, o partida are doua reprize a cate 20 sau 25 de minute fiecare.</li>
            <li><strong>Dimensiunea terenului:</strong> Suprafata de joc este redusa, avand de obicei lungimi intre 36-46 metri si latimi intre 18-26 metri.</li>
            <li><strong>Fara ofsaid:</strong> In minifotbal nu se aplica regula ofsaidului, ceea ce face jocul mult mai spectaculos si plin de goluri.</li>
            <li><strong>Schimbari nelimitate:</strong> Inlocuirile de jucatori se pot face in mod repetat si in orice moment al meciului.</li>
        </ul>
        <br>
        <a href="/sporturi/minifotbal" class="btn-back">Inapoi la Minifotbal</a>
        """,
    )


@app.route("/sporturi/minifotbal/echipament")
def echipament():
    """A doua categorie: Echipament."""
    return pagina(
        "Echipament - Minifotbal",
        """
        <h1>Echipament de Minifotbal</h1>
        <p>Pentru a practica minifotbalul in conditii optime si de siguranta, un jucator are nevoie de:</p>
        <ul>
            <li><strong>Incaltaminte adecvata:</strong> Ghete de tip TF (turf) cu crampoane mici de cauciuc, ideale pentru terenul sintetic, sau AG (artificial grass).</li>
            <li><strong>Echipamentul echipei:</strong> Tricou din material respirabil, sort si jambiere.</li>
            <li><strong>Protectie:</strong> Aparatorile de tibie sunt puternic recomandate sau chiar obligatorii in competitii pentru a preveni accidentarile.</li>
            <li><strong>Echipamentul portarului:</strong> Manusi speciale de portar si bluza cu protectii la coate.</li>
            <li><strong>Mingea de joc:</strong> O minge marimea 4 sau 5, adaptata desfasurarii jocului pe suprafete reduse.</li>
        </ul>
        <br>
        <a href="/sporturi/minifotbal" class="btn-back">Inapoi la Minifotbal</a>
        """,
    )


@app.route("/")
def index():
    """Redirect catre pagina principala."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
