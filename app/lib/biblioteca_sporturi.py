"""
Continut HTML pentru paginile dedicate sahului.
"""


REGULI_SAH = [
    {
        "titlu": "Obiectiv",
        "descriere": (
            "Scopul jocului este sa dai mat regelui advers, adica sa il "
            "ataci fara ca acesta sa mai poata scapa legal."
        ),
    },
    {
        "titlu": "Mutarea pieselor",
        "descriere": (
            "Regele muta un patrat, dama combina linia si diagonala, tura "
            "merge pe linie, nebunul pe diagonala, calul sare in forma de L, "
            "iar pionul inainteaza spre ultima linie."
        ),
    },
    {
        "titlu": "Sah, mat si remiza",
        "descriere": (
            "Un rege atacat este in sah. Daca nu exista nicio aparare legala, "
            "pozitia este mat. Partida poate fi remiza prin pat, repetare, "
            "material insuficient sau acord."
        ),
    },
    {
        "titlu": "Rocada si promovarea",
        "descriere": (
            "Rocada pune regele la adapost si activeaza tura. Cand un pion "
            "ajunge pe ultima linie, acesta se promoveaza de obicei in dama."
        ),
    },
]


COMPETITII_SAH = [
    {
        "nume": "Campionatul Mondial",
        "format": "Meci intre campionul mondial si challenger",
        "detaliu": "Este varful sahului clasic si pune accent pe pregatire lunga.",
    },
    {
        "nume": "Olimpiada de Sah",
        "format": "Turneu pe echipe nationale",
        "detaliu": "Jucatorii reprezinta tara si aduna puncte pe mai multe mese.",
    },
    {
        "nume": "Turnee open",
        "format": "Sistem elvetian",
        "detaliu": (
            "Participa jucatori cu ratinguri diferite, iar rundele "
            "imperecheaza scoruri apropiate."
        ),
    },
    {
        "nume": "Rapid si blitz",
        "format": "Partide cu timp redus",
        "detaliu": (
            "Deciziile sunt mai rapide, iar tactica si gestionarea timpului "
            "devin esentiale."
        ),
    },
]


def genereaza_regulament_sah() -> str:
    """Returneaza sectiunea HTML cu regulile de baza ale sahului."""
    html = '<section class="content-grid">'
    for regula in REGULI_SAH:
        html += (
            '<article class="info-card">'
            f"<h2>{regula['titlu']}</h2>"
            f"<p>{regula['descriere']}</p>"
            "</article>"
        )
    html += "</section>"
    return html


def genereaza_competitii_sah() -> str:
    """Returneaza sectiunea HTML cu competitii importante de sah."""
    html = '<section class="competition-list">'
    for competitie in COMPETITII_SAH:
        html += (
            '<article class="competition-row">'
            "<div>"
            f"<h2>{competitie['nume']}</h2>"
            f"<p>{competitie['detaliu']}</p>"
            "</div>"
            f'<span class="tag">{competitie["format"]}</span>'
            "</article>"
        )
    html += "</section>"
    return html
