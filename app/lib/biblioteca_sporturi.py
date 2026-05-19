"""
Biblioteca cu cele doua functii pentru elementul ales: scrima.
"""


INFO_1 = [
    {"camp1": "Origine", "camp2": "Scrima provine din tehnicile de lupta cu sabia."},
    {"camp1": "Tip", "camp2": "Sport olimpic individual si pe echipe."},
]

INFO_2 = [
    ("Floreta", "Arma usoara folosita in competitii tehnice."),
    ("Sabia", "Arma rapida in care se puncteaza cu muchia si varful."),
]


def functie_1_scrima():
    """Functia 1: returneaza HTML formatat cu informatiile."""
    html = "<h2>Informatii generale despre scrima</h2>"
    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"
    return html


def functie_2_scrima():
    """Functia 2: returneaza HTML formatat cu informatiile."""
    html = "<h2>Tipuri de arme in scrima</h2><ul>"
    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
