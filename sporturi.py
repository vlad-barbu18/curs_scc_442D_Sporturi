from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_box,
    functie_2_box,
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
    return pagina("sporturi",
        """<h1>sporturi</h1>
        <p>Tema proiectului este sporturi. Elementul ales este box.</p>
        <a href="/sporturi/box">box</a>""")


@app.route("/sporturi/box")
def sport():
    """Pagina elementului ales."""
    return pagina("Sport",
        """<h1>box</h1>
        <p>Descriere generala.</p>
        <a href="/sporturi/box/functie_1_box">Informatia 1</a>
        <a href="/sporturi/box/functie_2_box">Informatia 2</a>
        <a href="/sporturi">Inapoi la sporturi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")

@app.route("/sporturi/box/functie_1_box")
def ruta_functie_1_sport():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Informatia 1 despre box</h1>"
    continut += functie_1_box()
    continut += '<a href="/sporturi/box">Inapoi</a>'
    return pagina("Informatia 1", continut)


@app.route("/sporturi/box/functie_2_box")
def ruta_functie_2_sport():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Informatia 2 despre box</h1>"
    continut += functie_2_box()
    continut += '<a href="/sporturi/box">Inapoi</a>'
    return pagina("Informatia 2", continut)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)