"""
Biblioteca cu cele doua functii pentru elementul ales: tir cu arcul.
"""

REGULI = [
    {"regula": "Distanta", "descriere": "Distanta de tragere este 70m (outdoor recurva) sau 18m (indoor)."},
    {"regula": "Tinta", "descriere": "Tinta are diametrul de 122cm outdoor si 40cm indoor, impartita in 10 sectoare."},
    {"regula": "Sageti", "descriere": "Fiecare arcas trage 3 sageti per voleu in meciurile olimpice."},
    {"regula": "Punctaj", "descriere": "Sectoarele valorizeaza 1-10 puncte; centrul (X) aduce 10 puncte."},
    {"regula": "Sistem set", "descriere": "Castigatorul unui set primeste 2 puncte; egalul aduce cate 1 punct fiecaruia."},
    {"regula": "Meci", "descriere": "Meciul se castiga la 6 puncte de set (primul la 6 puncte castiga)."},
]

CAMPIONI = [
    ("Brady Ellison", "SUA", "Multiplu campion mondial la arc recurva, dominatorul ultimului deceniu."),
    ("Kim Woojin", "Coreea de Sud", "Detinator al recordului mondial, campion olimpic si mondial."),
    ("Im Dong-hyun", "Coreea de Sud", "Campion olimpic 2004 si 2008, a stabilit recorduri mondiale la 70m."),
    ("Deepika Kumari", "India", "Multipla campioana mondiala la feminin, numar 1 mondial timp de mai multi ani."),
    ("Yun Mi-jin", "Coreea de Sud", "Campioana olimpica 2000, una dintre cele mai titrate arcase din istorie."),
]


def reguli_tir_cu_arcul():
    """Returneaza HTML cu regulile de baza ale tirului cu arcul."""
    html = "<h2>Regulile de baza ale tirului cu arcul</h2>"
    for item in REGULI:
        html += f"<p><b>{item['regula']}:</b> {item['descriere']}</p>"
    return html


def campioni_tir_cu_arcul():
    """Returneaza HTML cu campionii mondiali la tir cu arcul."""
    html = "<h2>Campioni mondiali la tir cu arcul</h2><ul>"
    for nume, tara, descriere in CAMPIONI:
        html += f"<li><b>{nume}</b> ({tara}): {descriere}</li>"
    html += "</ul>"
    return html
