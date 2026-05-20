"""
Biblioteca cu cele doua functii pentru elementul ales: sport.
"""


INFO_1 = [
    {"camp1": "valoare1", "camp2": "descriere1"},
    {"camp1": "valoare2", "camp2": "descriere2"},
]

INFO_2 = [
    ("titlu1", "descriere1"),
    ("titlu2", "descriere2"),
]


def functie_1_sport():
    """Functia 1: returneaza HTML formatat cu informatiile."""
    html = "<h2>Titlul informatiei 1</h2>"
    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"
    return html


def functie_2_sport():
    """Functia 2: returneaza HTML formatat cu informatiile."""
    html = "<h2>Titlul informatiei 2</h2><ul>"
    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
