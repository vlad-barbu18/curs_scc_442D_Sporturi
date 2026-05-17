
# Aplicatie pentru tema fotbal


from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    competitii_fotbal,
    echipament_fotbal,
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
            h1 {{ color: #1d4ed8; }}
            h2 {{ color: #16a34a; margin-top: 30px; }}
            p  {{ font-size: 18px; line-height: 1.6; }}
            a  {{
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
        <div class="container">{continut}</div>
    </body>
    </html>
    """



# prima ruta cu tema
@app.route("/sporturi")
def sporturi():
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>Proiect SCC 2026 - Barbu Vlad-Catalin</p>
        <a href="/sporturi/fotbal">Fotbal</a>
        """
    )


# a doua ruta cu sportul ales
@app.route("/sporturi/fotbal")
def fotbal():
    return pagina(
        "Fotbal",
        """
        <h1>Fotbal</h1>
        <p>
        Fotbalul este cel mai popular sport din lume, jucat de doua echipe de
        cate 11 jucatori. Scopul este sa marchezi mai multe goluri decat
        adversarul intr-un meci de 90 de minute.
        </p>
        <a href="/sporturi/fotbal/competitii_fotbal">Competitii fotbal</a>
        <a href="/sporturi/fotbal/echipament_fotbal">Echipament fotbal</a>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


# a treia ruta cu competitii
@app.route("/sporturi/fotbal/competitii_fotbal")
def ruta_competitii_fotbal():
    continut = "<h1>Competitii de fotbal</h1>"
    continut += competitii_fotbal()
    continut += '<a href="/sporturi/fotbal">Inapoi la Fotbal</a>'
    return pagina("Competitii Fotbal", continut)


# a patra ruta cu echipmanet
@app.route("/sporturi/fotbal/echipament_fotbal")
def ruta_echipament_fotbal():
    continut = "<h1>Echipament de fotbal</h1>"
    continut += echipament_fotbal()
    continut += '<a href="/sporturi/fotbal">Inapoi la Fotbal</a>'
    return pagina("Echipament Fotbal", continut)


@app.route("/")
def index():
    return redirect("/sporturi")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
