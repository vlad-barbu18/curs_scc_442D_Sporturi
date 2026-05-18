"""
Biblioteca cu cele doua functii pentru elementul ales: tenis de masa.
"""

REGULI = [
    {"regula": "Masa", "descriere": "Masa are dimensiunile 274 x 152.5 cm si este la 76 cm inaltime."},
    {"regula": "Plasa", "descriere": "Plasa are inaltimea de 15.25 cm si imparte masa in doua jumatati egale."},
    {"regula": "Minge", "descriere": "Mingea are diametrul de 40 mm si greutatea de 2.7 g, confectionata din plastic."},
    {"regula": "Punctaj", "descriere": "Setul se joaca pana la 11 puncte, cu diferenta de cel putin 2 puncte."},
    {"regula": "Serviciu", "descriere": "Serviciul se alterneaza la fiecare 2 puncte marcate."},
    {"regula": "Meci", "descriere": "Meciul se joaca la cel mai bun din 7 seturi (primul la 4 seturi castigate)."},
]

CAMPIONI = [
    ("Ma Long", "China", "Campion olimpic 2016 si 2020, considerat cel mai bun jucator din toate timpurile."),
    ("Jan-Ove Waldner", "Suedia", "Supranumit 'Mozart', campion mondial 1989 si 1997, legenda tenisului de masa."),
    ("Zhang Jike", "China", "Campion olimpic 2012, a castigat Grand Slam-ul tenisului de masa in acelasi an."),
    ("Timo Boll", "Germania", "Fost numarul 1 mondial, unul dintre cei mai longevivi jucatori de top din Europa."),
    ("Deng Yaping", "China", "4 medalii de aur olimpice, a dominat tenisul de masa feminin in anii '90."),
]


def reguli_tenis_de_masa():
    """Returneaza HTML cu regulile de baza ale tenisului de masa."""
    html = "<h2>Regulile de baza ale tenisului de masa</h2>"
    for item in REGULI:
        html += f"<p><b>{item['regula']}:</b> {item['descriere']}</p>"
    return html


def campioni_tenis_de_masa():
    """Returneaza HTML cu campionii mondiali la tenis de masa."""
    html = "<h2>Campioni mondiali la tenis de masa</h2><ul>"
    for nume, tara, descriere in CAMPIONI:
        html += f"<li><b>{nume}</b> ({tara}): {descriere}</li>"
    html += "</ul>"
    return html
