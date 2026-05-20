"""
Aplicatie Flask pentru sporturi.
Element ales: sah.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_sport,
    functie_2_sport,
)

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
        <p>Tema proiectului este sporturi. Sportul ales este sah.</p>
        <a href="/sporturi/sah">Sah</a>""")


@app.route("/sporturi/sah")
def sah():
    """Pagina elementului ales."""
    return pagina("Sah",
        """<h1>Sah</h1>
        <p>Descriere generala.</p>
        <a href="/sporturi/sah/functie_1_sport">Informatia 1</a>
        <a href="/sporturi/sah/functie_2_sport">Informatia 2</a>
        <a href="/sporturi">Inapoi la sporturi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina sporturi."""
    return redirect("/sporturi")


@app.route("/sporturi/sah/functie_1_sport")
def ruta_functie_1_sport():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Informatia 1 despre sah</h1>"
    continut += functie_1_sport()
    continut += '<a href="/sporturi/sah">Inapoi</a>'
    return pagina("Informatia 1", continut)


@app.route("/sporturi/sah/functie_2_sport")
def ruta_functie_2_sport():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Informatia 2 despre sah</h1>"
    continut += functie_2_sport()
    continut += '<a href="/sporturi/sah">Inapoi</a>'
    return pagina("Informatia 2", continut)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
