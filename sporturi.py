"""
Aplicatie pentru tema fotbal
"""
from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    competitii_fotbal,
    echipament_fotbal,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Design pagina"""
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            * {{ box-sizing: border-box; }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
                background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0d1117 100%);
                background-attachment: fixed;
                color: #e6edf3;
                margin: 0;
                padding: 40px 20px;
                min-height: 100vh;
                line-height: 1.6;
            }}
            .container {{
                background: rgba(22, 27, 34, 0.85);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                max-width: 1000px;
                margin: auto;
                padding: 40px;
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.08);
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            }}
            h1 {{
                color: #58a6ff;
                font-size: 36px;
                font-weight: 700;
                margin: 0 0 24px;
                padding-bottom: 16px;
                border-bottom: 2px solid rgba(88, 166, 255, 0.3);
                letter-spacing: -0.5px;
            }}
            h2 {{
                color: #3fb950;
                font-size: 22px;
                font-weight: 600;
                margin-top: 32px;
                margin-bottom: 16px;
                padding-left: 12px;
                border-left: 4px solid #3fb950;
            }}
            p {{
                font-size: 17px;
                color: #c9d1d9;
                margin: 12px 0;
            }}
            ul {{
                list-style: none;
                padding-left: 0;
            }}
            ul li {{
                padding: 10px 14px;
                margin: 6px 0;
                background: rgba(48, 54, 61, 0.4);
                border-radius: 8px;
                border-left: 3px solid #58a6ff;
                color: #c9d1d9;
            }}
            ul li b {{
                color: #f0883e;
                font-weight: 600;
            }}
            b {{ color: #f0883e; }}
            a {{
                color: white;
                padding: 12px 22px;
                text-decoration: none;
                border-radius: 10px;
                display: inline-block;
                margin: 8px 6px 8px 0;
                font-weight: 600;
                font-size: 15px;
                transition: all 0.25s ease;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            }}
            /* Buton primar - albastru Champions League */
            a {{
                background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
                border: 1px solid rgba(88, 166, 255, 0.4);
            }}
            a:hover {{
                background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4);
            }}
            /* Buton portocaliu - Europa League */
            a[href*="competitii"] {{
                background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%);
                border: 1px solid rgba(251, 146, 60, 0.4);
            }}
            a[href*="competitii"]:hover {{
                background: linear-gradient(135deg, #ea580c 0%, #f97316 100%);
                box-shadow: 0 8px 20px rgba(234, 88, 12, 0.4);
            }}
            /* Buton verde - Conference League */
            a[href*="echipament"] {{
                background: linear-gradient(135deg, #166534 0%, #16a34a 100%);
                border: 1px solid rgba(74, 222, 128, 0.4);
            }}
            a[href*="echipament"]:hover {{
                background: linear-gradient(135deg, #16a34a 0%, #22c55e 100%);
                box-shadow: 0 8px 20px rgba(22, 163, 74, 0.4);
            }}
            /* Buton inapoi - mai discret */
            a[href="/sporturi"], a[href="/sporturi/fotbal"] {{
                background: linear-gradient(135deg, #374151 0%, #4b5563 100%);
                border: 1px solid rgba(156, 163, 175, 0.3);
            }}
            a[href="/sporturi"]:hover, a[href="/sporturi/fotbal"]:hover {{
                background: linear-gradient(135deg, #4b5563 0%, #6b7280 100%);
            }}
            /* Card-uri pentru competitii (div-urile din biblioteca) */
            div[style*="border-left"] {{
                background: rgba(13, 17, 23, 0.6) !important;
                padding: 16px 20px !important;
                margin-bottom: 14px !important;
                border-radius: 8px !important;
                border-left-width: 4px !important;
                transition: transform 0.2s ease;
            }}
            div[style*="border-left"]:hover {{
                transform: translateX(4px);
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
    """Ruta cu descrierea temei"""
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>
        <p>Proiect SCC 2026 &mdash; Barbu Vlad-Catalin</p>
        <a href="/sporturi/fotbal">Fotbal &rarr;</a>
        """
    )


# a doua ruta cu sportul ales
@app.route("/sporturi/fotbal")
def fotbal():
    """Ruta cu tema alesa si butoanele"""
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
        <a href="/sporturi">&larr; Inapoi la Sporturi</a>
        """
    )


# a treia ruta cu competitii
@app.route("/sporturi/fotbal/competitii_fotbal")
def ruta_competitii_fotbal():
    """Ruta pentru competitii"""
    continut = "<h1>Competitii de fotbal</h1>"
    continut += competitii_fotbal()
    continut += '<a href="/sporturi/fotbal">&larr; Inapoi la Fotbal</a>'
    return pagina("Competitii Fotbal", continut)


# a patra ruta cu echipmanet
@app.route("/sporturi/fotbal/echipament_fotbal")
def ruta_echipament_fotbal():
    """Ruta pentru echipament"""
    continut = "<h1>Echipament de fotbal</h1>"
    continut += echipament_fotbal()
    continut += '<a href="/sporturi/fotbal">&larr; Inapoi la Fotbal</a>'
    return pagina("Echipament Fotbal", continut)


@app.route("/")
def index():
    """Ruta pentru trimitere automata la tema proiectului"""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5014)
