from flask import Flask

from app.lib.biblioteca_sporturi import (
    discipline_echitatie,
    echipamente_echitatie
)

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <html>
    <head>
        <title>Sporturi - Echitatie</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f7efe5;
                color: #3b2f2f;
                text-align: center;
                padding: 40px;
            }

            .card {
                background: white;
                border-radius: 20px;
                padding: 30px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }

            h1 {
                color: #8b5e3c;
            }

            a {
                display: block;
                margin: 15px auto;
                padding: 12px;
                width: 260px;
                text-decoration: none;
                background: #c89f7a;
                color: white;
                border-radius: 12px;
                font-weight: bold;
            }

            a:hover {
                background: #8b5e3c;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Sporturi - Echitatie 🐎</h1>
            
            <a href="/echitatie">Despre echitatie</a>
            <a href="/echitatie/discipline">Discipline</a>
            <a href="/echitatie/echipamente">Echipamente</a>
        </div>
    </body>
    </html>
    """

@app.route("/echitatie")
def echitatie():
    return """
    <html>
    <head>
        <title>Despre Echitatie</title>

        <style>

           a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 18px;
            background: #c89f7a;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
           }

           a:hover {
             background: #8b5e3c;
           }


            body {
                font-family: Arial, sans-serif;
                background: #f7efe5;
                color: #3b2f2f;
                padding: 40px;
                text-align: center;
            }

            .container {
                background: white;
                max-width: 550px;
                margin: auto;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }

            img {
                max-width: 300px;
                object-fit: cover;
                width: 100%;
                border-radius: 15px;
                margin-bottom: 20px;
            }

            h1 {
                color: #8b5e3c;
            }

            p {
                line-height: 1.7;
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Despre Echitatie 🐎</h1>

            <img src="/static/imagini/cal.png" alt="Echitatie">

            <p>
            Echitatia este denumirea generala pentru sporturile
            care implica mersul calare.
            </p>

            <p>
            Acest sport necesita echilibru, coordonare,
            incredere si o buna relatie intre cal si calaret.
            </p>

        </div>
    </body>
    </html>
    <a href="/">Inapoi la Home</a>
    """



@app.route("/echitatie/discipline")
def discipline():
    return discipline_echitatie()


@app.route("/echitatie/echipamente")
def echipamente():
    return echipamente_echitatie()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

