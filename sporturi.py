"""
Aplicatie pentru tema fotbal
"""

from flask import Flask, redirect

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



@app.route("/sporturi")
def sporturi():
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>fotbal.</p>
        <a href="/sporturi/fotbal">Fotbal</a>
        """
    )


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
        <p>Pagina elementului. Rutele cu informatii specifice vin in etapa urmatoare.</p>
        <a href="/sporturi">Inapoi la Sporturi</a>
        """
    )


@app.route("/")
def index():
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
