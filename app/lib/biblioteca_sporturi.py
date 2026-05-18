"""
Biblioteca pentru proiectul SCC - Sporturi.
Element ales: Balet.
"""


STILURI_BALET = [
    {
        "nume": "Balet clasic",
        "descriere": (
            "Baletul clasic este forma traditionala a baletului si pune accent "
            "pe postura corecta, miscari precise, echilibru, piruete si sarituri."
        ),
    },
    {
        "nume": "Balet romantic",
        "descriere": (
            "Baletul romantic evidentiaza expresivitatea, povestea si miscarile "
            "usoare, fiind asociat cu spectacole in care dansatorii transmit emotie."
        ),
    },
    {
        "nume": "Balet neoclasic",
        "descriere": (
            "Baletul neoclasic pastreaza tehnica baletului clasic, dar foloseste "
            "miscari mai libere si o interpretare mai moderna."
        ),
    },
    {
        "nume": "Balet contemporan",
        "descriere": (
            "Baletul contemporan combina tehnica de balet cu elemente moderne, "
            "permitand o exprimare mai libera si coregrafii variate."
        ),
    },
]


ECHIPAMENT_BALET = [
    {
        "element": "Poante",
        "rol": (
            "Sunt incaltamintea specifica baletului clasic si permit dansatoarelor "
            "sa execute miscari pe varful degetelor."
        ),
    },
    {
        "element": "Body de balet",
        "rol": (
            "Este folosit pentru a permite libertate de miscare si pentru ca "
            "postura corpului sa poata fi observata corect in timpul antrenamentului."
        ),
    },
    {
        "element": "Fusta tutu",
        "rol": (
            "Este un element vestimentar des intalnit in spectacolele de balet, "
            "avand atat rol estetic, cat si rol scenic."
        ),
    },
    {
        "element": "Colanti",
        "rol": (
            "Sunt folositi pentru sustinerea musculaturii si pentru evidentierea "
            "liniei picioarelor in timpul miscarilor."
        ),
    },
]


def stiluri_balet():
    """Returneaza cod HTML cu principalele stiluri de balet."""
    html = "<h2>Stiluri de balet</h2>"
    html += (
        "<p>Baletul include mai multe stiluri, fiecare avand caracteristici "
        "proprii de tehnica, expresivitate si interpretare scenica.</p>"
    )

    for stil in STILURI_BALET:
        html += f"<h3>{stil['nume']}</h3>"
        html += f"<p>{stil['descriere']}</p>"

    return html


def echipament_balet():
    """Returneaza cod HTML cu echipamentul folosit in balet."""
    html = "<h2>Echipament de balet</h2>"
    html += (
        "<p>Echipamentul de balet este important deoarece ajuta dansatorul "
        "sa execute miscarile corect, in siguranta si cu eleganta.</p>"
    )
    html += "<ul>"

    for obiect in ECHIPAMENT_BALET:
        html += f"<li><b>{obiect['element']}</b>: {obiect['rol']}</li>"

    html += "</ul>"
    return html
