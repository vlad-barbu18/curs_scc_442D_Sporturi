"""
Biblioteca cu functii HTML pentru elementul ales: ski.

Functiile sunt folosite de aplicatia Flask din sporturi.py.
"""


PROGRAM_PARTIE = [
    ("Luni - Joi", "09:00 - 17:00"),
    ("Vineri", "09:00 - 20:00"),
    ("Sambata - Duminica", "08:30 - 21:00"),
    ("Nocturna", "18:00 - 21:00, doar in weekend"),
]


TARIFE_SKIPASS = [
    ("Urcare individuala adult", "25 lei"),
    ("Urcare individuala copil", "18 lei"),
    ("Skipass 2 ore adult", "90 lei"),
    ("Skipass 2 ore copil", "65 lei"),
    ("Skipass 4 ore adult", "140 lei"),
    ("Skipass 4 ore copil", "100 lei"),
    ("Skipass zi completa adult", "210 lei"),
    ("Skipass zi completa copil", "150 lei"),
]


TARIFE_INCHIRIERI = [
    ("Set complet adult", "schiuri + clapari + bete", "95 lei / zi"),
    ("Set complet copil", "schiuri + clapari + bete", "70 lei / zi"),
    ("Schiuri", "pereche schiuri carving", "45 lei / zi"),
    ("Clapari", "marimi adulti si copii", "35 lei / zi"),
    ("Casca", "recomandata pentru siguranta", "20 lei / zi"),
    ("Ochelari ski", "protectie vant si zapada", "25 lei / zi"),
]


REGULI_PARTIE = [
    "Accesul pe partie se face doar cu echipament adecvat.",
    "Casca este recomandata pentru adulti si obligatorie pentru copii.",
    "Viteza trebuie adaptata nivelului de experienta si aglomeratiei.",
    "Este interzisa stationarea in zonele inguste sau fara vizibilitate.",
    "In caz de accident, anuntati imediat personalul partiei.",
]


def program_partie_ski():
    """Returneaza programul partiei si informatii despre stare."""
    html = """
    <h2>Program de functionare</h2>

    <table>
        <tr>
            <th>Zi / interval</th>
            <th>Program</th>
        </tr>
    """

    for zi, program in PROGRAM_PARTIE:
        html += f"""
        <tr>
            <td>{zi}</td>
            <td>{program}</td>
        </tr>
        """

    html += """
    </table>

    <div class="grid">
        <div class="card">
            <h3>Stare partie</h3>
            <p>Deschisa pentru sezonul de iarna.</p>
        </div>

        <div class="card">
            <h3>Strat zapada</h3>
            <p>35 - 55 cm, in functie de altitudine.</p>
        </div>

        <div class="card">
            <h3>Instalatie cablu</h3>
            <p>Telescaun functional, cu revizie zilnica dimineata.</p>
        </div>
    </div>
    """

    return html


def tarife_skipass_ski():
    """Returneaza tarifele pentru skipass si urcari individuale."""
    html = """
    <h2>Tarife skipass si urcari individuale</h2>

    <table>
        <tr>
            <th>Tip acces</th>
            <th>Pret</th>
        </tr>
    """

    for tip_acces, pret in TARIFE_SKIPASS:
        html += f"""
        <tr>
            <td>{tip_acces}</td>
            <td class="price">{pret}</td>
        </tr>
        """

    html += """
    </table>
    """

    return html


def tabel_inchirieri_ski():
    """Returneaza tabelul cu preturi pentru inchirieri echipament."""
    html = """
    <h2>Preturi inchirieri echipament</h2>

    <table>
        <tr>
            <th>Echipament</th>
            <th>Descriere</th>
            <th>Pret</th>
        </tr>
    """

    for echipament, descriere, pret in TARIFE_INCHIRIERI:
        html += f"""
        <tr>
            <td>{echipament}</td>
            <td>{descriere}</td>
            <td class="price">{pret}</td>
        </tr>
        """

    html += """
    </table>
    """

    return html


def reguli_partie_ski():
    """Returneaza lista regulilor de siguranta pentru partie."""
    html = "<h2>Reguli de siguranta</h2><ul>"

    for regula in REGULI_PARTIE:
        html += f"<li>{regula}</li>"

    html += "</ul>"

    return html