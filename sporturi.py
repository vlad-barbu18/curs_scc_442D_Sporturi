from flask import Flask

from app.lib.biblioteca_sporturi import (
    sarituri_patinaj_artistic,
    echipamente_patinaj_artistic,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    return f"""
    <html>
    <head>
        <title>{titlu}</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #eaf4ff;
                margin: 0;
                padding: 30px;
            }}

            .container {{
                background-color: white;
                max-width: 900px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
            }}

            h1 {{
                color: #1d4ed8;
            }}

            p {{
                font-size: 18px;
                line-height: 1.6;
            }}

            img {{
                width: 100%;
                border-radius: 10px;
                margin: 20px 0;
            }}

            a {{
                background-color: #2563eb;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin: 5px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            {continut}
        </div>
    </body>
    </html>
    """


@app.route("/")
def patinaj_artistic():
    return pagina(
        "Patinaj artistic",
        """
        <h1>⛸️ Patinaj artistic</h1>

        <img src="/static/images/poza_generala.jpeg">

        <p>
        Patinajul artistic este un sport de iarna practicat pe gheata,
        care combina tehnica, eleganta, muzica si expresivitatea artistica.
        </p>

        <p>
        Sportivii executa sarituri, piruete si pasi coregrafici
        sincronizati cu muzica. Acest sport necesita echilibru,
        forta, flexibilitate si foarte mult antrenament.
        </p>

        <p>
        Patinajul artistic poate fi practicat individual,
        in perechi sau in dans pe gheata.
        </p>

        <a href="/sarituri">Sarituri</a>
        <a href="/echipamente">Echipamente</a>
        """
    )


@app.route("/sarituri")
def sarituri():
    return pagina(
        "Sarituri",
        f"""
        <h1>✨ Sarituri in patinaj artistic</h1>

        <img src="/static/images/poza_sarituri.jpeg">

        {sarituri_patinaj_artistic()}

        <a href="/">Inapoi la Patinaj artistic</a>
        """
    )


@app.route("/echipamente")
def echipamente():
    return pagina(
        "Echipamente",
        f"""
        <h1>🎽 Echipamente pentru patinaj artistic</h1>

        <img src="/static/images/poza_echipamente.png">

        {echipamente_patinaj_artistic()}

        <a href="/">Inapoi la Patinaj artistic</a>
        """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
