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
        <a href="{url_for('pagina_sporturi')}">Sporturi</a> |
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
    adaptata pentru tema Sporturi.
    </p>

    <p>
    Elementul ales este <b>ciclismul</b>. Aplicatia prezinta informatii despre
    competitiile de ciclism si echipamentele folosite de ciclisti.
    </p>

    <ul>
        <li>Pagina pentru tema generala: Sporturi</li>
        <li>Pagina pentru elementul ales: Ciclism</li>
        <li>Pagina pentru competitii de ciclism</li>
        <li>Pagina pentru echipament de ciclism</li>
    </ul>
    """
    return pagina_html("Aplicatie Sporturi - Ciclism", continut)


@app.route("/sporturi", methods=["GET"])
def pagina_sporturi():
    """
    Pagina pentru tema generala Sporturi.
    """
    continut = """
    <p>
    Sporturile sunt activitati fizice organizate, practicate individual sau in echipa,
    pe baza unor reguli. Acestea pot avea scop recreativ, educational sau competitional.
    </p>

    <p>
    Exemple de sporturi sunt: fotbal, baschet, tenis, inot, atletism si ciclism.
    In aceasta aplicatie, sportul prezentat este ciclismul.
    </p>
    """
    return pagina_html("Tema proiectului: Sporturi", continut)


@app.route("/sporturi/ciclism", methods=["GET"])
def pagina_ciclism():
    """
    Pagina pentru elementul ales: Ciclism.
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
    return pagina_html("Element ales: Ciclism", continut)


@app.route("/sporturi/ciclism/competitii", methods=["GET"])
def pagina_competitii_ciclism():
    """
    Pagina pentru competitiile de ciclism.
    """
    return pagina_html("Competitii de ciclism", competitii_ciclism())


@app.route("/sporturi/ciclism/echipament", methods=["GET"])
def pagina_echipament_ciclism():
    """
    Pagina pentru echipamentul de ciclism.
    """
    return pagina_html("Echipament de ciclism", echipament_ciclism())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)