"""
Sportul ales: Echitatie.
"""


def discipline_echitatie():
    """
    Returneaza informatii despre disciplinele din echitatie.
    """

    return """
    <html>
    <head>
        <title>Discipline Echitatie</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f7efe5;
                color: #3b2f2f;
                padding: 40px;
            }

            h1 {
                text-align: center;
                color: #8b5e3c;
                margin-bottom: 40px;
            }

            .container {
                max-width: 900px;
                margin: auto;
            }

            .card {
                background: white;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 20px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }

            h2 {
                color: #8b5e3c;
            }

            p {
                line-height: 1.6;
            }

            a {
                display: inline-block;
                margin-top: 20px;
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
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Discipline in Echitatie 🐎</h1>

            <div class="card">
                <h2>Sarituri peste obstacole</h2>

                <p>
                Aceasta disciplina presupune depasirea unui traseu
                cu obstacole intr-un timp cat mai bun si fara penalizari.
                </p>
            </div>

            <div class="card">
                <h2>Dresaj</h2>

                <p>
                Dresajul pune accent pe eleganta, precizie si
                controlul miscarilor calului.
                </p>
            </div>

            <div class="card">
                <h2>Curse de cai</h2>

                <p>
                Cursele de cai sunt competitii in care caii si calaretii
                concureaza pentru a ajunge primii la linia de sosire.
                </p>
            </div>

            <div class="card">
                <h2>Polo</h2>

                <p>
                Polo este un sport de echipa in care jucatorii incearca
                sa introduca mingea in poarta adversa folosind un baston special.
                </p>
            </div>

            <a href="/">Inapoi la Home</a>

        </div>

    </body>
    </html>
    """


def echipamente_echitatie():
    """
    Returneaza informatii despre echipamentele folosite in echitatie.
    """

    return """
    <html>
    <head>
        <title>Echipamente Echitatie</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f7efe5;
                color: #3b2f2f;
                padding: 40px;
            }

            .container {
                max-width: 750px;
                margin: auto;
                background: white;
                padding: 25px;
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                text-align: center;
            }

            h1 {
                color: #8b5e3c;
                margin-bottom: 10px;
            }

            .intro {
                font-size: 17px;
                line-height: 1.6;
                margin-bottom: 25px;
            }

            img {
                width: 100%;
                max-width: 650px;
                border-radius: 15px;
                margin: 15px 0 25px 0;
                box-shadow: 0 3px 10px rgba(0,0,0,0.12);
            }

            .lista {
                text-align: left;
                line-height: 1.7;
                font-size: 16px;
            }

            .lista li {
                margin-bottom: 8px;
            }

            a {
                display: inline-block;
                margin-top: 20px;
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
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Echipamente in Echitatie 🐎</h1>

            <p class="intro">
            Echipamentele potrivite asigura siguranta, confortul
            si o comunicare mai buna intre cal si calaret.
            </p>

            <img src="/static/imagini/echipamente_echitatie.jpeg" alt="Echipamente echitatie">

            <ul class="lista">
                <li><b>Seaua</b> ofera stabilitate si confort calaretului.</li>
                <li><b>Pad-ul</b> protejeaza spatele calului si absoarbe socurile.</li>
                <li><b>Ham-ul</b> ajuta la controlul directiei si vitezei calului.</li>
                <li><b>Etrierele</b> ofera sprijin si stabilitate picioarelor.</li>
                <li><b>Casca</b> protejeaza calaretul in caz de cadere.</li>
            </ul>

            <a href="/">Inapoi la Home</a>

        </div>
    </body>
    </html>
    """
