"""
Aplicatie Flask pentru tema Sporturi.
Sport ales: Patinaj artistic.
"""

from flask import Flask

from app.lib.biblioteca_sporturi import (
    sarituri_patinaj_artistic,
    echipamente_patinaj_artistic,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """
    Creeaza o pagina HTML simpla cu stil comun.
    """
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

@app.route("/sporturi")
def sporturi():
    """
    Afiseaza pagina temei Sporturi.
    """
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>

        <p>
        Tema proiectului este Sporturi. Elementul ales de mine este
        patinajul artistic.
        </p>

        <a href="/sporturi/patinaj-artistic">Patinaj artistic</a>
        """
    )


@app.route("/sporturi/patinaj-artistic")
def patinaj_artistic():
    """
    Afiseaza pagina principala despre patinaj artistic.
    """
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

        <a href="/sporturi/patinaj-artistic/sarituri">Sarituri</a>
	<a href="/sporturi/patinaj-artistic/echipamente">Echipamente</a>
	<a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


@app.route("/sporturi/patinaj-artistic/sarituri")
def sarituri():
    """
    Afiseaza pagina despre sarituri in patinaj artistic.
    """
    return pagina(
        "Sarituri",
        f"""
        <h1>✨ Sarituri in patinaj artistic</h1>

        <img src="/static/images/poza_sarituri.jpeg">

        {sarituri_patinaj_artistic()}

        <a href="/sporturi/patinaj-artistic">Inapoi la Patinaj artistic</a>
        """
    )


@app.route("/sporturi/patinaj-artistic/echipamente")
def echipamente():
    """
    Afiseaza pagina despre echipamentele pentru patinaj artistic.
    """
    return pagina(
        "Echipamente",
        f"""
        <h1>🎽 Echipamente pentru patinaj artistic</h1>

        <img src="/static/images/poza_echipamente.png">

        {echipamente_patinaj_artistic()}

        <a href="/sporturi/patinaj-artistic">Inapoi la Patinaj artistic</a>
        """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
