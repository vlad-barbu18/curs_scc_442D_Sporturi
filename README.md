# Proiect SCC - Sporturi

## Dezvoltator
- **Nume:** Ana Maria Petre
- **Grupa:** 442D
- **Element alocat:** Tenis de Camp

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

Obiectivul proiectului a fost realizarea unei aplicații web folosind framework-ul Flask, parcurgerea unui proces complet de dezvoltare software în care folosim Jenkins, Docker, Python și GitHub pentru versionare, containerizare, programare și automatizare.

Tema aleasă pentru proiect este reprezentată de sporturi, iar elementul implementat este tenisul de câmp. Aplicația oferă informații generale despre acest sport și prezintă câteva tehnici importante utilizate în tenis.

## Funcționalitate implementată

În acest branch au fost adăugate și personalizate următoarele componente:

- Fișierul `app/lib/biblioteca_sporturi.py` cu cele două funcții cerute:
  - `functie_1_tenis()` – afișează informații generale despre tenisul de câmp.
  - `functie_2_tenis()` – afișează tehnici importante utilizate în tenis.

- Fișierul principal `sporturi.py` care conține cele patru rute conform cerinței:
  - `/sporturi` – pagina principală a temei.
  - `/sporturi/tenis` – pagina elementului ales.
  - `/sporturi/tenis/functie_1_tenis` – informația 1.
  - `/sporturi/tenis/functie_2_tenis` – informația 2.

- Fișierul `app/tests/test_biblioteca_sporturi.py` care conține testele automate realizate cu `pytest`.

## Stadiu dezvoltare

- Funcționalitate complet implementată.
- Cod adăugat în branch-ul `dev_nume_prenume`.
- Dockerfile și Jenkinsfile funcționale.
- Testare locală, automată și containerizată realizată cu succes.
- Pipeline Jenkins configurat și executat cu succes.

## Testare manuală în browser (rulare locală)

```bash
git clone <url-repo>
cd <folder-repo>
git checkout dev_nume_prenume
. ./activeaza_venv
./ruleaza_aplicatia