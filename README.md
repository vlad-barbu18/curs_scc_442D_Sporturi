# Curs SCC 442D Sporturi

## Dezvoltator

- **Nume:** Nedelcu Alexandru
- **Grupa:** 442D
- **Tema proiectului:** Sporturi
- **Element ales:** Ski
- **Branch de dezvoltare:** `dev_Nedelcu_Alexandru`

---

## Cuprins

- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Structura proiectului](#structura-proiectului)
- [Rute disponibile](#rute-disponibile)
- [Tehnologii utilizate](#tehnologii-utilizate)
- [Rulare locală](#rulare-locală)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Rulare cu Docker](#rulare-cu-docker)
- [DevOps CI - Jenkins](#devops-ci---jenkins)
- [Capturi de ecran](#capturi-de-ecran)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

---

## Descriere generală

Acest proiect a fost realizat pentru disciplina SCC și urmărește dezvoltarea unei aplicații web simple folosind framework-ul Flask.

Tema generală a proiectului este **Sporturi**, iar elementul ales pentru implementarea individuală este **ski-ul**. Aplicația prezintă o pagină dedicată unei pârtii de ski, cu informații despre programul de funcționare, starea pârtiei, prețuri pentru skipass, urcări individuale, închirieri de echipament și date de contact.

Pagina `/sporturi` este gândită ca pagină generală pentru proiectul de grup, unde pot fi integrate și celelalte sporturi ale colegilor. Componenta individuală este disponibilă la ruta `/sporturi/ski`.

---

## Funcționalitate implementată

În cadrul branch-ului `dev_Nedelcu_Alexandru` au fost implementate următoarele componente:

- aplicație web Flask în fișierul `sporturi.py`;
- pagină generală pentru tema **Sporturi**;
- pagină principală pentru sportul ales: **Ski**;
- pagină pentru programul pârtiei și starea acesteia;
- pagină pentru tarife skipass și urcări individuale;
- pagină pentru închirieri echipament;
- pagină pentru reguli și contact;
- bibliotecă Python separată în `app/lib/biblioteca_sporturi.py`;
- teste automate în `app/tests/test_biblioteca_sporturi.py`;
- configurare pentru rulare locală cu virtual environment;
- configurare Docker prin `Dockerfile` și `dockerstart.sh`;
- configurare CI/CD prin `Jenkinsfile`.

---

## Structura proiectului

```text
curs_scc_442D_Sporturi/
│
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_sporturi.py
│   └── tests/
│       ├── __init__.py
│       └── test_biblioteca_sporturi.py
│
├── doc/
│   ├── docker_build.png
│   ├── docker_ps.png
│   ├── docker_run.png
│   ├── imagine_creeata.png
│   ├── jenkins_blue_ocean.png
│   ├── jenkins_status.png
│   ├── pagina skipass.png
│   ├── pagina_contact.png
│   ├── pagina_inchirieri.png
│   ├── pagina_program.png
│   ├── pagina_ski.png
│   └── pagina_sporturi.png
│
├── Dockerfile
├── Jenkinsfile
├── README.md
├── activeaza_venv
├── activeaza_venv_jenkins
├── dockerstart.sh
├── pytest.ini
├── quickrequirements.txt
├── ruleaza_aplicatia
└── sporturi.py
