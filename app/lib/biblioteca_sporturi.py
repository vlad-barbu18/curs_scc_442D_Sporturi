"""
Biblioteca cu cele doua functii pentru elementul ales: minifotbal.
Tema: Sporturi
"""

# INFO_1 folosește o listă de dicționare pentru Reguli
INFO_1 = [
    {"regula": "Numar jucatori", "descriere": "Se joaca in format de 5 jucatori de camp si un portar (5+1)."},
    {"regula": "Durata meciului", "descriere": "O partida oficiala are doua reprize a cate 20 sau 25 de minute fiecare."},
    {"regula": "Fara ofsaid", "descriere": "Nu exista regula ofsaidului, ceea ce face jocul foarte rapid si dinamic."},
    {"regula": "Schimbari", "descriere": "Inlocuirile de jucatori sunt nelimitate si se pot face in orice moment."},
]

# INFO_2 folosește o listă de tupluri pentru Echipament
INFO_2 = [
    ("Incaltaminte", "Ghete de tip Turf (TF) cu crampoane mici de cauciuc pentru teren sintetic."),
    ("Protectie", "Aparatorile de tibie sunt recomandate pentru prevenirea accidentarilor."),
    ("Mingea", "Minge speciala marimea 4 sau 5, adaptata pentru suprafete reduse."),
    ("Portar", "Manusi specifice si echipament cu protectie buretata la coate si genunchi."),
]


def functie_1_sport():
    """Functia 1: returneaza HTML formatat cu regulile de minifotbal."""
    html = "<h2>Reguli principale de Minifotbal</h2>"
    for item in INFO_1:
        html += f"<p><b>{item['regula']}</b>: {item['descriere']}</p>"
    return html


def functie_2_sport():
    """Functia 2: returneaza HTML formatat sub forma de lista cu echipamentul."""
    html = "<h2>Echipament necesar pentru Minifotbal</h2><ul>"
    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
