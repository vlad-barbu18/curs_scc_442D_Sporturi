"""
Aplicatie Flask pentru tema Sporturi.
Element ales: tir cu arcul.
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    reguli_tir_cu_arcul,
    campioni_tir_cu_arcul,
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
        <p>Tema proiectului este Sporturi. Elementul ales este tir cu arcul.</p>
        <a href="/sporturi/tir_cu_arcul">Tir cu arcul</a>""")


@app.route("/sporturi/tir_cu_arcul")
def tir_cu_arcul():
    """Pagina elementului ales."""
    return pagina("Tir cu arcul",
        """<h1>Tir cu arcul</h1>
        <p>Tirul cu arcul este un sport olimpic cu o traditie de mii de ani, practicat in intreaga lume.</p>
        <a href="/sporturi/tir_cu_arcul/reguli_tir_cu_arcul">Reguli</a>
        <a href="/sporturi/tir_cu_arcul/campioni_tir_cu_arcul">Campioni</a>
        <a href="/sporturi">Inapoi la Sporturi</a>""")


@app.route("/sporturi/tir_cu_arcul/reguli_tir_cu_arcul")
def ruta_reguli_tir_cu_arcul():
    """Ruta 3: afiseaza regulile tirului cu arcul."""
    continut = "<h1>Regulile tirului cu arcul</h1>"
    continut += reguli_tir_cu_arcul()
    continut += '<a href="/sporturi/tir_cu_arcul">Inapoi</a>'
    return pagina("Reguli tir cu arcul", continut)


@app.route("/sporturi/tir_cu_arcul/campioni_tir_cu_arcul")
def ruta_campioni_tir_cu_arcul():
    """Ruta 4: afiseaza campionii la tir cu arcul."""
    continut = "<h1>Campioni la tir cu arcul</h1>"
    continut += campioni_tir_cu_arcul()
    continut += '<a href="/sporturi/tir_cu_arcul">Inapoi</a>'
    return pagina("Campioni tir cu arcul", continut)


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
