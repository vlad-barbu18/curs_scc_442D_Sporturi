"""
Aplicatie Flask pentru tema sporturi.
Sport ales: sah.
"""

from flask import Flask, redirect

from app.lib.biblioteca_sporturi import (
    genereaza_competitii_sah,
    genereaza_regulament_sah,
)

app = Flask(__name__)


def navigatie() -> str:
    """Returneaza meniul principal al aplicatiei."""
    return """
    <nav class="top-nav" aria-label="Navigatie principala">
      <a href="/sporturi">Sporturi</a>
      <a href="/sporturi/sah">Sah</a>
      <a href="/sporturi/sah/regulament">Regulament</a>
      <a href="/sporturi/sah/competitii">Competitii</a>
    </nav>
    """


def tabla_sah() -> str:
    """Returneaza o tabla de sah decorativa, construita in HTML."""
    piese = [
        "&#9820;", "&#9822;", "&#9821;", "&#9819;", "&#9818;", "&#9821;", "&#9822;", "&#9820;",
        "&#9823;", "&#9823;", "&#9823;", "&#9823;", "&#9823;", "&#9823;", "&#9823;", "&#9823;",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "&#9817;", "&#9817;", "&#9817;", "&#9817;", "&#9817;", "&#9817;", "&#9817;", "&#9817;",
        "&#9814;", "&#9816;", "&#9815;", "&#9813;", "&#9812;", "&#9815;", "&#9816;", "&#9814;",
    ]
    patrate = []
    for pozitie, piesa in enumerate(piese):
        culoare = "light" if (pozitie + pozitie // 8) % 2 == 0 else "dark"
        patrate.append(f'<span class="{culoare}">{piesa}</span>')
    return '<div class="chessboard" aria-label="Tabla de sah">' + "".join(patrate) + "</div>"


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML cu stil comun pentru toate rutele."""
    return f"""
    <!doctype html>
    <html lang="ro">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{titlu}</title>
      <style>
        :root {{
          --ink: #15181d;
          --muted: #5c6572;
          --paper: #fffaf0;
          --surface: #ffffff;
          --line: #ded6c7;
          --green: #116149;
          --gold: #c58b2c;
          --red: #8f2e2e;
          --dark-square: #7b5338;
          --light-square: #efd9b6;
        }}
        * {{ box-sizing: border-box; }}
        body {{
          margin: 0;
          color: var(--ink);
          background: var(--paper);
          font-family: Arial, Helvetica, sans-serif;
          line-height: 1.6;
        }}
        .page {{
          min-height: 100vh;
        }}
        .top-nav {{
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
          align-items: center;
          justify-content: center;
          padding: 18px 20px;
          background: #111111;
          border-bottom: 4px solid var(--gold);
        }}
        .top-nav a {{
          color: #ffffff;
          text-decoration: none;
          font-weight: 700;
          padding: 9px 14px;
          border: 1px solid rgba(255, 255, 255, 0.22);
          border-radius: 6px;
        }}
        .top-nav a:hover {{
          background: var(--green);
          border-color: var(--green);
        }}
        .hero {{
          display: grid;
          grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
          gap: 34px;
          align-items: center;
          max-width: 1120px;
          margin: 0 auto;
          padding: 52px 24px 36px;
        }}
        .hero-text {{
          max-width: 680px;
        }}
        .eyebrow {{
          color: var(--red);
          font-size: 0.82rem;
          font-weight: 800;
          letter-spacing: 0;
          margin: 0 0 8px;
          text-transform: uppercase;
        }}
        h1 {{
          font-size: clamp(2rem, 4vw, 4.2rem);
          line-height: 1.05;
          margin: 0 0 18px;
        }}
        h2 {{
          color: var(--green);
          font-size: 1.25rem;
          margin: 0 0 8px;
        }}
        p {{
          margin: 0;
        }}
        .lead {{
          color: var(--muted);
          font-size: 1.12rem;
          max-width: 640px;
        }}
        .actions {{
          display: flex;
          flex-wrap: wrap;
          gap: 12px;
          margin-top: 24px;
        }}
        .button {{
          display: inline-flex;
          align-items: center;
          min-height: 42px;
          color: #ffffff;
          background: var(--green);
          text-decoration: none;
          font-weight: 700;
          padding: 10px 16px;
          border-radius: 6px;
        }}
        .button.secondary {{
          color: var(--ink);
          background: #ffffff;
          border: 1px solid var(--line);
        }}
        .visual-panel {{
          display: grid;
          gap: 16px;
          justify-items: center;
          padding: 20px;
          background: #1b1a17;
          border: 1px solid #000000;
          border-radius: 8px;
          box-shadow: 0 18px 42px rgba(21, 24, 29, 0.18);
        }}
        .visual-panel p {{
          color: #f3ead7;
          font-weight: 700;
          text-align: center;
        }}
        .chessboard {{
          display: grid;
          grid-template-columns: repeat(8, 1fr);
          width: min(100%, 360px);
          aspect-ratio: 1;
          border: 6px solid #111111;
        }}
        .chessboard span {{
          display: grid;
          place-items: center;
          min-width: 0;
          color: #111111;
          font-size: clamp(1.1rem, 4.8vw, 2rem);
          font-weight: 700;
        }}
        .chessboard .light {{ background: var(--light-square); }}
        .chessboard .dark {{ background: var(--dark-square); color: #ffffff; }}
        .section {{
          max-width: 1120px;
          margin: 0 auto;
          padding: 18px 24px 54px;
        }}
        .section-heading {{
          max-width: 760px;
          margin-bottom: 22px;
        }}
        .content-grid {{
          display: grid;
          grid-template-columns: repeat(2, minmax(0, 1fr));
          gap: 18px;
        }}
        .info-card,
        .stat-card,
        .competition-row {{
          background: var(--surface);
          border: 1px solid var(--line);
          border-radius: 8px;
          box-shadow: 0 10px 24px rgba(21, 24, 29, 0.08);
        }}
        .info-card,
        .stat-card {{
          padding: 20px;
        }}
        .stat-grid {{
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 18px;
          margin-top: 28px;
        }}
        .stat-card strong {{
          display: block;
          color: var(--red);
          font-size: 1.8rem;
          line-height: 1;
          margin-bottom: 8px;
        }}
        .competition-list {{
          display: grid;
          gap: 14px;
        }}
        .competition-row {{
          display: flex;
          gap: 16px;
          align-items: center;
          justify-content: space-between;
          padding: 18px 20px;
        }}
        .tag {{
          flex: 0 0 auto;
          color: #ffffff;
          background: var(--red);
          border-radius: 999px;
          font-size: 0.86rem;
          font-weight: 700;
          padding: 8px 12px;
          text-align: center;
        }}
        .note-band {{
          margin-top: 28px;
          padding: 20px;
          color: #ffffff;
          background: var(--green);
          border-radius: 8px;
        }}
        @media (max-width: 780px) {{
          .hero {{
            grid-template-columns: 1fr;
            padding-top: 34px;
          }}
          .content-grid,
          .stat-grid {{
            grid-template-columns: 1fr;
          }}
          .competition-row {{
            align-items: flex-start;
            flex-direction: column;
          }}
          .top-nav {{
            justify-content: flex-start;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="page">
        {navigatie()}
        {continut}
      </div>
    </body>
    </html>
    """


@app.route("/sporturi")
def sporturi():
    """Pagina principala pentru tema sporturi."""
    continut = f"""
    <main>
      <section class="hero">
        <div class="hero-text">
          <p class="eyebrow">Tema: sporturi</p>
          <h1>Sahul, sportul mintii</h1>
          <p class="lead">
            Sahul imbina logica, rabdarea si spiritul competitiv. Fiecare
            partida este o lupta de idei in care planul bun, calculul precis
            si calmul sub presiune conteaza la fel de mult ca talentul.
          </p>
          <div class="actions">
            <a class="button" href="/sporturi/sah">Exploreaza sahul</a>
            <a class="button secondary" href="/sporturi/sah/regulament">Vezi regulamentul</a>
          </div>
        </div>
        <div class="visual-panel">
          {tabla_sah()}
          <p>64 de patrate, posibilitati aproape infinite.</p>
        </div>
      </section>
      <section class="section">
        <div class="section-heading">
          <h2>De ce este sahul un sport?</h2>
          <p>
            In sah exista antrenament, performanta, arbitraj, clasamente,
            turnee si presiune reala de concurs. Este un sport al concentrarii
            si al deciziilor luate in timp limitat.
          </p>
        </div>
        <div class="stat-grid">
          <article class="stat-card">
            <strong>64</strong>
            <p>patrate pe tabla, impartite egal intre campuri deschise si inchise.</p>
          </article>
          <article class="stat-card">
            <strong>32</strong>
            <p>piese la start, fiecare cu rol tactic si valoare strategica.</p>
          </article>
          <article class="stat-card">
            <strong>3</strong>
            <p>rezultate posibile: victorie, remiza sau infrangere.</p>
          </article>
        </div>
      </section>
    </main>
    """
    return pagina("Sporturi | Sah", continut)


@app.route("/sporturi/sah")
def sah():
    """Pagina de prezentare a sahului."""
    continut = f"""
    <main>
      <section class="hero">
        <div class="hero-text">
          <p class="eyebrow">Sport ales: sah</p>
          <h1>Un joc de strategie, timp si curaj</h1>
          <p class="lead">
            O partida buna de sah incepe cu dezvoltarea pieselor, continua cu
            planuri pe termen lung si se decide adesea printr-o combinatie
            tactica aparuta intr-un moment critic.
          </p>
          <div class="actions">
            <a class="button" href="/sporturi/sah/regulament">Regulament</a>
            <a class="button secondary" href="/sporturi/sah/competitii">Competitii</a>
          </div>
        </div>
        <div class="visual-panel">
          {tabla_sah()}
          <p>Deschidere, joc de mijloc, final: fiecare etapa cere alt tip de atentie.</p>
        </div>
      </section>
      <section class="section">
        <div class="content-grid">
          <article class="info-card">
            <h2>Strategie</h2>
            <p>Jucatorii urmaresc centrul, siguranta regelui si activitatea pieselor.</p>
          </article>
          <article class="info-card">
            <h2>Tactica</h2>
            <p>Furculitele, legaturile si atacurile descoperite pot schimba partida rapid.</p>
          </article>
          <article class="info-card">
            <h2>Gestionarea timpului</h2>
            <p>Ceasul de sah transforma fiecare decizie intr-un exercitiu de eficienta.</p>
          </article>
          <article class="info-card">
            <h2>Fair-play</h2>
            <p>Respectul pentru adversar si regulile clare sunt parte din cultura sahului.</p>
          </article>
        </div>
      </section>
    </main>
    """
    return pagina("Sah | Prezentare", continut)


@app.route("/sporturi/sah/regulament")
def regulament():
    """Pagina cu regulamentul sahului."""
    continut = """
    <main>
      <section class="hero">
        <div class="hero-text">
          <p class="eyebrow">Regulament</p>
          <h1>Reguli de baza pentru o partida corecta</h1>
          <p class="lead">
            Regulile sahului definesc miscarea pieselor, situatiile de sah si
            mat, conditiile de remiza si modul in care se termina partida.
          </p>
          <div class="actions">
            <a class="button" href="/sporturi/sah">Inapoi la sah</a>
            <a class="button secondary" href="/sporturi/sah/competitii">Vezi competitii</a>
          </div>
        </div>
        <div class="visual-panel">
          """ + tabla_sah() + """
          <p>Regulile dau forma jocului si fac fiecare partida comparabila.</p>
        </div>
      </section>
      <section class="section">
        """ + genereaza_regulament_sah() + """
        <div class="note-band">
          O mutare este legala doar daca regele propriu nu ramane in sah dupa
          executarea ei.
        </div>
      </section>
    </main>
    """
    return pagina("Sah | Regulament", continut)


@app.route("/sporturi/sah/competitii")
def competitii():
    """Pagina cu competitii de sah."""
    continut = """
    <main>
      <section class="hero">
        <div class="hero-text">
          <p class="eyebrow">Competitii</p>
          <h1>Unde se masoara performanta in sah</h1>
          <p class="lead">
            Sahul are competitii individuale si pe echipe, ritmuri lente sau
            rapide si turnee pentru toate nivelurile de experienta.
          </p>
          <div class="actions">
            <a class="button" href="/sporturi/sah/regulament">Regulament</a>
            <a class="button secondary" href="/sporturi/sah">Inapoi la sah</a>
          </div>
        </div>
        <div class="visual-panel">
          """ + tabla_sah() + """
          <p>Turneele testeaza pregatirea, rezistenta si adaptarea la adversar.</p>
        </div>
      </section>
      <section class="section">
        """ + genereaza_competitii_sah() + """
        <div class="note-band">
          In competitiile oficiale, rezultatele influenteaza ratingul si
          pozitia jucatorului in clasamente.
        </div>
      </section>
    </main>
    """
    return pagina("Sah | Competitii", continut)


@app.route("/")
def index():
    """Redirect spre pagina sporturi."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
