"""
Biblioteca cu cele doua functii pentru elementul ales: sport.
Sport ales: baschet.
"""


INFO_1 = [
    {
        "camp1": "NBA",
        "camp2": "Cea mai cunoscuta competitie de baschet din lume, desfasurata in Statele Unite ale Americii.",
    },
    {
        "camp1": "EuroLeague",
        "camp2": "Una dintre cele mai importante competitii de baschet din Europa, la nivel de cluburi.",
    },
    {
        "camp1": "Campionatul Mondial FIBA",
        "camp2": "Competitie internationala organizata intre echipele nationale de baschet.",
    },
    {
        "camp1": "Jocurile Olimpice",
        "camp2": "Baschetul este inclus ca sport olimpic, fiind disputat intre echipe nationale.",
    },
]


INFO_2 = [
    (
        "Minge de baschet",
        "Este elementul principal al jocului si este folosita pentru pase, dribling si aruncari la cos.",
    ),
    (
        "Cos de baschet",
        "Este format din panou, inel si plasa, iar scopul jocului este introducerea mingii in cos.",
    ),
    (
        "Echipament sportiv",
        "Jucatorii poarta tricou, sort si incaltaminte speciala pentru baschet.",
    ),
    (
        "Pantofi de baschet",
        "Sunt proiectati pentru aderenta, stabilitate si protectia gleznelor in timpul jocului.",
    ),
    (
        "Tabela de scor",
        "Este folosita pentru afisarea punctajului, timpului ramas si a altor informatii despre meci.",
    ),
]


def functie_1_sport():
    """Functia 1: returneaza HTML formatat cu competitii de baschet."""
    html = "<h2>Competitii importante de baschet</h2>"

    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"

    return html


def functie_2_sport():
    """Functia 2: returneaza HTML formatat cu echipamente folosite in baschet."""
    html = "<h2>Echipamente folosite in baschet</h2>"
    html += "<ul>"

    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"

    html += "</ul>"

    return html
