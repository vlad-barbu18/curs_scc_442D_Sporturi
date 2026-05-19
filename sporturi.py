"""Aplicatie Flask pentru tema sporturi, cu focus pe box."""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    competitii_box,
    echipament_box,
)

app = Flask(__name__)


def pagina(titlu: str, subtitlu: str, continut: str, pagina_activa: str) -> str:
    """Creeaza o pagina HTML cu stil comun."""
    return f"""
    <!doctype html>
    <html lang="ro"><head><title>{titlu}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
        color: #18202f;
        background: #f4f6f2;
      }}
      a {{ color: inherit; }}
      .page-shell {{
        width: min(1120px, calc(100% - 32px));
        margin: 0 auto;
        padding: 24px 0 42px;
      }}
      .topbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 18px;
        padding-bottom: 18px;
        border-bottom: 1px solid #d7ddcf;
      }}
      .brand {{
        font-weight: 800;
        text-decoration: none;
        letter-spacing: 0;
      }}
      .nav-links {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
      }}
      .nav-links a {{
        border: 1px solid #d7ddcf;
        border-radius: 8px;
        color: #2b3342;
        padding: 9px 12px;
        text-decoration: none;
        background: #ffffff;
      }}
      .nav-links a.active {{
        border-color: #b42318;
        color: #b42318;
      }}
      .hero {{
        margin-top: 28px;
        padding: 34px;
        border-radius: 8px;
        background: #18202f;
        color: #ffffff;
        overflow: hidden;
      }}
      .eyebrow {{
        margin: 0 0 10px;
        color: #b42318;
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
      }}
      .hero .eyebrow {{ color: #f7c548; }}
      h1, h2, h3, p {{ margin-top: 0; }}
      h1 {{
        margin-bottom: 16px;
        font-size: clamp(2.1rem, 6vw, 4.2rem);
        line-height: 1;
        letter-spacing: 0;
      }}
      h2 {{
        margin-bottom: 12px;
        font-size: 1.75rem;
        line-height: 1.2;
      }}
      h3 {{
        margin-bottom: 10px;
        font-size: 1.08rem;
        line-height: 1.3;
      }}
      p {{
        color: #4a5363;
        line-height: 1.65;
      }}
      .hero p {{ color: #e7ebf0; }}
      .hero-copy {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 180px;
      }}
      .content-section {{
        margin-top: 28px;
        padding: 30px;
        border: 1px solid #d7ddcf;
        border-radius: 8px;
        background: #ffffff;
      }}
      .section-heading {{
        max-width: 760px;
        margin-bottom: 22px;
      }}
      .content-grid,
      .card-grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 16px;
      }}
      .info-card {{
        border: 1px solid #d7ddcf;
        border-radius: 8px;
        padding: 20px;
        background: #fbfcf9;
      }}
      .card-label {{
        margin-bottom: 8px;
        color: #1f6f5b;
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
      }}
      .card-detail {{
        margin-bottom: 0;
        color: #18202f;
        font-weight: 700;
      }}
      .timeline-list {{
        display: grid;
        gap: 12px;
      }}
      .timeline-item {{
        display: grid;
        grid-template-columns: 54px minmax(0, 1fr);
        gap: 16px;
        align-items: start;
        padding: 18px;
        border: 1px solid #d7ddcf;
        border-radius: 8px;
        background: #fbfcf9;
      }}
      .timeline-item span {{
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border-radius: 8px;
        background: #18202f;
        color: #ffffff;
        font-weight: 800;
      }}
      .timeline-item p:last-child,
      .info-card p:last-child {{
        margin-bottom: 0;
      }}
      @media (max-width: 820px) {{
        .topbar {{ align-items: flex-start; flex-direction: column; }}
        .hero {{ padding: 26px; }}
        .hero-copy {{ min-height: auto; }}
        .content-grid,
        .card-grid {{ grid-template-columns: 1fr; }}
        .content-section {{ padding: 22px; }}
      }}
    </style></head>
    <body>
      <main class="page-shell">
        <header class="topbar">
          <a class="brand" href="/sporturi">Sporturi SCC</a>
          <nav class="nav-links" aria-label="Navigatie principala">
            <a class="{"active" if pagina_activa == "sporturi" else ""}"
               href="/sporturi">Tema</a>
            <a class="{"active" if pagina_activa == "box" else ""}"
               href="/sporturi/box">Box</a>
            <a class="{"active" if pagina_activa == "echipament" else ""}"
               href="/sporturi/box/echipament">Echipament</a>
            <a class="{"active" if pagina_activa == "competitii" else ""}"
               href="/sporturi/box/competitii">Competitii</a>
          </nav>
        </header>
        <section class="hero">
          <div class="hero-copy">
            <p class="eyebrow">Proiect SCC</p>
            <h1>{titlu}</h1>
            <p>{subtitlu}</p>
          </div>
        </section>
        {continut}
      </main>
    </body></html>
    """


@app.route("/sporturi")
def tema():
    """Pagina temei."""
    continut = """
    <section class="content-section">
      <div class="content-grid">
        <article class="info-card">
          <p class="card-label">Tema grupei</p>
          <h2>Sporturi</h2>
          <p>
            Tema grupei este lumea sporturilor: disciplina, pregatirea,
            competitia si regulile care transforma miscarea intr-o activitate
            organizata.
          </p>
        </article>
        <article class="info-card">
          <p class="card-label">Sport ales</p>
          <h2>Boxul</h2>
          <p>
            Sportul ales de mine este boxul, un sport de contact bazat pe
            tehnica, viteza, rezistenta si control mental.
          </p>
        </article>
      </div>
    </section>
    """
    return pagina(
        "Sporturi",
        "Tema grupei este sporturi, iar sportul ales pentru proiect este boxul.",
        continut,
        "sporturi",
    )


@app.route("/sporturi/box")
def sport():
    """Pagina elementului ales."""
    continut = """
    <section class="content-section">
      <div class="section-heading">
        <p class="eyebrow">Descriere generala</p>
        <h2>Ce este boxul?</h2>
        <p>
          Boxul este un sport de lupta in care doi sportivi concureaza intr-un
          ring, folosind doar lovituri cu pumnii, aparare, deplasare si tactica.
          Meciurile sunt impartite in reprize, iar rezultatul poate fi decis
          prin punctaj, abandon, oprirea arbitrului sau knockout.
        </p>
      </div>
      <div class="content-grid">
        <article class="info-card">
          <p class="card-label">Tehnica</p>
          <h3>Lovituri si aparare</h3>
          <p>
            Jab-ul, directa, croseul si upercutul sunt combinate cu garda,
            eschivele si pasii laterali.
          </p>
        </article>
        <article class="info-card">
          <p class="card-label">Pregatire</p>
          <h3>Rezistenta si disciplina</h3>
          <p>
            Un boxer lucreaza constant la conditie fizica, viteza de reactie,
            coordonare si strategie.
          </p>
        </article>
      </div>
    </section>
    """
    return pagina(
        "Box",
        "Un sport de contact in care forta conteaza, dar tehnica si luciditatea "
        "fac diferenta.",
        continut,
        "box",
    )


@app.route("/")
def index():
    """Redirect spre pagina temei."""
    return redirect("/sporturi")


@app.route("/sporturi/box/echipament")
def ruta_echipament_box():
    """Pagina cu echipamentul folosit in box."""
    continut = echipament_box()
    return pagina(
        "Echipament",
        "Piesele de baza folosite in box si rolul fiecareia in siguranta "
        "sportivului.",
        continut,
        "echipament",
    )


@app.route("/sporturi/box/competitii")
def ruta_competitii_box():
    """Pagina cu competitiile disponibile in box."""
    continut = competitii_box()
    return pagina(
        "Competitii",
        "Principalele trasee competitionale pentru boxeri amatori si "
        "profesionisti.",
        continut,
        "competitii",
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
