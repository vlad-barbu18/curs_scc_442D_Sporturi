"""
Biblioteca cu cele doua functii pentru elementul ales: biliard.
"""


INFO_GENERALE = [
    {
        "titlu": "Definitie",
        "descriere": "Biliardul este un sport de precizie in care jucatorii lovesc bilele cu un tac.",
    },
    {
        "titlu": "Masa de joc",
        "descriere": "Jocul se desfasoara pe o masa acoperita cu postav, prevazuta de obicei cu buzunare.",
    },
    {
        "titlu": "Scopul jocului",
        "descriere": "Scopul este introducerea bilelor in buzunare conform regulilor variantei jucate.",
    },
]


REGULI_BAZA = [
    (
        "Lovirea bilei albe",
        "Jucatorul loveste bila alba cu tacul pentru a pune in miscare celelalte bile.",
    ),
    (
        "Respectarea randului",
        "Fiecare jucator executa lovituri in functie de regulile jocului si de rezultatul loviturii anterioare.",
    ),
    (
        "Fault",
        "Un fault poate aparea daca bila alba este introdusa in buzunar sau daca nu este atinsa bila corecta.",
    ),
]


def functie_1_biliard():
    """Returneaza informatii generale despre biliard in format HTML."""
    html = "<h2>Informatii generale despre biliard</h2>"
    for item in INFO_GENERALE:
        html += f"<p><b>{item['titlu']}</b>: {item['descriere']}</p>"
    return html


def functie_2_biliard():
    """Returneaza reguli de baza despre biliard in format HTML."""
    html = "<h2>Reguli de baza in biliard</h2><ul>"
    for titlu, descriere in REGULI_BAZA:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
