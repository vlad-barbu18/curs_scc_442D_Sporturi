"""
Biblioteca cu cele doua functii pentru elementul ales: biatlon.
"""


INFO_1 = [
    {
        "camp1": "Descriere",
        "camp2": "Biatlonul este un sport de iarna care combina schiul fond cu tirul sportiv.",
    },
    {
        "camp1": "Origine",
        "camp2": "Sportul provine din exercitii militare nordice, unde soldatii se deplasau pe schiuri si trageau la tinta.",
    },
    {
        "camp1": "Scop",
        "camp2": "Sportivii trebuie sa parcurga traseul cat mai rapid si sa aiba precizie la sesiunile de tragere.",
    },
]

INFO_2 = [
    ("Schi fond", "Partea de rezistenta, unde sportivii se deplaseaza rapid pe zapada."),
    ("Tir sportiv", "Partea de precizie, unde sportivii trag la tinte aflate la distanta."),
    ("Penalizari", "Pentru tintele ratate se primesc ture suplimentare sau timp adaugat."),
    ("Competitii", "Biatlonul este prezent la Jocurile Olimpice de Iarna si la Campionatele Mondiale."),
]


def functie_1_biatlon():
    """Functia 1: returneaza HTML formatat cu descrierea biatlonului."""
    html = """
    <h2>Introducere despre sporturi</h2>
    <p>
        Sporturile reprezinta activitati fizice organizate, practicate individual sau in echipa,
        care dezvolta rezistenta, disciplina, coordonarea si spiritul competitiv.
        Acestea pot fi sporturi de vara, sporturi de iarna, sporturi individuale sau sporturi de echipa.
    </p>

    <h2>Biatlon</h2>
    <p>
        Biatlonul este un sport de iarna complex, deoarece combina doua abilitati foarte diferite:
        efortul fizic intens din schiul fond si concentrarea necesara pentru tirul sportiv.
        Dupa o portiune de schi, sportivul trebuie sa isi controleze respiratia si pulsul pentru a trage precis la tinta.
    </p>

   

    <h2>Informatii principale</h2>
    """

    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"

    return html


def functie_2_biatlon():
    """Functia 2: returneaza HTML formatat cu elementele importante ale biatlonului."""
    html = """
    <h2>Elemente importante in biatlon</h2>
    <p>
        Biatlonul este considerat un sport dificil deoarece sportivul trebuie sa alterneze
        intre viteza, anduranta si precizie. O greseala mica la tragere poate schimba rezultatul final.
    </p>
    <ul>
    """

    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"

    html += """
    </ul>

    <h2>De ce este biatlonul interesant?</h2>
    <p>
        Acest sport este spectaculos deoarece imbina strategia cu performanta fizica.
        Sportivii trebuie sa decida ritmul de deplasare, sa gestioneze oboseala si sa ramana calmi
        in momentele de tragere.
    </p>
    """

    return html
