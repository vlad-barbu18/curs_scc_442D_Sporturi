"""Biblioteca pentru cele doua functii publice ale proiectului Sporturi."""

REGULI_VOLEI = [
    "Voleiul se joaca intre doua echipe formate din cate 6 jucatori.",
    "Un set se joaca pana la 25 de puncte.",
    "Este necesara o diferenta de minimum doua puncte pentru castigarea setului.",
    "Fiecare echipa are maximum trei atingeri inainte de a trimite mingea peste fileu.",
    "Jucatorii trebuie sa respecte ordinea rotatiei pe teren.",
]

ECHIPAMENT_VOLEI = [
    ("Mingea de volei", "este usoara si special conceputa pentru pase, servicii si atacuri."),
    ("Genunchierele", "protejeaza genunchii in timpul plonjoanelor."),
    ("Incaltamintea sport", "ofera stabilitate si aderenta pe teren."),
    ("Tricoul si sortul", "asigura libertate de miscare."),
    ("Accesoriile de protectie", "pot include benzi, cotiere sau suporturi pentru glezna."),
]


def reguli_volei():
    """Returneaza HTML formatat cu reguli importante pentru volei."""
    reguli_html = '<h2 style="color:#1d4ed8;">Reguli importante</h2>'
    reguli_html += '<ul style="font-size:18px; line-height:1.8;">'
    for regula in REGULI_VOLEI:
        reguli_html += f"<li>{regula}</li>"
    reguli_html += "</ul>"
    return reguli_html


def echipament_volei():
    """Returneaza HTML formatat cu echipamentele folosite in volei."""
    echipament_html = '<h2 style="color:#1d4ed8;">Echipamente utilizate</h2>'
    echipament_html += '<ul style="font-size:18px; line-height:1.8;">'
    for nume, descriere in ECHIPAMENT_VOLEI:
        echipament_html += f"<li><b>{nume}</b> - {descriere}</li>"
    echipament_html += "</ul>"
    return echipament_html
