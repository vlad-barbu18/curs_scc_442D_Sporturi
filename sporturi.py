"""
Aplicatie Flask pentru tema sporturi.
Element ales: scrima.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_scrima,
    functie_2_scrima,
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
def tema():
    """Pagina temei."""
    return pagina("Sporturi",
        """<h1>Sporturi</h1>
        <p>Tema proiectului este Sporturi. Elementul ales este scrima.</p>
        <a href="/sporturi/scrima">Scrima</a>""")


@app.route("/sporturi/scrima")
def sport():
    """Pagina elementului ales."""
    return pagina("Scrima",
        """<h1>Scrima</h1>
        <p>Scrima este un sport de luptă practicat cu arme albe convenționale.</p>
        
	<a href="/sporturi/scrima/functie_1_scrima">Informatia 1</a>
	<a href="/sporturi/scrima/functie_2_scrima">Informatia 2</a>
	<a href="/sporturi">Inapoi la Sporturi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


@app.route("/sporturi/scrima/functie_1_scrima")
def ruta_functie_1_scrima():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Informatii generale despre scrima</h1>"
    continut += functie_1_scrima()
    continut += '<a href="/sporturi/scrima">Inapoi</a>'
    return pagina("Informatia 1", continut)


@app.route("/sporturi/scrima/functie_2_scrima")
def ruta_functie_2_scrima():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Tipuri de arme in scrima</h1>"
    continut += functie_2_scrima()
    continut += '<a href="/sporturi/scrima">Inapoi</a>'
    return pagina("Informatia 2", continut)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
