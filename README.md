# Proiect SCC - Sporturi

## Dezvoltator

Andrei Blindu

## Tema proiectului

Tema proiectului este **Sporturi**, iar elementul ales pentru implementare este **Rugby**.

## Descriere proiect

Acest proiect reprezintă o aplicație web simplă realizată în Flask pentru disciplina **Servicii Cloud și Containerizare**.

Aplicația prezintă informații despre sportul Rugby și include pagini web pentru afișarea regulilor de bază și a echipamentului folosit în rugby.

Scopul proiectului este utilizarea unor instrumente specifice dezvoltării software și DevOps, precum Git, GitHub, Flask, pytest, Jenkins și Docker.

## Funcționalitate implementată

Pentru sportul ales, Rugby, au fost implementate două funcții în fișierul `app/lib/biblioteca_rugby.py`.

Funcțiile implementate sunt `reguli_rugby()` și `echipament_rugby()`.

Funcția `reguli_rugby()` returnează informații formatate HTML despre regulile de bază din rugby, precum pasele, eseul, placajul și lovitura de pedeapsă.

Funcția `echipament_rugby()` returnează informații formatate HTML despre echipamentul folosit în rugby, precum mingea, tricoul, ghetele, protecția dentară și terenul.

## Structura proiectului

Proiectul conține aplicația principală Flask în fișierul `sporturi.py`, biblioteca pentru funcționalitatea Rugby în `app/lib/biblioteca_rugby.py`, testele automate în `app/tests/test_biblioteca_rugby.py`, fișierul `Jenkinsfile` pentru rularea pipeline-ului Jenkins, fișierul `Dockerfile` pentru containerizare, scriptul `dockerstart.sh` pentru pornirea aplicației în container, fișierul `quickrequirements.txt` pentru dependențe și folderul `doc/` pentru capturile de ecran Docker.

## Rute implementate

Aplicația conține următoarele rute:

- `/` redirecționează către `/sporturi`
- `/sporturi` afișează pagina principală a temei Sporturi
- `/sporturi/rugby` afișează pagina principală pentru sportul Rugby
- `/sporturi/rugby/reguli` afișează regulile de bază din rugby
- `/sporturi/rugby/echipament` afișează echipamentul folosit în rugby

## Rulare locală

Pentru rularea aplicației local, se activează mediul virtual:

source ./activeaza_venv
