"""
Aplicatie Flask pentru tema Sporturi.
Sportul ales: Inot.
"""

from flask import Flask, url_for
from app.lib import inot

app = Flask(__name__)


STIL_CSS = """
<style>
body { font-family: 'Segoe UI', sans-serif; background: #ffffff; color: #1a1a1a; line-height: 1.6; padding: 40px 20px; margin: 0; }
.wrapper { max-width: 760px; margin: 0 auto; }
header { border-bottom: 1px solid #e5e5e5; padding-bottom: 24px; margin-bottom: 32px; }
header h1 { font-size: 1.75em; margin: 0 0 4px 0; }
header p { color: #6b7280; margin: 0; }
nav { margin-bottom: 32px; }
nav a { color: #2563eb; text-decoration: none; margin-right: 20px; }
nav a:hover { text-decoration: underline; }
h2 { font-size: 1.3em; margin-bottom: 20px; }
.item { padding: 16px 0 16px 16px; border-left: 3px solid #2563eb; margin-bottom: 20px; }
.item h3 { font-size: 1.05em; margin: 0 0 6px 0; }
.item .meta { font-size: 0.85em; color: #6b7280; margin-bottom: 8px; }
.item p { color: #374151; margin-top: 6px; }
.intro { background: #f9fafb; padding: 20px; border-radius: 6px; margin-bottom: 24px; }
.paginare { display: flex; justify-content: space-between; margin-top: 40px; padding-top: 20px; border-top: 1px solid #e5e5e5; }
.paginare a { color: #2563eb; text-decoration: none; padding: 8px 16px; border: 1px solid #e5e5e5; border-radius: 6px; }
.paginare a:hover { background: #f9fafb; }
.paginare .spacer { flex: 1; }
</style>
"""


def pagina(titlu, continut):
    html = "<!DOCTYPE html><html lang='ro'><head><meta charset='UTF-8'>"
    html += "<title>" + titlu + " - Inot</title>" + STIL_CSS
    html += "</head><body><div class='wrapper'>"
    html += "<header><h1>Inot</h1><p>Tema proiect SCC - Ovezea Corina</p></header>"
    html += "<nav>"
    html += "<a href='" + url_for('index') + "'>Acasa</a>"
    html += "<a href='" + url_for('concursuri') + "'>Concursuri</a>"
    html += "<a href='" + url_for('inotatori') + "'>Inotatori</a>"
    html += "</nav>"
    html += continut
    html += "</div></body></html>"
    return html


@app.route("/", methods=['GET'])
def index():
    continut = "<h2>Despre proiect</h2>"
    continut += "<div class='intro'>"
    continut += "<p>Inotul este unul dintre cele mai complete sporturi, antrenand "
    continut += "toate grupele musculare si dezvoltand rezistenta cardiovasculara.</p>"
    continut += "<p style='margin-top: 10px;'>Acest proiect prezinta concursurile "
    continut += "internationale de inot si inotatori profesionisti celebri.</p>"
    continut += "</div>"
    continut += "<p style='color: #6b7280; font-size: 0.9em;'>"
    continut += "Foloseste meniul de mai sus pentru a naviga intre sectiuni.</p>"
    continut += "<div class='paginare'>"
    continut += "<div class='spacer'></div>"
    continut += "<a href='/concursuri'>Pagina urmatoare: Concursuri &rarr;</a>"
    continut += "</div>"
    return pagina("Acasa", continut)


@app.route("/concursuri", methods=['GET'])
def concursuri():
    lista = inot.get_concursuri_inot()
    elemente = ""
    for c in lista:
        elemente += "<div class='item'>"
        elemente += "<h3>" + c['nume'] + "</h3>"
        elemente += "<div class='meta'>" + c['organizator'] + " &middot; " + c['frecventa'] + "</div>"
        elemente += "<p>" + c['descriere'] + "</p>"
        elemente += "</div>"
    paginare = "<div class='paginare'>"
    paginare += "<a href='/'>&larr; Acasa</a>"
    paginare += "<a href='/inotatori'>Pagina urmatoare: Inotatori &rarr;</a>"
    paginare += "</div>"
    continut = "<h2>Concursuri internationale</h2>" + elemente + paginare
    return pagina("Concursuri", continut)


@app.route("/inotatori", methods=['GET'])
def inotatori():
    lista = inot.get_inotatori_profesionisti()
    elemente = ""
    for sportiv in lista:
        elemente += "<div class='item'>"
        elemente += "<h3>" + sportiv['nume'] + "</h3>"
        elemente += "<div class='meta'>" + sportiv['tara'] + " &middot; " + sportiv['specialitate'] + "</div>"
        elemente += "<p>" + sportiv['realizare'] + "</p>"
        elemente += "</div>"
    paginare = "<div class='paginare'>"
    paginare += "<a href='/concursuri'>&larr; Pagina anterioara: Concursuri</a>"
    paginare += "<a href='/'>Acasa</a>"
    paginare += "</div>"
    continut = "<h2>Inotatori profesionisti</h2>" + elemente + paginare
    return pagina("Inotatori", continut)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
