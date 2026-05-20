from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_padel,
    functie_2_padel,
)

app = Flask(__name__)

#comentariu 

def pagina(titlu: str, continut: str) -> str:
    return f"""
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #dcfce7, #f0fdf4);
                color: #1f2937;
                min-height: 100vh;
            }}

            .header {{
                background: #166534;
                color: white;
                padding: 22px 40px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.18);
            }}

            .header h1 {{
                margin: 0;
                font-size: 34px;
                color: white;
                border: none;
                padding: 0;
            }}

            .header p {{
                margin-top: 8px;
                font-size: 16px;
                background: none;
                border: none;
                color: #dcfce7;
                padding: 0;
            }}

            .container {{
                background: #ffffff;
                max-width: 1000px;
                margin: 35px auto;
                padding: 35px;
                border-radius: 20px;
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
                border: 1px solid #bbf7d0;
            }}

            h1 {{
                color: #166534;
                font-size: 34px;
                margin-top: 0;
                border-bottom: 3px solid #86efac;
                padding-bottom: 12px;
            }}

            h2 {{
                color: #15803d;
                margin-top: 25px;
            }}

            p {{
                font-size: 17px;
                line-height: 1.7;
                background: #f0fdf4;
                padding: 15px;
                border-left: 5px solid #22c55e;
                border-radius: 10px;
            }}

            a {{
                background: #16a34a;
                color: white;
                padding: 11px 18px;
                text-decoration: none;
                border-radius: 10px;
                display: inline-block;
                margin: 8px 6px 0 0;
                font-weight: bold;
                transition: 0.2s;
            }}

            a:hover {{
                background: #15803d;
                transform: translateY(-2px);
            }}

            .card {{
                background: #ecfdf5;
                padding: 22px;
                border-radius: 16px;
                border: 1px solid #bbf7d0;
                margin-top: 20px;
            }}

            .butoane {{
                margin-top: 25px;
            }}

            .imagine-principala {{
                width: 100%;
                height: 320px;
                object-fit: cover;
                border-radius: 18px;
                margin-bottom: 25px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.16);
            }}

            .galerie {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin-top: 25px;
            }}

            .poza-card {{
                background: #f0fdf4;
                border-radius: 16px;
                padding: 15px;
                border: 1px solid #bbf7d0;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            }}

            .poza-card img {{
                width: 100%;
                height: 220px;
                object-fit: cover;
                border-radius: 13px;
            }}

            .poza-card h2 {{
                margin-bottom: 8px;
            }}

            .footer {{
                text-align: center;
                color: #166534;
                padding: 20px;
                font-size: 14px;
            }}

            @media (max-width: 700px) {{
                .container {{
                    margin: 20px;
                    padding: 22px;
                }}

                .galerie {{
                    grid-template-columns: 1fr;
                }}

                .imagine-principala {{
                    height: 230px;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="header">
            <h1>Proiect Sporturi</h1>
            <p>Element ales: Padel</p>
        </div>

        <div class="container">
            {continut}
        </div>

        <div class="footer">
            Proiect realizat pentru tema Sporturi - Padel
        </div>
    </body>
    </html>
    """


@app.route("/sporturi")
def sporturi():
    return pagina(
        "Sporturi",
        """
        <h1>Sporturi</h1>

        <img class="imagine-principala" src="/static/imagini/padel-teren.jpg" alt="Teren de padel">

        <div class="card">
            <p>
                Tema proiectului este sporturi, iar elementul ales este padel.
                Acest site prezinta informatii generale despre padel, regulile de baza
                si cateva aspecte importante despre acest sport.
            </p>
        </div>

        <div class="butoane">
            <a href="/sporturi/padel">Vezi pagina Padel</a>
        </div>
        """
    )


@app.route("/sporturi/padel")
def padel():
    return pagina(
        "Padel",
        """
        <h1>Padel</h1>

        <div class="card">
            <p>
                Padelul este un sport de racheta asemanator cu tenisul,
                jucat de obicei la dublu, pe un teren inchis cu pereti de sticla.
            </p>

            <p>
                Este un sport rapid, accesibil si popular datorita combinatiei
                dintre tehnica, strategie si lucru in echipa.
            </p>
        </div>

        <div class="galerie">
            <div class="poza-card">
                <img src="/static/imagini/padel-racheta-minge.jpg" alt="Racheta si minge de padel">
                <h2>Echipament</h2>
                <p>
                    Pentru padel se folosesc o racheta speciala si o minge asemanatoare
                    cu cea de tenis.
                </p>
            </div>

            <div class="poza-card">
                <img src="/static/imagini/padel-jucatori.jpg" alt="Jucatori de padel">
                <h2>Joc in echipa</h2>
                <p>
                    Padelul se joaca cel mai des la dublu, fiind importanta comunicarea
                    dintre coechipieri.
                </p>
            </div>
        </div>

        <div class="butoane">
            <a href="/sporturi/padel/functie_1_padel">Informatia 1</a>
            <a href="/sporturi/padel/functie_2_padel">Informatia 2</a>
            <a href="/sporturi">Inapoi la Sporturi</a>
        </div>
        """
    )


@app.route("/sporturi/padel/functie_1_padel")
def ruta_functie_1_padel():
    continut = """
    <h1>Informatia 1 despre padel</h1>

    <div class="card">
    """
    continut += functie_1_padel()
    continut += """
    </div>

    <div class="butoane">
        <a href="/sporturi/padel">Inapoi la Padel</a>
    </div>
    """

    return pagina("Informatia 1", continut)


@app.route("/sporturi/padel/functie_2_padel")
def ruta_functie_2_padel():
    continut = """
    <h1>Informatia 2 despre padel</h1>

    <div class="card">
    """
    continut += functie_2_padel()
    continut += """
    </div>

    <div class="butoane">
        <a href="/sporturi/padel">Inapoi la Padel</a>
    </div>
    """

    return pagina("Informatia 2", continut)


@app.route("/")
def index():
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
