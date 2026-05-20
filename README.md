# Proiect SCC - Sporturi

## Student
- **Nume:** Dumitrascu Alexandru
- **Grupa:** 442D
- **Element alocat:** Polo pe apa
- **Branch dezvoltare:** `dev_dumitrascu_alexandru`
- **Branch personal main:** `main_dumitrascu-alexandru`

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

Obiectivul acestui proiect este dezvoltarea unei aplicații web utilizând limbajul Python și framework-ul Flask, având ca temă principală sporturile și ca subtemă polo pe apă. Aplicația are rolul de a prezenta informații generale despre acest sport de echipă intens, regulamentul de joc și echipamentul necesar.

Proiectul urmărește implementarea unor concepte de bază din dezvoltarea aplicațiilor web și din zona DevOps, precum organizarea codului pe module, testarea automată cu pytest, validarea calității codului cu pylint, containerizarea aplicației folosind Docker și automatizarea procesului de build și testare prin Jenkins Pipeline.

## Funcționalitate implementată

În acest branch am adăugat și personalizat aplicația pentru tema „Sporturi”, având ca subtemă polo pe apa.

- Fișierul `app/lib/biblioteca_sporturi.py` contine cele două funcții principale cerute:
  - `reguli_polo()` – returnează informații generale despre regulamentul jocului de polo.
  - `echipament_polo()` –  returnează informații despre echipamentul utilizat de jucători.

- Fișierul principal `sporturi.py` implementeaza cele patru rute conform cerinței:
  - `/sporturi` – pagina principală a temei, cu introducere generală despre sporturi și polo.
  - `/sporturi/polo` – pagina dedicată sportului ales.
  - `/sporturi/polo/reguli_polo` – afișează informațiile despre regulament.
  - `/sporturi/polo/echipament_polo` – afișează informațiile despre echipament.

- Interfața aplicației a fost personalizată folosind HTML și CSS, având o structură simplă și ușor de navigat.

- Fișierul `app/tests/test_biblioteca_sporturi.py` conține testele automate realizate cu pytest pentru verificarea funcțiilor implementate.

- Pentru partea DevOps au fost adăugate:
  - `Dockerfile` pentru containerizarea aplicației,
  - `dockerstart.sh` pentru pornirea automată a aplicației în container,
  - `Jenkinsfile` pentru automatizarea etapelor de build, testare și deploy.

## Stadiu dezvoltare


Funcționalitatea aplicației a fost implementată complet.
- Codul sursă a fost dezvoltat și organizat în branch-ul `dev_dumitrascu_alexandru`.
- Rutele Flask și funcțiile bibliotecii Python sunt funcționale și testate.
- Testarea automată cu pytest a fost realizată cu succes.
- Validarea codului folosind pylint a fost integrată în pipeline-ul Jenkins.
- Aplicația a fost containerizată utilizând Docker.
- Pipeline-ul Jenkins pentru build, testare și deploy funcționează corect.
- Capturile de ecran și documentația README au fost adăugate în proiect.
- Testarea locală, automată și containerizată a fost realizată cu succes.
  
## Testare manuală în browser (rulare locală)

```bash
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_dumitrascu_alexandru
. ./activeaza_venv
./ruleaza_aplicatia
```

Aplicația se accesează la: `http://127.0.0.1:5012/sporturi`

![Pagina tema - local](doc/paginaSporturiLocal.png)
![Pagina element - local](doc/paginaPoloLocal.png)
![Pagina functia 1 - local](doc/paginaReguliPoloLocal.png)
![Pagina functia 2 - local](doc/paginaEchipamentPoloLocal.png)

## Testare automată cu `pytest`

```bash
pytest
```

![Rezultate pytest](doc/pytest.png)

## Validare cod cu `pylint`

```bash
pylint --exit-zero app/lib/biblioteca_sporturi.py
pylint --exit-zero app/tests/test_biblioteca_sporturi.py
pylint --exit-zero sporturi.py
```

![Rezultate pylint](doc/pylint.png)

## Testare cu Docker

```bash
docker build -t sporturi:v01 .
docker run --name sporturi1 -p 8021:5012 sporturi:v01
```

![Consolă container](doc/dockerconsola.png)
![Container Docker](doc/dockerps.png)

Aplicația din container, accesată la `http://localhost:8021/sporturi`:

![Pagina tema - container](doc/paginaTemaContainer.png)
![Pagina element - container](doc/paginaElementContainer.png)
![Pagina functia 1 - container](doc/paginaFunctie1Container.png)
![Pagina functia 2 - container](doc/paginaFunctie2Container.png)

# DevOps CI

Pipeline declarativ definit în `Jenkinsfile`, cu 4 stages:
1. **Build**
   - activarea mediului virtual,
   - verificarea structurii proiectului,
   - pregătirea dependențelor necesare.
2. **pylint** 
   - realizarea analizei statice a codului Python,
   - identificarea warning-urilor și a problemelor de stil.
3. **Unit Tests** - rularea testelor automate folosind 'pytest'
4. **Deploy** - build Docker + creare container
 
## Pipeline Jenkins clasic
![Pipeline Jenkins clasic](doc/jenkinsSimplu.png)

## Pipeline Console Output
![Pipeline Console Output](doc/jenkinsConsoleOutput.png)

## Pipeline Blue Ocean
![Pipeline Blue Ocean](doc/jenkinsBlueOcean.png)

## Concluzii

Proiectul realizat demonstrează dezvoltarea cu succes a unei aplicații web folosind framework-ul Flask împreună cu tehnologii moderne utilizate în zona DevOps.

- **Dezvoltare modulară:** aplicația a fost organizată pe module și funcții separate pentru o structură mai clară și mai ușor de întreținut.
- **Interfață web:** au fost implementate pagini HTML dinamice, elemente vizuale și navigare între rute pentru prezentarea informațiilor despre **polo pe apă**.
- **Testare automată și asigurarea calității:** funcționalitățile aplicației au fost verificate utilizând teste automate realizate cu pytest, iar analiza statică a codului a fost realizată folosind pylint.
- **Portabilitate:** utilizarea Docker a permis rularea aplicației într-un mediu izolat și consistent.
- **Automatizare DevOps:** Jenkins a fost utilizat pentru automatizarea etapelor de build, testare și deploy ale aplicației.

În urma implementării, aplicația a funcționat corect atât local, cât și în containerul Docker, iar pipeline-ul Jenkins a executat cu succes toate etapele configurate.

## Bibliografie

https://github.com/crchende/sysinfo.git
