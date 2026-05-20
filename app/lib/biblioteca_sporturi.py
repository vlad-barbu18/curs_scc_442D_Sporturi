"""
Biblioteca pentru proiectul SCC - Sporturi.
Element ales: sailing.
"""


COMPETITII_SAILING = [
    {
        "nume": "America's Cup",
        "descriere": "Una dintre cele mai cunoscute competitii internationale de sailing, disputata intre echipe de top care folosesc ambarcatiuni performante.",
    },
    {
        "nume": "Sailing World Championships",
        "descriere": "Competitie mondiala organizata pentru mai multe clase olimpice si internationale de ambarcatiuni.",
    },
    {
        "nume": "Olympic Sailing Regatta",
        "descriere": "Competitia de sailing din cadrul Jocurilor Olimpice, unde sportivii concureaza pe clase diferite de barci.",
    },
    {
        "nume": "Volvo Ocean Race",
        "descriere": "Cursa oceanica de anduranta, cunoscuta pentru etapele lungi si conditiile dificile de navigatie.",
    },
    {
        "nume": "Rolex Sydney Hobart Yacht Race",
        "descriere": "Cursa celebra intre Sydney si Hobart, considerata una dintre cele mai solicitante competitii de yachting.",
    },
]


ECHIPAMENT_SAILING = [
    (
        "Barca cu vele",
        "Elementul principal al sportului, folosita pentru deplasare cu ajutorul vantului si controlata prin vele, carma si alte sisteme de reglaj.",
    ),
    (
        "Vele",
        "Suprafete textile speciale care capteaza vantul si transforma forta acestuia in miscare.",
    ),
    (
        "Vesta de salvare",
        "Echipament obligatoriu de siguranta, folosit pentru protectia sportivului in cazul caderii in apa.",
    ),
    (
        "Costum impermeabil",
        "Protejeaza sportivul impotriva apei, vantului si temperaturilor scazute.",
    ),
    (
        "Franghii si sisteme de control",
        "Sunt folosite pentru reglarea velelor si pentru controlul directiei si vitezei ambarcatiunii.",
    ),
]


def competitii_sailing():
    """Returneaza HTML cu informatii despre competitii importante de sailing."""
    html = "<h2>Competitii importante de sailing</h2>"
    for competitie in COMPETITII_SAILING:
        html += (
            f"<p><b>{competitie['nume']}</b>: "
            f"{competitie['descriere']}</p>"
        )
    return html


def echipament_sailing():
    """Returneaza HTML cu informatii despre echipamentul folosit in sailing."""
    html = "<h2>Echipament folosit in sailing</h2><ul>"
    for nume, descriere in ECHIPAMENT_SAILING:
        html += f"<li><b>{nume}</b>: {descriere}</li>"
    html += "</ul>"
    return html
