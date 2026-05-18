from flask import Flask
from app.lib.biblioteca_sporturi import reguli_golf, echipament_golf, teren_golf

app = Flask(__name__)


@app.route("/")
def index():
    return "Proiect SCC - Sporturi"


@app.route("/golf")
def golf():
    return """
    <h1>Golf</h1>
    <p>Pagina pentru sportul Golf.</p>

    <img src="/static/images/golf.jpg" width="400">

    <br><br>

    <a href="/golf/reguli">Reguli</a> |
    <a href="/golf/echipament">Echipament</a> |
    <a href="/golf/teren">Teren</a>
    """

@app.route("/golf/reguli")
def golf_reguli():
    return reguli_golf()


@app.route("/golf/echipament")
def golf_echipament():
    return echipament_golf()


@app.route("/golf/teren")
def golf_teren():
    return teren_golf()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
