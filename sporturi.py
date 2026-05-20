"""
Aplicatie Flask pentru tema Sporturi.
Dezvoltator: Mitu Marian
Element ales: MMA.
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
        <a href="/sporturi">Inapoi la Sporturi</a>
    """
    return pagina("MMA", continut)


@app.route("/")
def index():
    """Redirect spre pagina principala a temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
