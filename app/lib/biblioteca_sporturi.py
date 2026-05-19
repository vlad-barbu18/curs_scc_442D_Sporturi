INFO_1 = [
    {
        "camp1": "Origine",
        "camp2": "Padelul a aparut in Mexic si a devenit foarte popular in Spania si America Latina.",
    },
    {
        "camp1": "Teren",
        "camp2": "Se joaca pe un teren mai mic decat cel de tenis, inconjurat de pereti de sticla.",
    },
    {
        "camp1": "Jucatori",
        "camp2": "De obicei se joaca la dublu, adica doua echipe formate din cate doi jucatori.",
    },
]

INFO_2 = [
    (
        "Racheta",
        "Racheta de padel este solida, perforata si nu are corzi ca racheta de tenis.",
    ),
    (
        "Mingea",
        "Mingea este asemanatoare cu cea de tenis, dar are presiune putin diferita.",
    ),
    (
        "Reguli",
        "Mingea poate lovi peretii dupa ce atinge terenul, ceea ce face jocul mai strategic.",
    ),
]


def functie_1_padel():
    html = "<h2>Informatii generale despre padel</h2>"
    for item in INFO_1:
        html += f"<p><b>{item['camp1']}</b>: {item['camp2']}</p>"
    return html


def functie_2_padel():
    html = "<h2>Echipament si reguli in padel</h2><ul>"
    for titlu, descriere in INFO_2:
        html += f"<li><b>{titlu}</b>: {descriere}</li>"
    html += "</ul>"
    return html
