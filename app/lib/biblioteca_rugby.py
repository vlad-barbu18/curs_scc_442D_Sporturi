"""
Biblioteca pentru elementul ales: rugby.
"""


INFO_REGULI_RUGBY = [
    {
        "regula": "Pasele",
        "descriere": "In rugby, mingea poate fi pasata doar inapoi sau lateral, nu inainte.",
    },
    {
        "regula": "Eseul",
        "descriere": "Un eseu este inscris atunci cand mingea este culcata in terenul de tinta al adversarului.",
    },
    {
        "regula": "Placajul",
        "descriere": "Placajul este permis doar asupra jucatorului care are mingea.",
    },
    {
        "regula": "Lovitura de pedeapsa",
        "descriere": "O echipa poate obtine puncte printr-o lovitura de pedeapsa executata printre buturi.",
    },
]


INFO_ECHIPAMENT_RUGBY = [
    ("Mingea", "Mingea de rugby are forma ovala si este diferita de mingea folosita in fotbal."),
    ("Tricou", "Jucatorii poarta tricouri rezistente, adaptate contactului fizic intens."),
    ("Ghete", "Ghetele de rugby au crampoane pentru aderenta mai buna pe teren."),
    ("Protectie dentara", "Protectia dentara este folosita pentru reducerea riscului de accidentari."),
    ("Terenul", "Terenul de rugby include zona de joc si terenurile de tinta pentru inscrierea eseurilor."),
]


def reguli_rugby():
    """Returneaza HTML cu reguli de baza din rugby."""
    html = "<h2>Reguli de baza in rugby</h2>"

    for item in INFO_REGULI_RUGBY:
        html += f"<p><b>{item['regula']}</b>: {item['descriere']}</p>"

    return html


def echipament_rugby():
    """Returneaza HTML cu informatii despre echipamentul folosit in rugby."""
    html = "<h2>Echipament folosit in rugby</h2><ul>"

    for titlu, descriere in INFO_ECHIPAMENT_RUGBY:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"

    html += "</ul>"
    return html
