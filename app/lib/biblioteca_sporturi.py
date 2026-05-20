"""
Biblioteca cu cele doua functii pentru elementul ales: polo.
"""

INFO_1 = [
    {"camp1": "Jucatori", "camp2": "O echipa are 7 jucatori in apa (6 de camp si un portar)."},
    {"camp1": "Durata", "camp2": "Meciul este impartit in 4 reprize a cate 8 minute."},
    {"camp1": "Regula mainii", "camp2": "Jucatorii de camp pot atinge mingea doar cu o singura mana."},
]

INFO_2 = [
    ("Casca", "Obligatorie, protejeaza urechile. Echipele au culori diferite."),
    ("Costum", "Rezistent la trageri, din material special pentru apa."),
    ("Mingea", "Are o textura aderenta, cauciucata, nu aluneca in apa."),
]

def reguli_polo():
    """Functia 1: returneaza HTML formatat cu informatiile despre reguli."""
    html = "<h2>Reguli de baza in Polo</h2>"
    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"
    return html

def echipament_polo():
    """Functia 2: returneaza HTML formatat cu informatiile despre echipament."""
    html = "<h2>Echipament necesar in Polo</h2><ul>"
    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
