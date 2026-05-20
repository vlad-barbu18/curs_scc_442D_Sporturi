"""
Blueprint pentru elementul ales: Inot.

Inregistreaza cele 4 rute conform cerintei:
- /sporturi                         -> pagina temei
- /sporturi/inot                    -> pagina elementului ales
- /sporturi/inot/concursuri         -> functia 1
- /sporturi/inot/inotatori          -> functia 2
"""

from flask import Blueprint, redirect

from app.lib.biblioteca_inot import (
    concursuri_inot,
    inotatori_inot,
)

inot_bp = Blueprint("inot", __name__)


def pagina(titlu: str, sub_titlu: str, ruta_activa: str, continut: str) -> str:
    """Construieste o pagina HTML cu header, navigare si stil comun."""
    def link(eticheta: str, href: str, cheie: str) -> str:
        clasa = "nav-link active" if cheie == ruta_activa else "nav-link"
        return f'<a class="{clasa}" href="{href}">{eticheta}</a>'

    nav = (
        link("Acasa", "/sporturi/inot", "acasa")
        + link("Concursuri", "/sporturi/inot/concursuri", "concursuri")
        + link("Inotatori", "/sporturi/inot/inotatori", "inotatori")
    )

    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<title>{titlu}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    font-family: Arial, sans-serif;
    background: #f5f7fa;
    margin: 0;
    color: #1f2937;
  }}
  .container {{
    max-width: 900px;
    margin: 0 auto;
    padding: 30px 40px;
    background: #ffffff;
    min-height: 100vh;
  }}
  .header h1 {{
    margin: 0;
    color: #111827;
    font-size: 28px;
  }}
  .header .subtitle {{
    color: #6b7280;
    font-size: 14px;
    margin-top: 4px;
  }}
  hr {{
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 18px 0 24px 0;
  }}
  .nav {{ margin-bottom: 24px; }}
  .nav-link {{
    color: #2563eb;
    text-decoration: none;
    margin-right: 18px;
    font-size: 15px;
  }}
  .nav-link:hover {{ text-decoration: underline; }}
  .nav-link.active {{ font-weight: bold; }}
  h2 {{
    color: #111827;
    font-size: 20px;
    margin-top: 24px;
    margin-bottom: 16px;
  }}
  .card {{
    border-left: 3px solid #2563eb;
    padding: 0 0 0 16px;
    margin-bottom: 28px;
  }}
  .card h3 {{
    margin: 0 0 10px 0;
    color: #111827;
    font-size: 16px;
  }}
  .card-img {{
    display: block;
    max-width: 100%;
    width: 320px;
    height: auto;
    border-radius: 4px;
    margin: 6px 0 10px 0;
  }}
  .card-body p {{
    margin: 4px 0;
    font-size: 14px;
    line-height: 1.5;
  }}
  .card-body .meta {{
    color: #6b7280;
    font-size: 13px;
  }}
  .hero-img {{
    display: block;
    max-width: 100%;
    border-radius: 6px;
    margin: 12px 0 18px 0;
  }}
  .next-link {{
    display: inline-block;
    margin-top: 24px;
    padding: 10px 16px;
    background: #eff6ff;
    color: #2563eb;
    text-decoration: none;
    border-radius: 4px;
  }}
  .next-link:hover {{ background: #dbeafe; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>{titlu}</h1>
    <div class="subtitle">{sub_titlu}</div>
  </div>
  <hr>
  <div class="nav">{nav}</div>
  {continut}
</div>
</body>
</html>"""


@inot_bp.route("/sporturi")
def sporturi():
    """Ruta 1: pagina temei (Sporturi)."""
    continut = """
    <h2>Tema proiect: Sporturi</h2>
    <p>Acest site prezinta tema <b>Sporturi</b>, dezvoltata de grupa noastra in cadrul
       proiectului SCC. Fiecare student a ales un element din tema si a construit o
       sectiune dedicata.</p>
    <p>Elementul ales de mine este <b>Inotul</b>.</p>
    <a class="next-link" href="/sporturi/inot">Pagina urmatoare: Inot &rarr;</a>
    """
    return pagina("Sporturi", "Tema proiect SCC - grupa", "acasa", continut)


@inot_bp.route("/sporturi/inot")
def inot():
    """Ruta 2: pagina elementului ales (Inot) - 'Despre proiect'."""
    continut = """
    <h2>Despre proiect</h2>
    <img class="hero-img" src="/static/images/inot_acasa.jpg" alt="Inot">
    <p>Inotul este unul dintre cele mai complexe si elegante sporturi, fiind practicat
       atat la nivel recreational, cat si la nivel de performanta. Acesta dezvolta
       rezistenta cardiovasculara, forta musculara, coordonarea si disciplina, avand
       in acelasi timp un impact redus asupra articulatiilor.</p>
    <p>Acest proiect prezinta informatii despre inot, competitiile importante din
       acest sport si cativa dintre cei mai cunoscuti inotatori profesionisti din lume.
       Scopul site-ului este de a evidentia importanta inotului, beneficiile sale si
       performantele remarcabile obtinute de sportivi la nivel international.</p>
    <a class="next-link" href="/sporturi/inot/concursuri">Pagina urmatoare: Concursuri &rarr;</a>
    """
    return pagina("Inot", "Tema proiect SCC - Ovezea Corina", "acasa", continut)


@inot_bp.route("/sporturi/inot/concursuri")
def concursuri():
    """Ruta 3: functia 1 - concursuri internationale."""
    continut = concursuri_inot()
    continut += (
        '<a class="next-link" href="/sporturi/inot/inotatori">'
        'Pagina urmatoare: Inotatori &rarr;</a>'
    )
    return pagina("Inot", "Tema proiect SCC - Ovezea Corina", "concursuri", continut)


@inot_bp.route("/sporturi/inot/inotatori")
def inotatori():
    """Ruta 4: functia 2 - inotatori profesionisti."""
    continut = inotatori_inot()
    continut += '<a class="next-link" href="/sporturi/inot">&larr; Inapoi la Inot</a>'
    return pagina("Inot", "Tema proiect SCC - Ovezea Corina", "inotatori", continut)


@inot_bp.route("/")
def index():
    """Redirect din root spre pagina temei."""
    return redirect("/sporturi")
