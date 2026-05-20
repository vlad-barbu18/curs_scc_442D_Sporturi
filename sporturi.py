"""
Aplicatie Flask pentru tema sporturi.
Element ales: Tenis de camp.
"""

from flask import Flask, redirect

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html><head><title>{titlu}</title>
    <style>
      body {{ font-family: Arial; background: #eaf4ff; padding: 30px; }}
      .container {{ background: white; max-width: 900px; margin: auto;
                   padding: 30px; border-radius: 12px; }}
      h1 {{ color: #1d4ed8; }} h2 {{ color: #16a34a; }}
      a {{ background: #2563eb; color: white; padding: 10px 15px;
          text-decoration: none; border-radius: 8px; display: inline-block;
          margin: 5px; }}
    </style></head><body><div class="container">{continut}</div></body></html>
    """


@app.route("/sporturi")
def tema():
    """Pagina temei."""
    return pagina("Sporturi",
        """<h1>Sporturi</h1>
        <p>Tema proiectului este sporturi. Elementul ales este Tenis de camp.</p>
        <a href="/sporturi/tenis-de-camp">Tenis de camp</a>""")


@app.route("/sporturi/tenis-de-camp")
def sport():
    """Pagina elementului ales."""
    return pagina("Tenis de camp",
        """<h1>Tenis de camp</h1>
        <p>Tenisul de camp este un sport practicat individual sau in echipa, folosind rachete si o minge.</p>
        <a href="/sporturi">Inapoi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
