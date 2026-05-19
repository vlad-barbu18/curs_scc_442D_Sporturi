"""
Biblioteca cu cele doua functii pentru elementul ales: scrima.
"""


INFO_1 = [
    {"camp1": "Origine", "camp2": "Scrima provine din tehnicile de lupta cu sabia practicate încă din Antichitate și Evul Mediu."},
    {"camp1": "Tip", "camp2": "Sport olimpic individual tehnic si tactic deoarece pune accent pe viteza, precizie, coordonare si strategie."},
]

INFO_2 = [
    ("Floreta", "Arma usoara folosita in competitii tehnice."),
    ("Sabia", "Arma rapida in care se puncteaza cu muchia si varful."),
    ("Spada", "Arma mai grea decat flotanta unde intreaga suprafata a corpului este zona valida pentru punctaj"),
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

    html += '<div style="text-align: center;">'
    html += '<img src="https://patranescu.wordpress.com/wp-content/uploads/2011/04/arme_scrima.gif" width="400" style="border-radius: 12px; margin-top: 20px;">' 
    html += '</div>'

    return html
