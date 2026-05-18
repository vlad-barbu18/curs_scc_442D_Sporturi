"""
Aplicatie WEB Flask pentru tema Sporturi.
Sportul: Ciclism.
"""

from flask import Flask, url_for

from app.lib.biblioteca_sporturi import competitii_ciclism, echipament_ciclism


app = Flask(__name__)


def meniu_navigare():
    """
    Genereaza meniul de navigare al aplicatiei.
    """
    return f"""
    <nav>
        <a href="{url_for('index')}">Acasa</a> |
        <a href="{url_for('pagina_ciclism')}">Ciclism</a> |
        <a href="{url_for('pagina_competitii_ciclism')}">Competitii</a> |
        <a href="{url_for('pagina_echipament_ciclism')}">Echipament</a>
    </nav>
    <hr>
    """


def pagina_html(titlu, continut):
    """
    Genereaza structura HTML comuna pentru paginile aplicatiei.
    """
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                color: #222;
                margin: 40px;
                line-height: 1.6;
            }}

            h1 {{
                color: #0b5ed7;
            }}

            h2 {{
                color: #198754;
            }}

            nav a {{
                color: #0b5ed7;
                font-weight: bold;
                text-decoration: none;
            }}

            nav a:hover {{
                text-decoration: underline;
            }}

            .container {{
                background-color: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}

            figure {{
                margin: 20px 0;
            }}

            img {{
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }}

            figcaption {{
                font-size: 14px;
                color: #555;
                margin-top: 8px;
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {meniu_navigare()}
            <h1>{titlu}</h1>
            {continut}
        </div>
    </body>
    </html>
    """


@app.route("/", methods=["GET"])
def index():
    """
    Pagina principala a aplicatiei.
    """
    continut = """
    <p>
    Aceasta aplicatie WEB este realizata in Python folosind framework-ul Flask.
    Aplicatia are la baza scheletul proiectului sysinfo, dar functionalitatea a fost
    adaptata pentru prezentarea ciclismului.
    </p>

    <p>
    Aplicatia prezinta informatii despre <b>ciclism</b>, competitiile importante
    din acest domeniu si echipamentele folosite de ciclisti.
    </p>

    <ul>
        <li>Pagina principala</li>
        <li>Pagina despre ciclism</li>
        <li>Pagina despre competitii de ciclism</li>
        <li>Pagina despre echipament de ciclism</li>
    </ul>
    """
    return pagina_html("Aplicatie despre ciclism", continut)


@app.route("/ciclism", methods=["GET"])
def pagina_ciclism():
    """
    Pagina despre ciclism.
    """
    continut = """
    <p>
    Ciclismul este un sport bazat pe folosirea bicicletei. Poate fi practicat
    atat recreational, cat si la nivel profesionist.
    </p>

    <p>
    Exista mai multe forme de ciclism: ciclism pe sosea, ciclism montan,
    ciclism pe pista, BMX si gravel.
    </p>

    <p>
    In cadrul proiectului sunt prezentate competitiile importante de ciclism
    si echipamentele folosite de ciclisti.
    </p>
    """
    return pagina_html("Ciclism", continut)


@app.route("/ciclism/competitii", methods=["GET"])
def pagina_competitii_ciclism():
    """
    Pagina pentru competitiile de ciclism.
    """
    imagine_url = url_for(
        "static",
        filename="images/stage2.jpeg"
    )

    return pagina_html(
        "Competitii de ciclism",
        competitii_ciclism(imagine_url)
    )


@app.route("/ciclism/echipament", methods=["GET"])
def pagina_echipament_ciclism():
    """
    Pagina pentru echipamentul de ciclism.
    """
    imagine_url = url_for(
        "static",
        filename="images/bicla.jpeg"
    )

    return pagina_html(
        "Echipament de ciclism",
        echipament_ciclism(imagine_url)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)