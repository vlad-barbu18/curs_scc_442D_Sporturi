"""
Biblioteca cu informatii despre inot.
Returneaza date Python (liste de dicționare).
Formatarea HTML se face in rutele Flask din sporturi.py.
"""


def get_concursuri_inot():
    """
    Returneaza o lista cu cele mai importante concursuri internationale de inot.
    Fiecare concurs e un dictionar cu: nume, organizator, frecventa, descriere.
    """
    return [
        {
            "nume": "Jocurile Olimpice",
            "organizator": "Comitetul International Olimpic (CIO)",
            "frecventa": "o data la 4 ani",
            "descriere": (
                "Cea mai importanta competitie sportiva internationala. "
                "Inotul este prezent din 1896 (Atena). Probele se desfasoara "
                "in bazin de 50m."
            ),
        },
        {
            "nume": "Campionatele Mondiale",
            "organizator": "World Aquatics (fosta FINA)",
            "frecventa": "o data la 2 ani",
            "descriere": (
                "Cea mai prestigioasa competitie anuala dupa Jocurile Olimpice. "
                "Reuneste cei mai buni inotatori din toate continentele."
            ),
        },
        {
            "nume": "Campionatele Europene",
            "organizator": "LEN (Ligue Europeenne de Natation)",
            "frecventa": "o data la 2 ani",
            "descriere": (
                "Principala competitie continentala europeana. Se desfasoara "
                "atat in bazin lung (50m) cat si in bazin scurt (25m)."
            ),
        },
        {
            "nume": "FINA World Cup",
            "organizator": "World Aquatics",
            "frecventa": "anual",
            "descriere": (
                "Serie de competitii in bazin scurt (25m) organizate in mai "
                "multe orase din lume pe parcursul unui sezon."
            ),
        },
        {
            "nume": "Universiada",
            "organizator": "FISU (Federatia Internationala Sportiva Universitara)",
            "frecventa": "o data la 2 ani",
            "descriere": (
                "Competitia mondiala studenteasca de varf. Inotul este una "
                "dintre disciplinele principale."
            ),
        },
    ]


def get_inotatori_profesionisti():
    """
    Returneaza o lista cu inotatori profesionisti celebri.
    Fiecare inotator e un dictionar cu: nume, tara, specialitate, realizare.
    """
    return [
        {
            "nume": "Michael Phelps",
            "tara": "Statele Unite",
            "specialitate": "fluture, mix individual, liber",
            "realizare": (
                "Cel mai medaliat sportiv olimpic din istorie, cu 28 de "
                "medalii (23 de aur). Considerat cel mai mare inotator "
                "al tuturor timpurilor."
            ),
        },
        {
            "nume": "Katie Ledecky",
            "tara": "Statele Unite",
            "specialitate": "fond - 400m, 800m, 1500m liber",
            "realizare": (
                "Dominatoare absoluta a probelor de fond feminin. Detine "
                "recordurile mondiale la 800m si 1500m liber."
            ),
        },
        {
            "nume": "Caeleb Dressel",
            "tara": "Statele Unite",
            "specialitate": "sprint - 50m si 100m liber, fluture",
            "realizare": (
                "Multiplu campion olimpic si mondial pe distantele scurte. "
                "Cunoscut pentru startul exploziv si finalul puternic."
            ),
        },
        {
            "nume": "David Popovici",
            "tara": "Romania",
            "specialitate": "100m si 200m liber",
            "realizare": (
                "Campion olimpic la 200m liber la Paris 2024. Fost detinator "
                "al recordului mondial la 100m liber. Mandria inotului romanesc."
            ),
        },
        {
            "nume": "Sarah Sjostrom",
            "tara": "Suedia",
            "specialitate": "fluture si liber - sprint",
            "realizare": (
                "Una dintre cele mai bune sprintere din istorie. Detine "
                "recordul mondial la 100m fluture."
            ),
        },
        {
            "nume": "Adam Peaty",
            "tara": "Marea Britanie",
            "specialitate": "bras - 50m si 100m",
            "realizare": (
                "Specialist absolut in bras. Campion olimpic si detinator "
                "al recordului mondial la 100m bras."
            ),
        },
    ]
