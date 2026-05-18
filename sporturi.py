"""
Aplicatie Flask pentru tema Sporturi.
Element ales: tenis de masa (ping-pong).
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    reguli_tenis_de_masa,
    campioni_tenis_de_masa,
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
    """Pagina temei."""
    return pagina("Sporturi",
        """<h1>Sporturi</h1>
        <p>Tema proiectului este Sporturi. Elementul ales este tenis de masa (ping-pong).</p>
        <a href="/sporturi/tenis_de_masa">Tenis de masa</a>""")


@app.route("/sporturi/tenis_de_masa")
def tenis_de_masa():
    """Pagina elementului ales."""
    return pagina("Tenis de masa",
        """<h1>Tenis de masa (Ping-Pong)</h1>
        <p>Tenis de masa este un sport olimpic practicat de milioane de oameni in intreaga lume.</p>
        <a href="/sporturi/tenis_de_masa/reguli_tenis_de_masa">Reguli</a>
        <a href="/sporturi/tenis_de_masa/campioni_tenis_de_masa">Campioni</a>
        <a href="/sporturi">Inapoi la Sporturi</a>""")


@app.route("/sporturi/tenis_de_masa/reguli_tenis_de_masa")
def ruta_reguli_tenis_de_masa():
    """Ruta 3: afiseaza regulile tenisului de masa."""
    continut = "<h1>Regulile tenisului de masa</h1>"
    continut += reguli_tenis_de_masa()
    continut += '<a href="/sporturi/tenis_de_masa">Inapoi</a>'
    return pagina("Reguli tenis de masa", continut)


@app.route("/sporturi/tenis_de_masa/campioni_tenis_de_masa")
def ruta_campioni_tenis_de_masa():
    """Ruta 4: afiseaza campionii la tenis de masa."""
    continut = "<h1>Campioni la tenis de masa</h1>"
    continut += campioni_tenis_de_masa()
    continut += '<a href="/sporturi/tenis_de_masa">Inapoi</a>'
    return pagina("Campioni tenis de masa", continut)


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
