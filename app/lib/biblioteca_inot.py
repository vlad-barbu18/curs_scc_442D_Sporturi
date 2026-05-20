"""
Biblioteca cu cele doua functii pentru elementul ales: inot.

Functiile returneaza HTML formatat cu informatii despre:
- Concursuri internationale de inot
- Inotatori profesionisti de top
"""

CONCURSURI = [
    {
        "nume": "Jocurile Olimpice",
        "imagine": "olympics.jpg",
        "organizator": "Comitetul International Olimpic (CIO)",
        "frecventa": "o data la 4 ani",
        "descriere": (
            "Cea mai importanta competitie sportiva internationala. "
            "Inotul este prezent din 1896 (Atena). "
            "Probele se desfasoara in bazin de 50m."
        ),
    },
    {
        "nume": "Campionatele Mondiale",
        "imagine": "mondiale.jpg",
        "organizator": "World Aquatics (fosta FINA)",
        "frecventa": "o data la 2 ani",
        "descriere": (
            "Cea mai prestigioasa competitie anuala dupa Jocurile Olimpice. "
            "Reuneste cei mai buni inotatori din toate continentele."
        ),
    },
    {
        "nume": "Campionatele Europene",
        "imagine": "europene.jpg",
        "organizator": "LEN (Ligue Europeenne de Natation)",
        "frecventa": "o data la 2 ani",
        "descriere": (
            "Principala competitie continentala. Are forme atat in bazin de 50m, "
            "cat si in bazin scurt (25m), reunind toate tarile europene."
        ),
    },
    {
        "nume": "FINA World Cup",
        "imagine": "fina_cup.jpg",
        "organizator": "World Aquatics",
        "frecventa": "anual (mai multe etape)",
        "descriere": (
            "Circuit international cu mai multe etape pe an. "
            "Inotatorii acumuleaza puncte si premii in bani."
        ),
    },
    {
        "nume": "Universiada",
        "imagine": "universiade.jpg",
        "organizator": "FISU",
        "frecventa": "o data la 2 ani",
        "descriere": (
            "Competitia mondiala pentru studenti-sportivi. "
            "Multi campioni olimpici au inceput sa se afirme aici."
        ),
    },
]

INOTATORI = [
    {
        "nume": "Michael Phelps",
        "imagine": "phelps.jpg",
        "tara": "Statele Unite",
        "probe": "fluture, mix individual, liber",
        "descriere": (
            "Cel mai medaliat sportiv olimpic din istorie, cu 28 de medalii "
            "(23 de aur). Considerat cel mai mare inotator al tuturor timpurilor."
        ),
    },
    {
        "nume": "Katie Ledecky",
        "imagine": "ledecky.jpg",
        "tara": "Statele Unite",
        "probe": "fond - 400m, 800m, 1500m liber",
        "descriere": (
            "Una dintre cele mai mari inotatoare de fond din toate timpurile. "
            "Detine recordurile mondiale la 800m si 1500m liber."
        ),
    },
    {
        "nume": "Adam Peaty",
        "imagine": "peaty.jpg",
        "tara": "Marea Britanie",
        "probe": "bras - 50m, 100m",
        "descriere": (
            "Dublu campion olimpic la 100m bras. Primul inotator care a coborat "
            "sub 57 de secunde la aceasta proba."
        ),
    },
    {
        "nume": "Sarah Sjostrom",
        "imagine": "sjostrom.jpg",
        "tara": "Suedia",
        "probe": "fluture, liber - sprint",
        "descriere": (
            "Detinatoare a recordului mondial la 100m fluture. "
            "Multipla campioana olimpica si mondiala."
        ),
    },
    {
        "nume": "Caeleb Dressel",
        "imagine": "dressel.jpg",
        "tara": "Statele Unite",
        "probe": "sprint - liber, fluture",
        "descriere": (
            "Campion olimpic multiplu la sprint. Detinator al recordului mondial "
            "la 100m fluture in bazin de 50m."
        ),
    },
    {
        "nume": "David Popovici",
        "imagine": "popovici.jpg",
        "tara": "Romania",
        "probe": "liber - 100m, 200m",
        "descriere": (
            "Campion olimpic la 200m liber (Paris 2024). Detinator al recordului "
            "mondial la 100m liber. Cea mai mare speranta a inotului romanesc."
        ),
    },
]


def concursuri_inot():
    """Returneaza HTML cu lista concursurilor internationale de inot."""
    html = '<h2>Concursuri internationale</h2>'
    for concurs in CONCURSURI:
        html += '<div class="card">'
        html += (
            f'<img src="/static/images/{concurs["imagine"]}" '
            f'alt="{concurs["nume"]}" class="card-img">'
        )
        html += '<div class="card-body">'
        html += f'<h3>{concurs["nume"]}</h3>'
        html += (
            f'<p class="meta">{concurs["organizator"]} '
            f'- {concurs["frecventa"]}</p>'
        )
        html += f'<p>{concurs["descriere"]}</p>'
        html += '</div></div>'
    return html


def inotatori_inot():
    """Returneaza HTML cu lista inotatorilor profesionisti."""
    html = '<h2>Inotatori profesionisti</h2>'
    for inotator in INOTATORI:
        html += '<div class="card">'
        html += (
            f'<img src="/static/images/{inotator["imagine"]}" '
            f'alt="{inotator["nume"]}" class="card-img">'
        )
        html += '<div class="card-body">'
        html += f'<h3>{inotator["nume"]}</h3>'
        html += (
            f'<p class="meta">{inotator["tara"]} - {inotator["probe"]}</p>'
        )
        html += f'<p>{inotator["descriere"]}</p>'
        html += '</div></div>'
    return html
