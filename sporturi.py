"""
Aplicatie Flask pentru tema Sporturi - Echitatie.
"""

from flask import Flask

from app.lib.biblioteca_sporturi import (
    discipline_echitatie,
    echipamente_echitatie,
    pagina_html,
)

app = Flask(__name__)


@app.route("/")
def index():
    """
    Afiseaza pagina principala a aplicatiei.
    """

    continut = """
    <h1>Sporturi - Echitatie 🐎</h1>

    <p>
    Bine ai venit in aplicatia despre echitatie.
    Alege una dintre sectiunile de mai jos.
    </p>

    <a href="/echitatie">Despre echitatie</a>
    <a href="/echitatie/discipline">Discipline</a>
    <a href="/echitatie/echipamente">Echipamente</a>
    """

    return pagina_html("Sporturi - Echitatie", continut, False)


@app.route("/echitatie")
def echitatie():
    """
    Afiseaza informatii generale despre echitatie.
    """

    continut = """
    <h1>Despre Echitatie 🐎</h1>

    <img src="/static/imagini/cal.png" alt="Cal">

    <p>
    Echitatia este denumirea generala pentru sporturile care implica
    mersul calare.
    </p>

    <p>
    Exista mai multe discipline ecvestre, precum sariturile peste
    obstacole, dresajul, cursele de cai sau polo.
    </p>

    <p>
    Acest sport necesita echilibru, coordonare, incredere si o buna
    relatie intre cal si calaret.
    </p>
    """

    return pagina_html("Despre Echitatie", continut)


@app.route("/echitatie/discipline")
def discipline():
    """
    Afiseaza disciplinele din echitatie.
    """

    return discipline_echitatie()


@app.route("/echitatie/echipamente")
def echipamente():
    """
    Afiseaza echipamentele folosite in echitatie.
    """

    return echipamente_echitatie()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
