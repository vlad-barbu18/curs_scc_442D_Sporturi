"""
Aplicatie Flask pentru tema Sporturi.
Dezvoltator: Mitu Marian
Element ales: MMA.
"""

from flask import Flask, redirect
from app.lib.biblioteca_sporturi import (
    afiseaza_luptatori_mma,
    afiseaza_tehnici_mma,
)

app = Flask(__name__)


def pagina(titlu: str, continut: str) -> str:
    """Creeaza o pagina HTML moderna cu fundal tematic MMA."""
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titlu}</title>

        <style>
          * {{
              box-sizing: border-box;
          }}

          body {{
              margin: 0;
              font-family: Arial, sans-serif;
              color: #f8fafc;
              background:
                  radial-gradient(circle at top left, rgba(239, 68, 68, 0.22), transparent 28%),
                  radial-gradient(circle at bottom right, rgba(59, 130, 246, 0.18), transparent 30%),
                  linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
              min-height: 100vh;
              overflow-x: hidden;
          }}

          .background-scene {{
              position: fixed;
              inset: 0;
              z-index: 0;
              pointer-events: none;
              overflow: hidden;
          }}

          .arena-glow {{
              position: absolute;
              width: 900px;
              height: 900px;
              left: 50%;
              top: 50%;
              transform: translate(-50%, -50%);
              border-radius: 50%;
              background: radial-gradient(
                  circle,
                  rgba(239, 68, 68, 0.12) 0%,
                  rgba(30, 41, 59, 0.08) 35%,
                  transparent 70%
              );
              filter: blur(12px);
          }}

          .ring-wrap {{
              position: absolute;
              left: 50%;
              top: 58%;
              transform: translate(-50%, -50%);
              width: 760px;
              height: 420px;
              opacity: 0.22;
          }}

          .ring-base {{
              position: absolute;
              inset: 0;
              border-radius: 50%;
              background:
                  radial-gradient(circle, rgba(255, 255, 255, 0.10) 0%, rgba(255, 255, 255, 0.03) 48%, transparent 60%);
              border: 2px solid rgba(255, 255, 255, 0.10);
              transform: perspective(900px) rotateX(68deg);
              box-shadow:
                  0 0 0 14px rgba(148, 163, 184, 0.04),
                  0 0 0 28px rgba(148, 163, 184, 0.025);
          }}

          .rope {{
              position: absolute;
              left: 12%;
              right: 12%;
              height: 3px;
              background: rgba(255, 255, 255, 0.18);
              border-radius: 999px;
              transform: perspective(900px) rotateX(68deg);
          }}

          .rope-1 {{ top: 32%; }}
          .rope-2 {{ top: 39%; }}
          .rope-3 {{ top: 46%; }}
          .rope-4 {{ top: 53%; }}

          .post {{
              position: absolute;
              width: 12px;
              height: 120px;
              background: linear-gradient(180deg, rgba(248, 250, 252, 0.35), rgba(148, 163, 184, 0.18));
              border-radius: 12px;
              box-shadow: 0 0 18px rgba(255, 255, 255, 0.08);
          }}

          .post-1 {{ left: 13%; top: 29%; }}
          .post-2 {{ right: 13%; top: 29%; }}
          .post-3 {{ left: 13%; top: 49%; }}
          .post-4 {{ right: 13%; top: 49%; }}

          .fighter,
          .center-fighter {{
              position: absolute;
              width: 82px;
              height: 160px;
          }}

          .fighter .head,
          .center-fighter .head {{
              position: absolute;
              width: 28px;
              height: 28px;
              border-radius: 50%;
              background: rgba(255, 255, 255, 0.20);
              left: 27px;
              top: 0;
          }}

          .fighter .body,
          .center-fighter .body {{
              position: absolute;
              width: 18px;
              height: 56px;
              background: rgba(255, 255, 255, 0.20);
              left: 32px;
              top: 28px;
              border-radius: 12px;
          }}

          .fighter .arm-left,
          .fighter .arm-right,
          .center-fighter .arm-left,
          .center-fighter .arm-right {{
              position: absolute;
              width: 14px;
              height: 54px;
              background: rgba(255, 255, 255, 0.16);
              top: 34px;
              border-radius: 12px;
              transform-origin: top center;
          }}

          .fighter .arm-left,
          .center-fighter .arm-left {{
              left: 20px;
              transform: rotate(32deg);
          }}

          .fighter .arm-right,
          .center-fighter .arm-right {{
              right: 20px;
              transform: rotate(-32deg);
          }}

          .fighter .leg-left,
          .fighter .leg-right,
          .center-fighter .leg-left,
          .center-fighter .leg-right {{
              position: absolute;
              width: 14px;
              height: 62px;
              background: rgba(255, 255, 255, 0.16);
              top: 78px;
              border-radius: 12px;
              transform-origin: top center;
          }}

          .fighter .leg-left,
          .center-fighter .leg-left {{
              left: 28px;
              transform: rotate(14deg);
          }}

          .fighter .leg-right,
          .center-fighter .leg-right {{
              right: 28px;
              transform: rotate(-14deg);
          }}

          .corner-fighter {{
              opacity: 0.16;
              transform: scale(1.15);
          }}

          .corner-top-left {{
              top: 80px;
              left: 42px;
          }}

          .corner-top-right {{
              top: 80px;
              right: 42px;
              transform: scale(1.15) scaleX(-1);
          }}

          .corner-bottom-left {{
              bottom: 70px;
              left: 42px;
          }}

          .corner-bottom-right {{
              bottom: 70px;
              right: 42px;
              transform: scale(1.15) scaleX(-1);
          }}

          .center-fighter {{
              opacity: 0.22;
              top: 110px;
          }}

          .center-left {{
              left: 250px;
              transform: scale(1.05);
          }}

          .center-right {{
              right: 250px;
              transform: scale(1.05) scaleX(-1);
          }}

          .page {{
              position: relative;
              z-index: 1;
              width: 100%;
              min-height: 100vh;
              padding: 24px;
          }}

          .container {{
              max-width: 1100px;
              margin: 0 auto;
          }}

          .navbar {{
              display: flex;
              justify-content: space-between;
              align-items: center;
              gap: 16px;
              padding: 18px 22px;
              margin-bottom: 28px;
              background: rgba(15, 23, 42, 0.84);
              border: 1px solid rgba(148, 163, 184, 0.24);
              border-radius: 22px;
              box-shadow: 0 20px 45px rgba(0, 0, 0, 0.28);
              backdrop-filter: blur(8px);
          }}

          .logo {{
              font-size: 22px;
              font-weight: 900;
              letter-spacing: 1px;
          }}

          .logo span {{
              color: #ef4444;
          }}

          .nav-links {{
              display: flex;
              flex-wrap: wrap;
              justify-content: flex-end;
              gap: 10px;
          }}

          .nav-links a,
          .btn {{
              color: #f8fafc;
              background: rgba(255, 255, 255, 0.08);
              border: 1px solid rgba(255, 255, 255, 0.14);
              padding: 10px 14px;
              border-radius: 999px;
              text-decoration: none;
              font-weight: 700;
              font-size: 14px;
              transition: 0.2s ease;
              display: inline-block;
              backdrop-filter: blur(6px);
          }}

          .nav-links a:hover,
          .btn:hover {{
              background: #ef4444;
              border-color: #ef4444;
              transform: translateY(-2px);
          }}

          .hero {{
              display: grid;
              grid-template-columns: 1.2fr 0.8fr;
              gap: 24px;
              align-items: stretch;
              margin-bottom: 24px;
          }}

          .hero-card,
          .content-card,
          .stat-card {{
              background: rgba(15, 23, 42, 0.82);
              border: 1px solid rgba(148, 163, 184, 0.22);
              border-radius: 28px;
              box-shadow: 0 22px 55px rgba(0, 0, 0, 0.35);
              backdrop-filter: blur(10px);
          }}

          .hero-card {{
              padding: 42px;
          }}

          .side-card {{
              padding: 28px;
              display: flex;
              flex-direction: column;
              justify-content: center;
              background:
                  linear-gradient(160deg, rgba(239, 68, 68, 0.90), rgba(124, 45, 18, 0.82)),
                  rgba(15, 23, 42, 0.9);
              border-radius: 28px;
              box-shadow: 0 22px 55px rgba(0, 0, 0, 0.35);
              backdrop-filter: blur(10px);
          }}

          .badge {{
              display: inline-block;
              width: fit-content;
              padding: 8px 12px;
              margin-bottom: 16px;
              border-radius: 999px;
              background: rgba(239, 68, 68, 0.18);
              border: 1px solid rgba(248, 113, 113, 0.4);
              color: #fecaca;
              font-size: 13px;
              font-weight: 800;
              letter-spacing: 0.5px;
              text-transform: uppercase;
          }}

          h1 {{
              margin: 0 0 16px;
              font-size: 46px;
              line-height: 1.05;
              letter-spacing: -1px;
          }}

          h2 {{
              margin-top: 0;
              color: #fca5a5;
              font-size: 26px;
          }}

          h3 {{
              color: #ffffff;
              margin-bottom: 8px;
          }}

          p {{
              color: #cbd5e1;
              line-height: 1.75;
              font-size: 17px;
          }}

          b {{
              color: #ffffff;
          }}

          .content-card {{
              padding: 30px;
              margin-bottom: 24px;
          }}

          .grid {{
              display: grid;
              grid-template-columns: repeat(3, 1fr);
              gap: 18px;
              margin: 24px 0;
          }}

          .stat-card {{
              padding: 22px;
          }}

          ul {{
              padding-left: 20px;
          }}

          li {{
              color: #dbeafe;
              margin: 10px 0;
              line-height: 1.6;
          }}

          .actions {{
              display: flex;
              flex-wrap: wrap;
              gap: 10px;
              margin-top: 22px;
          }}

          .btn-primary {{
              background: #ef4444;
              border-color: #ef4444;
          }}

          .btn-primary:hover {{
              background: #dc2626;
          }}

          @media (max-width: 1100px) {{
              .ring-wrap {{
                  width: 620px;
                  height: 360px;
              }}

              .center-left {{
                  left: 200px;
              }}

              .center-right {{
                  right: 200px;
              }}
          }}

          @media (max-width: 850px) {{
              .navbar {{
                  flex-direction: column;
                  align-items: flex-start;
              }}

              .nav-links {{
                  justify-content: flex-start;
              }}

              .hero {{
                  grid-template-columns: 1fr;
              }}

              .grid {{
                  grid-template-columns: 1fr;
              }}

              h1 {{
                  font-size: 36px;
              }}

              .page {{
                  padding: 14px;
              }}

              .hero-card,
              .content-card,
              .side-card {{
                  padding: 24px;
              }}

              .ring-wrap {{
                  width: 480px;
                  height: 280px;
                  top: 62%;
              }}

              .center-left {{
                  left: 140px;
              }}

              .center-right {{
                  right: 140px;
              }}

              .corner-fighter {{
                  opacity: 0.12;
                  transform: scale(0.95);
              }}

              .corner-top-right {{
                  transform: scale(0.95) scaleX(-1);
              }}

              .corner-bottom-right {{
                  transform: scale(0.95) scaleX(-1);
              }}
          }}

          @media (max-width: 560px) {{
              .ring-wrap {{
                  width: 360px;
                  height: 220px;
              }}

              .center-fighter {{
                  display: none;
              }}

              .corner-fighter {{
                  opacity: 0.08;
              }}
          }}
        </style>
      </head>

      <body>
        <div class="background-scene">
          <div class="arena-glow"></div>

          <div class="ring-wrap">
            <div class="ring-base"></div>

            <div class="rope rope-1"></div>
            <div class="rope rope-2"></div>
            <div class="rope rope-3"></div>
            <div class="rope rope-4"></div>

            <div class="post post-1"></div>
            <div class="post post-2"></div>
            <div class="post post-3"></div>
            <div class="post post-4"></div>

            <div class="center-fighter center-left">
              <div class="head"></div>
              <div class="body"></div>
              <div class="arm-left"></div>
              <div class="arm-right"></div>
              <div class="leg-left"></div>
              <div class="leg-right"></div>
            </div>

            <div class="center-fighter center-right">
              <div class="head"></div>
              <div class="body"></div>
              <div class="arm-left"></div>
              <div class="arm-right"></div>
              <div class="leg-left"></div>
              <div class="leg-right"></div>
            </div>
          </div>

          <div class="fighter corner-fighter corner-top-left">
            <div class="head"></div>
            <div class="body"></div>
            <div class="arm-left"></div>
            <div class="arm-right"></div>
            <div class="leg-left"></div>
            <div class="leg-right"></div>
          </div>

          <div class="fighter corner-fighter corner-top-right">
            <div class="head"></div>
            <div class="body"></div>
            <div class="arm-left"></div>
            <div class="arm-right"></div>
            <div class="leg-left"></div>
            <div class="leg-right"></div>
          </div>

          <div class="fighter corner-fighter corner-bottom-left">
            <div class="head"></div>
            <div class="body"></div>
            <div class="arm-left"></div>
            <div class="arm-right"></div>
            <div class="leg-left"></div>
            <div class="leg-right"></div>
          </div>

          <div class="fighter corner-fighter corner-bottom-right">
            <div class="head"></div>
            <div class="body"></div>
            <div class="arm-left"></div>
            <div class="arm-right"></div>
            <div class="leg-left"></div>
            <div class="leg-right"></div>
          </div>
        </div>

        <div class="page">
          <div class="container">
            <nav class="navbar">
              <div class="logo">SPORTURI<span>.</span>MMA</div>

              <div class="nav-links">
                <a href="/sporturi">Acasa</a>
                <a href="/sporturi/mma">MMA</a>
                <a href="/sporturi/mma/afiseaza_luptatori_mma">Luptatori</a>
                <a href="/sporturi/mma/afiseaza_tehnici_mma">Tehnici</a>
                <a href="/sporturi/mma/reguli">Reguli</a>
              </div>
            </nav>

            {continut}
          </div>
        </div>
      </body>
    </html>
    """


@app.route("/sporturi")
def sporturi():
    """Pagina principala a temei."""
    continut = """
        <section class="hero">
          <div class="hero-card">
            <span class="badge">Proiect Flask</span>
            <h1>Sporturi moderne si spectaculoase</h1>

            <p>
              Tema proiectului este <b>sporturi</b>, iar elementul ales
              pentru implementare este <b>MMA</b>.
            </p>

            <p>
              Site-ul prezinta informatii despre MMA, luptatori cunoscuti,
              tehnici folosite si cateva reguli de baza.
            </p>

            <div class="actions">
              <a class="btn btn-primary" href="/sporturi/mma">Descopera MMA</a>
              <a class="btn" href="/sporturi/mma/reguli">Vezi regulile</a>
            </div>
          </div>

          <div class="side-card">
            <span class="badge">Mixed Martial Arts</span>
            <h2>Box + Wrestling + Jiu-Jitsu + Strategie</h2>
            <p>
              MMA combina mai multe discipline de lupta si pune accent pe
              pregatire fizica, tehnica, disciplina si adaptare.
            </p>
          </div>
        </section>
    """
    return pagina("Sporturi - MMA", continut)


@app.route("/sporturi/mma")
def mma():
    """Pagina elementului ales."""
    continut = """
        <section class="hero">
          <div class="hero-card">
            <span class="badge">Element ales</span>
            <h1>MMA</h1>

            <p>
              MMA este un sport de contact in care sportivii folosesc tehnici
              de lupta in picioare si la sol.
            </p>

            <p>
              Este considerat unul dintre cele mai complexe sporturi deoarece
              combina lovituri, proiectari, control la sol si strategie.
            </p>

            <p>
              Am ales MMA deoarece este un sport modern, spectaculos si dificil,
              care necesita disciplina, rezistenta, curaj si pregatire continua.
            </p>

            <div class="actions">
              <a class="btn btn-primary" href="/sporturi/mma/afiseaza_luptatori_mma">Luptatori MMA</a>
              <a class="btn" href="/sporturi/mma/afiseaza_tehnici_mma">Tehnici MMA</a>
              <a class="btn" href="/sporturi/mma/reguli">Reguli de baza</a>
              <a class="btn" href="/sporturi">Inapoi la sporturi</a>
            </div>
          </div>

          <div class="side-card">
            <h2>De ce este MMA interesant?</h2>
            <p>
              Un luptator de MMA trebuie sa fie bun atat in striking,
              cat si in grappling. Nu este suficienta forta, ci conteaza
              tehnica, viteza de reactie si planul de lupta.
            </p>
          </div>
        </section>
    """
    return pagina("MMA", continut)


@app.route("/sporturi/mma/afiseaza_luptatori_mma")
def ruta_luptatori_mma():
    """Ruta pentru prima functie din biblioteca: luptatori MMA."""
    continut = """
        <section class="content-card">
          <span class="badge">Informatia 1</span>
          <h1>Luptatori MMA</h1>

          <p>
            Aceasta pagina prezinta cativa luptatori cunoscuti din MMA si
            stilurile prin care au devenit celebri.
          </p>
    """

    continut += afiseaza_luptatori_mma()

    continut += """
          <div class="actions">
            <a class="btn btn-primary" href="/sporturi/mma">Inapoi la MMA</a>
            <a class="btn" href="/sporturi/mma/afiseaza_tehnici_mma">Vezi tehnici</a>
            <a class="btn" href="/sporturi">Acasa</a>
          </div>
        </section>
    """

    return pagina("Luptatori MMA", continut)


@app.route("/sporturi/mma/afiseaza_tehnici_mma")
def ruta_tehnici_mma():
    """Ruta pentru a doua functie din biblioteca: tehnici MMA."""
    continut = """
        <section class="content-card">
          <span class="badge">Informatia 2</span>
          <h1>Tehnici MMA</h1>

          <p>
            Aceasta pagina prezinta cateva tehnici importante folosite in MMA.
            Un sportiv complet trebuie sa poata lupta atat in picioare,
            cat si la sol.
          </p>
    """

    continut += afiseaza_tehnici_mma()

    continut += """
          <div class="actions">
            <a class="btn btn-primary" href="/sporturi/mma">Inapoi la MMA</a>
            <a class="btn" href="/sporturi/mma/afiseaza_luptatori_mma">Vezi luptatori</a>
            <a class="btn" href="/sporturi">Acasa</a>
          </div>
        </section>
    """

    return pagina("Tehnici MMA", continut)


@app.route("/sporturi/mma/reguli")
def reguli_mma():
    """Pagina suplimentara cu reguli de baza in MMA."""
    continut = """
        <section class="content-card">
          <span class="badge">Pagina noua</span>
          <h1>Reguli de baza in MMA</h1>

          <p>
            MMA este un sport dur, dar organizat dupa reguli clare.
            Regulile exista pentru siguranta sportivilor si pentru
            desfasurarea corecta a meciurilor.
          </p>

          <div class="grid">
            <div class="stat-card">
              <h3>Runde</h3>
              <p>
                Meciurile sunt impartite in runde. In general, un meci normal
                are 3 runde, iar un meci important poate avea 5 runde.
              </p>
            </div>

            <div class="stat-card">
              <h3>Arbitru</h3>
              <p>
                Arbitrul poate opri lupta daca un sportiv nu se mai poate apara
                sau daca exista un risc mare de accidentare.
              </p>
            </div>

            <div class="stat-card">
              <h3>Fair-play</h3>
              <p>
                Sunt interzise loviturile ilegale si comportamentul nesportiv.
                Luptatorii trebuie sa respecte adversarul si decizia arbitrului.
              </p>
            </div>
          </div>

          <div class="actions">
            <a class="btn btn-primary" href="/sporturi/mma">Inapoi la MMA</a>
            <a class="btn" href="/sporturi/mma/afiseaza_luptatori_mma">Luptatori</a>
            <a class="btn" href="/sporturi/mma/afiseaza_tehnici_mma">Tehnici</a>
            <a class="btn" href="/sporturi">Acasa</a>
          </div>
        </section>
    """

    return pagina("Reguli MMA", continut)


@app.route("/")
def index():
    """Redirect spre pagina principala a temei."""
    return redirect("/sporturi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)