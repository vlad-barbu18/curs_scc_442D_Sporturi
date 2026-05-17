"""
Biblioteca cu cele doua functii pentru fotbal
"""


COMPETITII_INTERNATIONALE = [
    {
        "nume": "FIFA World Cup",
        "tip": "echipe nationale",
        "organizator": "FIFA",
        "an_infiintare": 1930,
        "frecventa": "la 4 ani",
        "detinator_titlu": "Argentina (2022)",
        "recordman_titluri": "Brazilia - 5 titluri",
    },
    {
        "nume": "UEFA European Championship (EURO)",
        "tip": "echipe nationale",
        "organizator": "UEFA",
        "an_infiintare": 1960,
        "frecventa": "la 4 ani",
        "detinator_titlu": "Spania (2024)",
        "recordman_titluri": "Spania - 4 titluri",
    },
    {
        "nume": "UEFA Champions League",
        "tip": "cluburi",
        "organizator": "UEFA",
        "an_infiintare": 1955,
        "frecventa": "anual",
        "detinator_titlu": "PSG (2025)",
        "recordman_titluri": "Real Madrid - 15 titluri",
    },
    {
        "nume": "UEFA Europa League",
        "tip": "cluburi",
        "organizator": "UEFA",
        "an_infiintare": 1971,
        "frecventa": "anual",
        "detinator_titlu": "Tottenham Hotspur (2025)",
        "recordman_titluri": "Sevilla - 7 titluri",
    },
    {
        "nume": "UEFA Conference League",
        "tip": "cluburi",
        "organizator": "UEFA",
        "an_infiintare": 2021,
        "frecventa": "anual",
        "detinator_titlu": "Chelsea (2025)",
        "recordman_titluri": "AS Roma, West Ham, Olympiacos, Chelsea - 1 titlu",
    },
    {
        "nume": "Copa America",
        "tip": "echipe nationale",
        "organizator": "CONMEBOL",
        "an_infiintare": 1916,
        "frecventa": "neregulata (2-4 ani)",
        "detinator_titlu": "Argentina (2024)",
        "recordman_titluri": "Argentina - 16 titluri",
    },
    {
        "nume": "Copa Libertadores",
        "tip": "cluburi",
        "organizator": "CONMEBOL",
        "an_infiintare": 1960,
        "frecventa": "anual",
        "detinator_titlu": "Flamengo (2025)",
        "recordman_titluri": "Independiente - 7 titluri",
    },
]

CAMPIONATE_NATIONALE = [
    {
        "nume": "Premier League",
        "tara": "Anglia",
        "an_infiintare": 1992,
        "numar_echipe": 20,
        "detinator_titlu": "Liverpool (2024-25)",
        "recordman_titluri": "Manchester United - 13 titluri",
    },
    {
        "nume": "La Liga",
        "tara": "Spania",
        "an_infiintare": 1929,
        "numar_echipe": 20,
        "detinator_titlu": "Barcelona (2025-26)",
        "recordman_titluri": "Real Madrid - 36 titluri",
    },
    {
        "nume": "Serie A",
        "tara": "Italia",
        "an_infiintare": 1898,
        "numar_echipe": 20,
        "detinator_titlu": "Inter Milano (2025-26)",
        "recordman_titluri": "Juventus - 36 titluri",
    },
    {
        "nume": "Bundesliga",
        "tara": "Germania",
        "an_infiintare": 1963,
        "numar_echipe": 18,
        "detinator_titlu": "Bayern Munchen (2025-26)",
        "recordman_titluri": "Bayern Munchen - 35 titluri",
    },
    {
        "nume": "Ligue 1",
        "tara": "Franta",
        "an_infiintare": 1932,
        "numar_echipe": 18,
        "detinator_titlu": "PSG (2025-26)",
        "recordman_titluri": "PSG - 14 titluri",
    },
    {
        "nume": "SuperLiga (Liga 1)",
        "tara": "Romania",
        "an_infiintare": 1909,
        "numar_echipe": 16,
        "detinator_titlu": "FCSB (2024-25)",
        "recordman_titluri": "Steaua Bucuresti - 28 titluri",
    },
]

ECHIPAMENT_JUCATOR = [
    ("Tricou", "Maneca scurta sau lunga, in culorile clubului / nationalei. "
               "Numar pe spate (si optional numele jucatorului)."),
    ("Sort", "Pantaloni scurti, in culoarea principala sau contrastanta."),
    ("Jambiere", "Sosete lungi, pana sub genunchi. Acopera aparatorile de tibie."),
    ("Aparatori de tibie", "OBLIGATORII conform FIFA. Protejeaza tibia."),
    ("Ghete de fotbal", "Au crampoane pentru aderenta. Tipuri: FG, SG, AG, IC."),
]

ECHIPAMENT_PORTAR = [
    ("Tricou de portar", "Culoare diferita de a coechipierilor. Captusit la coate."),
    ("Manusi de portar", "Latex in palme pentru aderenta. Pot avea finger save."),
    ("Sort lung sau pantaloni", "Adesea mai lungi sau captusiti la solduri."),
    ("Restul echipamentului", "Jambiere, aparatori si ghete - ca jucatorii."),
]

ECHIPAMENT_ARBITRU = [
    ("Tricou de arbitru", "Culoare neutra, diferita de cele doua echipe."),
    ("Fluier", "Pentru a semnaliza inceputul, sfarsitul si faulturile."),
    ("Cartonase galben si rosu", "Galben = avertisment. Rosu = eliminare."),
    ("Ceas / cronometru", "Unul clasic si unul pentru prelungiri."),
    ("Carnetel si pix", "Pentru a nota cartonase, goluri, schimbari."),
    ("Vanishing spray", "Marcheaza linia zidului la lovituri libere."),
    ("Casti / comunicatii", "Comunicare cu asistentii si arbitrul VAR."),
]

INFO_MINGE = {
    "Forma": "sferica",
    "Material": "piele sau material sintetic",
    "Circumferinta": "intre 68 si 70 cm (size 5 regulamentar)",
    "Greutate": "intre 410 si 450 g la inceputul meciului",
    "Presiune": "intre 0.6 si 1.1 atmosfere",
    "Standard FIFA": "FIFA Quality Pro pentru competitiile oficiale",
}

INFO_TEREN = {
    "Forma": "dreptunghiulara",
    "Lungime (international)": "intre 100 si 110 m",
    "Latime (international)": "intre 64 si 75 m",
    "Suprafata": "iarba naturala, hibrida sau sintetica",
    "Poarta": "lata de 7.32 m si inalta de 2.44 m",
    "Punct penalty": "la 11 m de linia portii",
    "Cerc central": "raza de 9.15 m",
    "Suprafata de pedeapsa": "16.5 m de la poarta, 40.32 m latime",
}


def _lista_piese_html(titlu, lista):
    """Privata. Formateaza o lista de piese ca HTML."""
    html = f"<h2>{titlu}</h2><ul>"
    for piesa, detalii in lista:
        html += f"<li><b>{piesa}</b> &mdash; {detalii}</li>"
    html += "</ul>"
    return html


def _dict_info_html(titlu, d):
    """Privata. Formateaza un dictionar cheie:valoare ca HTML."""
    html = f"<h2>{titlu}</h2><ul>"
    for cheie, valoare in d.items():
        html += f"<li><b>{cheie}:</b> {valoare}</li>"
    html += "</ul>"
    return html


def competitii_fotbal():
    """Functia 1: returneaza HTML cu competitiile internationale si nationale."""
    html = "<h2>Competitii internationale</h2>"
    for c in COMPETITII_INTERNATIONALE:
        html += "<div style='margin-bottom: 15px; padding: 10px; "
        html += "border-left: 4px solid #2563eb;'>"
        html += f"<b>{c['nume']}</b> ({c['tip']})<br>"
        html += f"Organizator: {c['organizator']} | "
        html += f"An infiintare: {c['an_infiintare']} | "
        html += f"Frecventa: {c['frecventa']}<br>"
        html += f"Detinator titlu: {c['detinator_titlu']}<br>"
        html += f"Recordman titluri: {c['recordman_titluri']}"
        html += "</div>"

    html += "<h2>Campionate nationale principale</h2>"
    for c in CAMPIONATE_NATIONALE:
        html += "<div style='margin-bottom: 15px; padding: 10px; "
        html += "border-left: 4px solid #16a34a;'>"
        html += f"<b>{c['nume']}</b> ({c['tara']})<br>"
        html += f"An infiintare: {c['an_infiintare']} | "
        html += f"Numar echipe: {c['numar_echipe']}<br>"
        html += f"Detinator titlu: {c['detinator_titlu']}<br>"
        html += f"Recordman titluri: {c['recordman_titluri']}"
        html += "</div>"
    return html


def echipament_fotbal():
    """Functia 2: returneaza HTML cu tot echipamentul de fotbal."""
    html = _lista_piese_html("Echipament jucator de camp", ECHIPAMENT_JUCATOR)
    html += _lista_piese_html("Echipament portar", ECHIPAMENT_PORTAR)
    html += _lista_piese_html("Echipament arbitru", ECHIPAMENT_ARBITRU)
    html += _dict_info_html("Mingea", INFO_MINGE)
    html += _dict_info_html("Terenul de joc", INFO_TEREN)
    return html
