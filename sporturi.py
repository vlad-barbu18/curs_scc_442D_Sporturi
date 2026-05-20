"""Aplicatie Flask pentru prezentarea sportului Volei."""
from flask import Flask, render_template

from app.lib.biblioteca_sporturi import echipament_volei, reguli_volei

app = Flask(__name__)

@app.route("/")
@app.route("/sporturi")
def sporturi():
    """Afiseaza pagina principala pentru sporturi."""
    return render_template("index.html")

@app.route("/sporturi/volei")
def volei():
    """Afiseaza pagina sportului Volei."""
    return render_template("volei.html")

@app.route("/sporturi/volei/reguli")
def reguli():
    """Afiseaza pagina cu regulile jocului de volei."""
    return render_template("reguli.html", reguli_html=reguli_volei())

@app.route("/sporturi/volei/echipament")
def echipament():
    """Afiseaza pagina cu echipamentele folosite in volei."""
    return render_template("echipament.html", echipament_html=echipament_volei())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
