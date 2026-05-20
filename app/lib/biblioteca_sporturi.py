"""
Biblioteca proiectului pentru elementul ales: MMA.
Contine doua functii care genereaza continut HTML.
"""


DATE_LUPTATORI = [
    {
        "nume": "Conor McGregor",
        "stil": "Striking",
        "descriere": (
            "luptator cunoscut pentru lovituri precise, carisma "
            "si promovare."
        ),
    },
    {
        "nume": "Khabib Nurmagomedov",
        "stil": "Grappling",
        "descriere": (
            "luptator recunoscut pentru control la sol, wrestling "
            "si dominare tactica."
        ),
    },
    {
        "nume": "Jon Jones",
        "stil": "Complet",
        "descriere": (
            "sportiv apreciat pentru creativitate, distanta, "
            "lovituri variate si adaptare."
        ),
    },
]

DATE_TEHNICI = [
    (
        "Striking",
        "tehnici de lovire cu pumnii, picioarele, genunchii si coatele.",
    ),
    (
        "Grappling",
        "tehnici de proiectare, control si lupta la sol.",
    ),
    (
        "Submissions",
        (
            "procedee prin care adversarul este fortat sa renunte, "
            "precum armbar sau rear naked choke."
        ),
    ),
]


def afiseaza_luptatori_mma():
    """Returneaza o sectiune HTML cu luptatori reprezentativi din MMA."""
    continut_html = """
        <h2>Luptatori reprezentativi</h2>
        <div class="grid">
    """

    for luptator in DATE_LUPTATORI:
        continut_html += f"""
            <div class="stat-card">
              <h3>{luptator['nume']}</h3>
              <p><b>Stil principal:</b> {luptator['stil']}</p>
              <p>{luptator['descriere']}</p>
            </div>
        """

    continut_html += "</div>"

    return continut_html


def afiseaza_tehnici_mma():
    """Returneaza o sectiune HTML cu tehnici importante din MMA."""
    continut_html = """
        <h2>Tehnici importante</h2>
        <div class="grid">
    """

    for tehnica, explicatie in DATE_TEHNICI:
        continut_html += f"""
            <div class="stat-card">
              <h3>{tehnica}</h3>
              <p>{explicatie}</p>
            </div>
        """

    continut_html += "</div>"

    return continut_html