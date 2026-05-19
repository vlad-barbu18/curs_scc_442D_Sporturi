# Proiect SCC - Sporturi

## Dezvoltator

- **Nume:** Ovezea Corina
- **Grupa:** 442D
- **Element alocat:** Inot

## Cuprins

- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuală în browser (rulare locală)](#testare-manuală-în-browser-rulare-locală)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI](#devops-ci)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

## Descriere generală

Obiectivul proiectului a fost realizarea unei aplicații web folosind framework-ul Flask, parcurgerea unui proces complet de dezvoltare software în care folosim Git pentru versionare, pytest pentru testare automată, pylint pentru analiză statică, Docker pentru containerizare și Jenkins pentru pipeline CI/CD. Tema grupei este **Sporturi**, iar elementul ales pentru această secțiune este **Înotul**.

## Funcționalitate implementată

În acest branch (`dev_ovezea_corina`) am adăugat și personalizat:

- Fișierul `app/lib/biblioteca_inot.py` cu cele două funcții cerute:
  - `functie_1_concursuri_inot()` – generează HTML cu lista celor mai importante competiții internaționale de înot (Jocurile Olimpice, Campionatele Mondiale, Campionatele Europene, FINA World Cup, Universiada).
  - `functie_2_inotatori_inot()` – generează HTML cu lista celor mai cunoscuți înotători profesioniști (Michael Phelps, Katie Ledecky, Adam Peaty, Sarah Sjöström, Caeleb Dressel, David Popovici).
- Fișierul principal `sporturi.py` care expune cele patru rute conform cerinței:
  - `/sporturi` – pagina temei.
  - `/sporturi/inot` – pagina elementului ales (descriere generală a înotului).
  - `/sporturi/inot/concursuri` – informația 1 (concursuri internaționale).
  - `/sporturi/inot/inotatori` – informația 2 (înotători profesioniști).
- Fișierul `app/tests/test_biblioteca_inot.py` cu 10 teste automate care verifică tipul rezultatelor, prezența tagurilor HTML, conținutul specific (nume de concursuri / înotători) și consistența între datele interne și HTML-ul generat.

## Stadiu dezvoltare

- Funcționalitate complet implementată.
- Cod adăugat în branch-ul `dev_ovezea_corina`.
- Dockerfile și Jenkinsfile sunt funcționale.
- Testare locală, automată și containerizată realizată cu succes.

## Testare manuală în browser (rulare locală)

```bash
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_ovezea_corina
. ./activeaza_venv
./ruleaza_aplicatia
```

Aplicația se accesează la: `http://127.0.0.1:5012/sporturi`

Cele 4 rute disponibile:

- `http://127.0.0.1:5012/sporturi`
- `http://127.0.0.1:5012/sporturi/inot`
- `http://127.0.0.1:5012/sporturi/inot/concursuri`
- `http://127.0.0.1:5012/sporturi/inot/inotatori`

## Testare automată cu `pytest`

```bash
pytest
```

![Rezultate pytest](doc/pytest.png)

Cele 10 teste verifică:

- că ambele funcții returnează șiruri non-goale;
- că HTML-ul generat conține tagurile așteptate (`<h2>`, `<div>`, `<img>`);
- că rezultatele conțin numele concursurilor și înotătorilor cheie;
- că imaginile sunt referite corect din `/static/images/`;
- că numărul de carduri HTML reflectă datele din listele interne.

## Validare cod cu `pylint`

```bash
pylint --exit-zero app/lib/biblioteca_inot.py
pylint --exit-zero app/tests/test_biblioteca_inot.py
pylint --exit-zero sporturi.py
```

![Rezultate pylint](doc/pylint.png)

Toate cele trei fișiere obțin rating-ul **10.00/10**.

## Testare cu Docker

```bash
docker build -t sporturi:v01 .
docker run --name sporturi1 -p 8021:5012 sporturi:v01
```

Imaginea Docker creată:

![Imagine Docker](doc/dockerimages.png)

Container rulând (output `docker ps`):

![Container Docker](doc/dockerps.png)

Consolă container (output Flask la pornire):

![Consolă container](doc/dockerconsola.png)

Aplicația din container, accesată la `http://localhost:8021/sporturi`:

![Pagina temei - container](doc/paginaTemaContainer.png)

![Pagina element (Înot) - container](doc/paginaElementContainer.png)

![Pagina funcția 1 (Concursuri) - container](doc/paginaFunctie1Container.png)

![Pagina funcția 2 (Înotători) - container](doc/paginaFunctie2Container.png)

## DevOps CI

Pipeline declarativ definit în `Jenkinsfile`, cu 4 stages:

1. **Build** – creare venv + instalare dependențe (`activeaza_venv_jenkins`).
2. **pylint** – analiză statică a codului (warning-only, cu `--exit-zero`).
3. **Unit Tests** – rulare `pytest` pe testele automate.
4. **Deploy** – build Docker (`sporturi:v${BUILD_NUMBER}`) și creare container (`sporturi${BUILD_NUMBER}`).

## Concluzii

- **Dezvoltare modulară:** aplicație Flask cu separarea datelor și logicii într-o bibliotecă dedicată (`app/lib/biblioteca_inot.py`).
- **Portabilitate:** Docker asigură rulare consistentă pe orice mediu.
- **Automatizare:** Jenkins automatizează testarea și deploy-ul prin pipeline declarativ.
- **Asigurarea calității:** pytest și pylint integrate în pipeline garantează calitatea codului la fiecare build.

## Bibliografie

- Ghid proiect SCC – Flask + Docker + Jenkins (material curs).
- Exemplu de referință: https://github.com/crchende/sysinfo.git
