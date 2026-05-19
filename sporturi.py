"""
Aplicatie Flask pentru tema sporturi.
Element ales: scrima.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    functie_1_scrima,
    functie_2_scrima,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html><head><title>{titlu}</title>
    <style>
      body {{ font-family: Arial; background: #ffe4e6; padding: 30px; }}
      .container {{ background: white; max-width: 900px; margin: auto;
                   padding: 30px; border-radius: 12px; }}
      h1 {{ color: #1d4ed8; }} h2 {{ color: #16a34a; }}
      a {{ background: #f87171; color: white; padding: 10px 15px;
          text-decoration: none; border-radius: 8px; display: inline-block;
          margin: 5px; }}
    </style></head><body><div class="container">{continut}</div></body></html>
    """


@app.route("/sporturi")
def tema():
    """Pagina temei."""
    return pagina("Sporturi",
        """<h1>Sporturi</h1>
        <p> Sportul reprezinta o activitate importanta pentru dezvoltarea fizica
    si mentala, contribuind la imbunatatirea conditiei fizice, disciplinei
    si spiritului competitiv. De-a lungul timpului, diferite ramuri sportive
    au devenit populare la nivel mondial datorita valorilor promovate,
    precum fair-play-ul, perseverenta si munca in echipa.</p>

<div style="text-align: center;">
    <img src="https://arenavalceana.ro/wp-content/uploads/2023/11/WP-top-10-cele-mai-populare-sporturi-din-lume-e1701093886968.jpg"
         width="500"
         style="border-radius: 12px; margin-top: 20px;">
</div>

<br><br>

        <a href="/sporturi/scrima">Scrima</a>""")


@app.route("/sporturi/scrima")
def sport():
    """Pagina elementului ales."""
    return pagina("Scrima",
        """<h1>Scrima</h1>
        <p> Scrima reprezinta unul dintre cele mai tehnice si elegante sporturi
    olimpice, bazat pe reflexe rapide, tactica si control. Competitiile
    de scrima implica dueluri intre sportivi folosind arme specializate,
    fiecare avand reguli si stiluri diferite de joc.</p>
        

    <img src="https://sportriposta.ro/wp-content/uploads/2022/05/Istoric-scrima%CC%86.png"
         width="500"
         style="border-radius: 12px; margin-top: 20px;">

    <br><br>


	<a href="/sporturi/scrima/functie_1_scrima">Generalitati</a>
	<a href="/sporturi/scrima/functie_2_scrima">Tipuri de arme</a>
	<a href="/sporturi">Inapoi la Sporturi</a>""")


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


@app.route("/sporturi/scrima/functie_1_scrima")
def ruta_functie_1_scrima():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Informatii generale despre scrima</h1>"
    continut += functie_1_scrima()
    continut += '<a href="/sporturi/scrima">Inapoi</a>'
    return pagina("Informatii generale", continut)


@app.route("/sporturi/scrima/functie_2_scrima")
def ruta_functie_2_scrima():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Tipuri de arme in scrima</h1>"
    continut += functie_2_scrima()
    continut += '<a href="/sporturi/scrima">Inapoi</a>'
    return pagina("Tipuri de arme", continut)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
