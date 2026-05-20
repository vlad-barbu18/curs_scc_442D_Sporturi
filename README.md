# # Proiect SCC - Sporturi

## Dezvoltator

- **Nume:** Mitu Marian
- **Grupa:** 442D
- **Tema proiectului:** Sporturi
- **Element ales:** MMA
- **Branch de dezvoltare:** `dev_mitu_marian`
- **Branch personal de main:** `main_mitu_marian`

---

## Cuprins

- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Structura proiectului](#structura-proiectului)
- [Rutele aplicației](#rutele-aplicației)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuală în browser](#testare-manuală-în-browser)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI - Jenkins](#devops-ci---jenkins)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

---

## Descriere generală

Acest proiect reprezintă o aplicație web realizată în Python, folosind framework-ul Flask.

Tema proiectului este **Sporturi**, iar elementul ales este **MMA**. Aplicația prezintă informații despre MMA, luptători cunoscuți, tehnici importante și reguli de bază.

Proiectul urmărește parcurgerea unui flux complet de dezvoltare software, folosind:

- **Python** pentru implementarea aplicației;
- **Flask** pentru dezvoltarea aplicației web;
- **GitHub** pentru versionare;
- **pytest** pentru testare automată;
- **pylint** pentru verificarea calității codului;
- **Docker** pentru containerizare;
- **Jenkins** pentru automatizarea procesului de build, testare și deploy.

---

## Funcționalitate implementată

În acest branch am adăugat și personalizat următoarele componente:

### 1. Fișierul principal `sporturi.py`

Acest fișier conține aplicația Flask și rutele principale ale site-ului.

Aplicația are un design modern, cu fundal tematic MMA, navigație între pagini și carduri pentru afișarea informațiilor.

### 2. Biblioteca `app/lib/biblioteca_sporturi.py`

Fișierul conține cele două funcții cerute în proiect:

- `afiseaza_luptatori_mma()`  
  Returnează conținut HTML despre luptători reprezentativi din MMA.

- `afiseaza_tehnici_mma()`  
  Returnează conținut HTML despre tehnici importante folosite în MMA.

### 3. Fișierul de teste `app/tests/test_biblioteca_sporturi.py`

Acest fișier conține teste automate pentru cele două funcții din biblioteca proiectului.

Testele verifică:

- dacă funcțiile returnează conținut HTML;
- dacă rezultatul conține elemente specifice;
- dacă apar informații despre luptători;
- dacă apar informații despre tehnici MMA.

### 4. Dockerfile

Fișierul `Dockerfile` permite construirea unei imagini Docker pentru aplicația Flask.

### 5. Jenkinsfile

Fișierul `Jenkinsfile` definește un pipeline declarativ cu etapele:

1. Build
2. Verificare cod cu pylint
3. Testare automată cu pytest
4. Deploy prin Docker

---

## Structura proiectului

Structura principală a proiectului este:

```text
curs_scc_442D_Sporturi/
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_sporturi.py
│   └── tests/
│       ├── __init__.py
│       └── test_biblioteca_sporturi.py
├── doc/
│   ├── dockerimages.png
│   ├── dockerconsola.png
│   ├── dockerps.png
│   ├── paginaTemaLocal.png
│   ├── paginaElementLocal.png
│   ├── paginaLuptatoriLocal.png
│   ├── paginaTehniciLocal.png
│   ├── paginaReguliLocal.png
│   ├── paginaTemaContainer.png
│   ├── paginaElementContainer.png
│   ├── paginaLuptatoriContainer.png
│   ├── paginaTehniciContainer.png
│   ├── paginaReguliContainer.png
│   ├── pytest.png
│   ├── pylint.png
│   ├── jenkinsBlueOcean.png
│   └── jenkinsSimplu.png
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