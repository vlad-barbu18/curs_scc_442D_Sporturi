"""
Biblioteca cu cele doua functii pentru tema badminton.
"""


INFO_REGULI_BADMINTON = [
    {
        "regula": "Serviciul",
        "descriere": "Serviciul se executa diagonal, dintr-un careu de serviciu catre careul opus.",
    },
    {
        "regula": "Fluturasul",
        "descriere": "Fluturasul trebuie lovit peste fileu si trebuie sa cada in terenul advers.",
    },
    {
        "regula": "Punctajul",
        "descriere": "Un set se joaca de obicei pana la 21 de puncte, cu diferenta de cel putin doua puncte.",
    },
    {
        "regula": "Fileul",
        "descriere": "Jucatorii nu au voie sa atinga fileul cu racheta sau corpul in timpul schimbului.",
    },
]


INFO_ECHIPAMENT_BADMINTON = [
    ("Racheta", "Racheta de badminton este usoara si permite lovituri rapide si precise."),
    ("Fluturasul", "Fluturasul poate fi realizat din pene naturale sau material sintetic."),
    ("Fileul", "Fileul separa cele doua jumatati ale terenului."),
    ("Incaltamintea", "Jucatorii folosesc incaltaminte sport cu aderenta buna pentru miscari rapide."),
    ("Terenul", "Terenul este delimitat diferit pentru joc simplu si joc de dublu."),
]


def reguli_badminton():
    """Functia 1: returneaza HTML formatat cu reguli de baza din badminton."""
    html = "<h2>Reguli de baza in badminton</h2>"

    for item in INFO_REGULI_BADMINTON:
        html += f"<p><b>{item['regula']}</b>: {item['descriere']}</p>"

    return html


def echipament_badminton():
    """Functia 2: returneaza HTML formatat cu echipamentul folosit in badminton."""
    html = "<h2>Echipament folosit in badminton</h2><ul>"

    for titlu, descriere in INFO_ECHIPAMENT_BADMINTON:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"

    html += "</ul>"
    return html
