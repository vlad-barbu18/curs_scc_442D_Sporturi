"""
Aplicatie Flask pentru tema Sporturi.
Dezvoltator: Mitu Marian
Element ales: MMA.
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    afiseaza_luptatori_mma,
    afiseaza_tehnici_mma,
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
              background: #eaf4ff;
              padding: 30px;
          }}
          .container {{
              background: white;
              max-width: 900px;
              margin: auto;
              padding: 30px;
              border-radius: 12px;
              box-shadow: 0 0 12px rgba(0, 0, 0, 0.12);
          }}
          h1 {{ color: #1d4ed8; }}
          h2 {{ color: #16a34a; }}
          p {{ line-height: 1.6; }}
          a {{
              background: #2563eb;
              color: white;
              padding: 10px 15px;
              text-decoration: none;
              border-radius: 8px;
              display: inline-block;
              margin: 5px;
          }}
          a:hover {{ background: #1e40af; }}
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
    """Pagina principala a temei."""
    continut = """
        <h1>Sporturi</h1>
        <p>
            Tema proiectului este <b>sporturi</b>, iar elementul ales
            pentru implementare este <b>MMA</b>.
        </p>
        <p>
            MMA inseamna Mixed Martial Arts si combina tehnici din box,
            kickboxing, wrestling, judo, jiu-jitsu brazilian si alte discipline.
        </p>
        <a href="/sporturi/mma">Vezi pagina MMA</a>
    """
    return pagina("Sporturi", continut)


@app.route("/sporturi/mma")
def mma():
    """Pagina elementului ales."""
    continut = """
        <h1>MMA</h1>
        <p>
            MMA este un sport de contact in care sportivii folosesc tehnici
            de lupta in picioare si la sol.
        </p>
        <h2>De ce am ales MMA?</h2>
        <p>
            Am ales MMA deoarece este un sport complex, modern si spectaculos,
            care necesita disciplina, pregatire fizica si strategie.
        </p>
        <a href="/sporturi/mma/afiseaza_luptatori_mma">Luptatori MMA</a>
        <a href="/sporturi/mma/afiseaza_tehnici_mma">Tehnici MMA</a>
        <a href="/sporturi">Inapoi la sporturi</a>
    """
    return pagina("MMA", continut)


@app.route("/sporturi/mma/afiseaza_luptatori_mma")
def ruta_luptatori_mma():
    """Ruta pentru prima functie din biblioteca: luptatori MMA."""
    continut = """
        <h1>Luptatori MMA</h1>
        <p>
            Aceasta pagina afiseaza cativa luptatori cunoscuti din MMA.
        </p>
    """

    continut += afiseaza_luptatori_mma()
    continut += """
        <br>
        <a href="/sporturi/mma">Inapoi la MMA</a>
        <a href="/sporturi">Inapoi la sporturi</a>
    """

    return pagina("Luptatori MMA", continut)


@app.route("/sporturi/mma/afiseaza_tehnici_mma")
def ruta_tehnici_mma():
    """Ruta pentru a doua functie din biblioteca: tehnici MMA."""
    continut = """
        <h1>Tehnici MMA</h1>
        <p>
            Aceasta pagina prezinta cateva tehnici importante folosite in MMA.
        </p>
    """

    continut += afiseaza_tehnici_mma()
    continut += """
        <br>
        <a href="/sporturi/mma">Inapoi la MMA</a>
        <a href="/sporturi">Inapoi la sporturi</a>
    """

    return pagina("Tehnici MMA", continut)


@app.route("/")
def index():
    """Redirect spre pagina principala a temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)