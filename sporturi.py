from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/sporturi")
def sporturi():
    return render_template("index.html")

@app.route("/sporturi/volei")
def volei():
    return render_template("volei.html")

@app.route("/sporturi/volei/reguli")
def reguli():
    return render_template("reguli.html")

@app.route("/sporturi/volei/echipament")
def echipament():
    return render_template("echipament.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
