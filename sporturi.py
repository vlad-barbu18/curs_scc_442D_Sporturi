"""
Aplicatie Flask pentru sporturi.
Element ales: sah.
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
def sporturi():
    """Pagina sporturi."""
    return pagina("sporturi",
        """<h1>sporturi</h1>
        <p>Proiectul este despre sporturi. Elementul ales este sport.</p>
        <a href="/sporturi/sport">Sport</a>""")


@app.route("/sporturi/sah")
def sport():
    """Pagina elementului ales."""
    return pagina("Sport",
        """<h1>Sport</h1>
        <p>Descriere generala.</p>
        <a href="/sporturi">Inapoi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina sporturi."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
