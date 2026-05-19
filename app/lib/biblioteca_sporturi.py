"""Fragmente HTML pentru paginile detaliate despre box."""

ECHIPAMENTE_BOX = [
    {
        "nume": "Manusi de box",
        "descriere": "Sunt piesa centrala a echipamentului si se aleg dupa marime, "
        "greutate si tipul antrenamentului.",
        "nevoie": "Protejeaza pumnii sportivului si reduc impactul primit de adversar.",
    },
    {
        "nume": "Bandaje pentru maini",
        "descriere": "Se infasoara pe incheieturi, palma si degete inainte de manusi.",
        "nevoie": "Stabilizeaza articulatiile si scad riscul de entorse sau lovituri "
        "dureroase la incheietura.",
    },
    {
        "nume": "Protectie dentara",
        "descriere": "Este o piesa mulata pe dinti, folosita la sparring si competitii.",
        "nevoie": "Protejeaza dintii, maxilarul si reduce socul loviturilor primite.",
    },
    {
        "nume": "Casca de protectie",
        "descriere": "Acopera fruntea, obrajii si partile laterale ale capului.",
        "nevoie": "Este folosita mai ales la antrenamente pentru a limita taieturile "
        "si loviturile accidentale.",
    },
    {
        "nume": "Incaltaminte de box",
        "descriere": "Ghetele sunt usoare, cu talpa subtire si aderenta buna pe ring.",
        "nevoie": "Ajuta la deplasare rapida, pivotare si stabilitate in schimburile "
        "de lovituri.",
    },
    {
        "nume": "Sac de box si palmare",
        "descriere": "Sunt folosite pentru exersarea loviturilor, preciziei si ritmului.",
        "nevoie": "Permit antrenarea tehnicii fara contact direct cu un adversar.",
    },
]

COMPETITII_BOX = [
    {
        "nume": "Jocurile Olimpice",
        "categorie": "box amator",
        "descriere": "Cel mai cunoscut nivel international pentru boxul olimpic.",
    },
    {
        "nume": "Campionatele Mondiale",
        "categorie": "box amator",
        "descriere": "Reunesc sportivi din multe tari si stabilesc campioni mondiali "
        "pe categorii de greutate.",
    },
    {
        "nume": "Campionatele Europene",
        "categorie": "box amator",
        "descriere": "Competitii continentale importante pentru sportivii europeni.",
    },
    {
        "nume": "Campionatele Nationale",
        "categorie": "box amator",
        "descriere": "Nivelul principal de selectie si afirmare pentru sportivii "
        "din fiecare tara.",
    },
    {
        "nume": "Cupa Romaniei si turnee locale",
        "categorie": "box amator",
        "descriere": "Competitii utile pentru experienta, clasament si selectie.",
    },
    {
        "nume": "Turnee de club, scolare si universitare",
        "categorie": "box de formare",
        "descriere": "Sunt potrivite pentru juniori si sportivi aflati la inceput.",
    },
    {
        "nume": "Gale profesioniste",
        "categorie": "box profesionist",
        "descriere": "Evenimente in care boxerii lupta pe baza de contract si palmares.",
    },
    {
        "nume": "Titluri WBC, WBA, IBF si WBO",
        "categorie": "box profesionist",
        "descriere": "Organizatii majore care acorda centuri mondiale la profesionisti.",
    },
]


def _card(titlu: str, eticheta: str, descriere: str, detaliu: str) -> str:
    """Construieste un card HTML reutilizabil."""
    return f"""
    <article class="info-card">
      <p class="card-label">{eticheta}</p>
      <h3>{titlu}</h3>
      <p>{descriere}</p>
      <p class="card-detail">{detaliu}</p>
    </article>
    """


def echipament_box() -> str:
    """Returneaza lista de echipamente folosite in box."""
    html = """
    <section class="content-section">
      <div class="section-heading">
        <p class="eyebrow">Echipament</p>
        <h2>Echipamentul esential pentru box</h2>
        <p>
          In box, echipamentul nu este doar accesoriu. Fiecare piesa ajuta
          sportivul sa se antreneze corect, sa loveasca eficient si sa reduca
          riscul de accidentare.
        </p>
      </div>
      <div class="card-grid">
    """
    for item in ECHIPAMENTE_BOX:
        html += _card(
            item["nume"],
            "necesar in antrenament",
            item["descriere"],
            item["nevoie"],
        )
    html += """
      </div>
    </section>
    """
    return html


def competitii_box() -> str:
    """Returneaza competitiile disponibile pentru box."""
    html = """
    <section class="content-section">
      <div class="section-heading">
        <p class="eyebrow">Competitii</p>
        <h2>Competitii disponibile in box</h2>
        <p>
          Boxul are trasee competitionale pentru incepatori, sportivi amatori
          si profesionisti. Competitiile sunt organizate de obicei pe categorii
          de varsta, sex si greutate.
        </p>
      </div>
      <div class="timeline-list">
    """
    for index, competitie in enumerate(COMPETITII_BOX, start=1):
        html += f"""
        <article class="timeline-item">
          <span>{index:02d}</span>
          <div>
            <p class="card-label">{competitie["categorie"]}</p>
            <h3>{competitie["nume"]}</h3>
            <p>{competitie["descriere"]}</p>
          </div>
        </article>
        """
    html += """
      </div>
    </section>
    """
    return html
