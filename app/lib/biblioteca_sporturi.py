"""
Biblioteca cu cele doua functii pentru elementul ales: tenis de camp.
"""

INFO_1 = [
    {
        "camp1": "Definitie",
        "camp2": "Tenisul de camp este un sport practicat intre doi jucatori sau doua echipe de cate doi jucatori."
    },
    {
        "camp1": "Scop",
        "camp2": "Scopul jocului este trimiterea mingii peste fileu astfel incat adversarul sa nu o poata returna corect."
    },
    {
        "camp1": "Echipament",
        "camp2": "Pentru tenis sunt necesare racheta, mingi speciale, fileu si teren marcat."
    },
]

INFO_2 = [
    (
        "Serviciul",
        "Serviciul este lovitura prin care incepe fiecare punct. Jucatorul trebuie sa trimita mingea in careul de serviciu advers."
    ),
    (
        "Forehand",
        "Forehand-ul este una dintre cele mai folosite lovituri si se executa de pe partea dominanta a jucatorului."
    ),
    (
        "Backhand",
        "Backhand-ul este lovitura executata de pe partea opusa mainii dominante."
    ),
]


def functie_1_tenis():
    """Functia 1: returneaza HTML formatat cu informatii generale despre tenis."""
    html = "<h2>Informatii generale despre tenis de camp</h2>"

    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"

    return html


def functie_2_tenis():
    """Functia 2: returneaza HTML formatat cu tehnici importante din tenis."""
    html = "<h2>Tehnici importante in tenis de camp</h2>"
    html += "<ul>"

    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"

    html += "</ul>"

    return html