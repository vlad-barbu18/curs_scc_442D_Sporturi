from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Baschet</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e5e7eb;
                margin: 0;
                padding: 0;
            }
            header {
                background: #f97316;
                padding: 20px;
                text-align: center;
                color: white;
            }
            nav {
                background: #1e293b;
                padding: 15px;
                text-align: center;
            }
            nav a {
                color: #e5e7eb;
                margin: 0 15px;
                text-decoration: none;
                font-weight: bold;
            }
            section {
                padding: 40px;
                max-width: 900px;
                margin: auto;
            }
            .card {
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Baschet</h1>
            <p>Aplicație web despre competiții și echipamente de baschet</p>
        </header>

        <nav>
            <a href="/">Acasă</a>
            <a href="/competitii">Competiții</a>
            <a href="/echipament">Echipament</a>
        </nav>

        <section>
            <div class="card">
                <h2>Despre baschet</h2>
                <p>
                    Baschetul este un sport de echipă în care două formații încearcă
                    să înscrie puncte prin aruncarea mingii în coșul advers.
                </p>
            </div>

            <div class="card">
                <h2>Ce conține aplicația?</h2>
                <p>
                    Aplicația prezintă informații despre principalele competiții de baschet
                    și despre echipamentele folosite de jucători.
                </p>
            </div>
        </section>
    </body>
    </html>
    """


@app.route("/competitii")
def competitii():
    return """
    <html>
    <head>
        <title>Competiții de baschet</title>
        <style>
            body { font-family: Arial; background: #0f172a; color: #e5e7eb; padding: 40px; }
            a { color: #f97316; }
            .card { background: #1e293b; padding: 20px; border-radius: 12px; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <h1>Competiții de baschet</h1>
        <a href="/">Înapoi la pagina principală</a>

        <div class="card">
            <h2>NBA</h2>
            <p>NBA este cea mai cunoscută ligă profesionistă de baschet din lume.</p>
        </div>

        <div class="card">
            <h2>EuroLeague</h2>
            <p>EuroLeague este una dintre cele mai importante competiții de baschet din Europa.</p>
        </div>

        <div class="card">
            <h2>FIBA Basketball World Cup</h2>
            <p>Campionatul Mondial FIBA este competiția internațională dedicată echipelor naționale.</p>
        </div>
    </body>
    </html>
    """


@app.route("/echipament")
def echipament():
    return """
    <html>
    <head>
        <title>Echipament de baschet</title>
        <style>
            body { font-family: Arial; background: #0f172a; color: #e5e7eb; padding: 40px; }
            a { color: #f97316; }
            .card { background: #1e293b; padding: 20px; border-radius: 12px; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <h1>Echipament de baschet</h1>
        <a href="/">Înapoi la pagina principală</a>

        <div class="card">
            <h2>Mingea de baschet</h2>
            <p>Este elementul principal al jocului și are dimensiuni diferite în funcție de categorie.</p>
        </div>

        <div class="card">
            <h2>Coșul de baschet</h2>
            <p>Este format din panou, inel și plasă. Înălțimea standard a inelului este de 3,05 m.</p>
        </div>

        <div class="card">
            <h2>Încălțămintea</h2>
            <p>Pantofii de baschet oferă aderență, stabilitate și protecție pentru gleznă.</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
