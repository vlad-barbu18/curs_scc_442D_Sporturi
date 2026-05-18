"""
Aplicatie Flask pentru tema sporturi.
Element ales: polo.
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import reguli_polo, echipament_polo

app = Flask(__name__)

def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML simpla cu stil comun."""
    return f"""
    <html><head><title>{titlu}</title>
    <style>
      body {{ font-family: Arial, sans-serif; background: #e0f2fe; padding: 30px; }}
      .container {{ background: white; max-width: 900px; margin: auto;
                   padding: 30px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
      h1 {{ color: #0369a1; }} 
      h2 {{ color: #0284c7; }}
      p, ul, ol, li {{ line-height: 1.6; font-size: 16px; color: #333; }}
      a {{ background: #0ea5e9; color: white; padding: 10px 15px;
          text-decoration: none; border-radius: 8px; display: inline-block;
          margin: 5px; transition: background 0.3s; }}
      a:hover {{ background: #0284c7; }}
    </style></head><body><div class="container">{continut}</div></body></html>
    """

@app.route("/sporturi")
def tema():
    """Pagina temei."""
    return pagina("Sporturi",
        """<h1>Sporturi</h1>
        <p>Tema proiectului este <b>sporturi</b>. Elementul pe care l-am ales pentru a-l detalia este <b>polo pe apa</b>.</p>
        <p>Acest sport fascinant combina inotul, rezistenta fizica si tactica de echipa intr-un mod unic si extrem de spectaculos.</p>
        <a href="/sporturi/polo">Descopera Polo pe apa</a>""")

@app.route("/sporturi/polo")
def sport():
    """Pagina elementului ales."""
    return pagina("Polo pe apa",
        """<h1>Polo pe apa</h1>
        <p>Polo pe apa (water polo) este adesea descris ca o combinatie intensa intre handbal si inot. A aparut in Marea Britanie la sfarsitul secolului al XIX-lea si este recunoscut drept unul dintre cele mai vechi sporturi de echipa incluse la Jocurile Olimpice.</p>
        <p>Jucatorii au nevoie de o forta fizica extraordinara, rezistenta cardiovasculara superioara si abilitatea de a se mentine constant la suprafata apei folosind o miscare specifica a picioarelor (procedeul "bicicleta"). Este un sport de contact, rapid, in care deciziile tactice se iau in fractiuni de secunda, deoarece efortul depus in apa face ca fiecare miscare sa fie calculata.</p>
        <p>Alege o categorie de mai jos pentru detalii specifice:</p>
        <a href="/sporturi/polo/reguli_polo">Reguli de Joc</a>
        <a href="/sporturi/polo/echipament_polo">Echipament</a>
        <br><br>
        <a href="/sporturi">Inapoi la Tematica</a>""")

@app.route("/sporturi/polo/reguli_polo")
def ruta_functie_1_sport():
    """Ruta 3: afiseaza informatia 1."""
    continut = "<h1>Detalii despre regulament</h1>"
    continut += reguli_polo()
    continut += '<br><a href="/sporturi/polo">Inapoi la Polo</a>'
    return pagina("Reguli Polo", continut)

@app.route("/sporturi/polo/echipament_polo")
def ruta_functie_2_sport():
    """Ruta 4: afiseaza informatia 2."""
    continut = "<h1>Detalii despre echipament</h1>"
    continut += echipament_polo()
    continut += '<br><a href="/sporturi/polo">Inapoi la Polo</a>'
    return pagina("Echipament Polo", continut)

@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
