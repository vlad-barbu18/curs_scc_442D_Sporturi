from flask import Flask

from app.lib.biblioteca_sporturi import (
    discipline_echitatie,
    echipamente_echitatie
)

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Sporturi</h1>

    <ul>
        <li><a href="/echitatie">Echitatie</a></li>
        <li><a href="/echitatie/discipline">Discipline</a></li>
        <li><a href="/echitatie/echipamente">Echipamente</a></li>
    </ul>
    """


@app.route("/echitatie")
def echitatie():
    return "<h2>Echitatia este un sport ecvestru.</h2>"


@app.route("/echitatie/discipline")
def discipline():
    return discipline_echitatie()


@app.route("/echitatie/echipamente")
def echipamente():
    return echipamente_echitatie()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
