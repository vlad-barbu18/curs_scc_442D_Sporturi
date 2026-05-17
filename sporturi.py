from flask import Flask
from app.lib.biblioteca_sporturi import reguli_golf, echipament_golf, teren_golf

app = Flask(__name__)


@app.route("/")
def index():
    return "Proiect SCC - Sporturi"


@app.route("/golf")
def golf():
    return "Pagina pentru sportul Golf."


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
