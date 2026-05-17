# curs_scc_442D_Sporturi — Biliard

---

# Cuprins

1. [Student](#student)
2. [Prezentare proiect](#prezentare-proiect)
3. [Functionalitate implementata](#functionalitate-implementata)
4. [Structura aplicatiei](#structura-aplicatiei)
5. [Rulare locala](#rulare-locala)
6. [Pagini WEB disponibile](#pagini-web-disponibile)
7. [Capturi aplicatie](#capturi-aplicatie)
8. [Testare automata](#testare-automata)
9. [Containerizare Docker](#containerizare-docker)
10. [Integrare Jenkins](#integrare-jenkins)
11. [Comenzi Git utilizate](#comenzi-git-utilizate)
12. [Pull Request](#pull-request)
13. [Concluzii](#concluzii)
14. [Bibliografie](#bibliografie)

---

# Student

- **Nume:** Andriu Cosmin
- **Grupa:** 442D
- **Disciplina:** SCC
- **Tema proiectului:** Sporturi
- **Element ales:** Biliard
- **Branch dezvoltare:** `dev_andriu_cosmin`
- **Branch personal main:** `main_andriu_cosmin`

---

# Prezentare proiect

Acest proiect a fost realizat pentru disciplina SCC și are ca scop dezvoltarea unei aplicații WEB simple folosind framework-ul Flask. Tema generală a proiectului este **Sporturi**, iar elementul ales pentru implementare este **biliardul**.

Aplicația prezintă informații despre biliard, un sport de precizie practicat pe o masă specială, cu bile și tacuri. În cadrul proiectului au fost implementate pagini WEB, funcții Python, teste automate, containerizare Docker și un pipeline Jenkins.

Scopul proiectului este parcurgerea unui flux complet de dezvoltare software, care include:

- folosirea Git și GitHub pentru versionare;
- lucrul pe branch separat;
- dezvoltarea unei aplicații Flask;
- organizarea codului în module;
- testare automată cu `pytest`;
- verificarea codului cu `pylint`;
- rularea aplicației într-un container Docker;
- integrarea unui pipeline Jenkins.

Proiectul a fost realizat pe branch separat pentru a evita modificarea directă a branch-ului principal al repository-ului comun.

---

# Functionalitate implementata

Aplicația conține patru rute principale, conform cerinței proiectului:

1. Pagina principală a temei **Sporturi**;
2. Pagina dedicată elementului ales **Biliard**;
3. Pagina pentru prima funcție din bibliotecă;
4. Pagina pentru a doua funcție din bibliotecă.

Funcțiile implementate în biblioteca proiectului sunt:

## `functie_1_biliard()`

Această funcție returnează informații generale despre biliard, precum:

- definiția sportului;
- masa de joc;
- scopul jocului.

Funcția generează conținut HTML care este afișat într-o pagină separată a aplicației.

## `functie_2_biliard()`

Această funcție returnează reguli de bază ale biliardului, precum:

- lovirea bilei albe;
- respectarea rândului;
- situațiile de fault.

Funcția generează o listă HTML cu regulile de bază, care este afișată într-o rută dedicată.

Aplicația folosește HTML generat în Python și stilizare simplă CSS pentru afișarea paginilor în browser.

---

# Structura aplicatiei

Structura principală a proiectului este următoarea:

```text
curs_scc_442D_Sporturi/
│
├── app/
│   ├── __init__.py
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_sporturi.py
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_biblioteca_sporturi.py
│
├── doc/
│   ├── dockerimages.png
│   ├── dockerconsola.png
│   ├── dockerps.png
│   ├── paginaTemaContainer.png
│   ├── paginaElementContainer.png
│   ├── paginaFunctie1Container.png
│   └── paginaFunctie2Container.png
│
├── sporturi.py
├── quickrequirements.txt
├── activeaza_venv
├── activeaza_venv_jenkins
├── ruleaza_aplicatia
├── pytest.ini
├── Dockerfile
├── dockerstart.sh
├── Jenkinsfile
├── README.md
└── .gitignore
```

## Rolul fisierelor principale

### `sporturi.py`

Fișierul principal al aplicației. Acesta conține:

- inițializarea aplicației Flask;
- funcția `pagina()` pentru generarea paginilor HTML;
- ruta `/sporturi`;
- ruta `/sporturi/biliard`;
- ruta `/sporturi/biliard/functie_1_biliard`;
- ruta `/sporturi/biliard/functie_2_biliard`;
- redirectarea de pe `/` către `/sporturi`.

### `app/lib/biblioteca_sporturi.py`

Acest fișier conține biblioteca proiectului, unde sunt definite cele două funcții cerute:

- `functie_1_biliard()`;
- `functie_2_biliard()`.

Separarea acestor funcții într-un modul dedicat ajută la organizarea codului și la testarea mai ușoară a funcționalităților.

### `app/tests/test_biblioteca_sporturi.py`

Acest fișier conține testele automate realizate cu `pytest`. Testele verifică dacă funcțiile din bibliotecă returnează conținut HTML valid și dacă includ informațiile relevante despre biliard.

### `quickrequirements.txt`

Fișierul conține bibliotecile necesare pentru proiect:

```text
flask
pytest
pylint
gunicorn
```

### `activeaza_venv`

Script folosit pentru activarea mediului virtual local. Dacă mediul virtual nu există, scriptul apelează `activeaza_venv_jenkins`.

### `activeaza_venv_jenkins`

Script folosit pentru crearea mediului virtual și instalarea dependențelor. Este utilizat și în pipeline-ul Jenkins.

### `ruleaza_aplicatia`

Script folosit pentru pornirea aplicației Flask local, pe portul `5012`.

### `Dockerfile`

Fișierul definește imaginea Docker folosită pentru rularea aplicației într-un container.

### `dockerstart.sh`

Script folosit pentru pornirea aplicației Flask în interiorul containerului Docker.

### `Jenkinsfile`

Fișierul definește pipeline-ul Jenkins, cu etape de build, verificare cod, testare și deploy.

---

# Rulare locala

Pentru rularea aplicației local, se clonează repository-ul și se intră pe branch-ul de dezvoltare personal:

```bash
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_andriu_cosmin
```

Se activează mediul virtual:

```bash
source ./activeaza_venv
```

Se pornește aplicația Flask:

```bash
source ./ruleaza_aplicatia
```

Aplicația poate fi accesată în browser la adresa:

```text
http://127.0.0.1:5012/sporturi
```

Pentru oprirea aplicației se folosește combinația:

```text
Ctrl + C
```

---

# Pagini WEB disponibile

Aplicația conține următoarele pagini WEB:

## 1. Pagina principală a temei

```text
http://127.0.0.1:5012/sporturi
```

Această pagină prezintă tema generală a proiectului, adică **Sporturi**, și oferă acces către pagina elementului ales, **Biliard**.

## 2. Pagina elementului ales

```text
http://127.0.0.1:5012/sporturi/biliard
```

Această pagină conține o scurtă prezentare a sportului ales și legături către cele două pagini generate pe baza funcțiilor din bibliotecă.

## 3. Pagina funcției 1

```text
http://127.0.0.1:5012/sporturi/biliard/functie_1_biliard
```

Această pagină afișează informații generale despre biliard, generate de funcția `functie_1_biliard()`.

## 4. Pagina funcției 2

```text
http://127.0.0.1:5012/sporturi/biliard/functie_2_biliard
```

Această pagină afișează reguli de bază despre biliard, generate de funcția `functie_2_biliard()`.

---

# Capturi aplicatie

În această secțiune sunt prezentate capturile aplicației rulate în container Docker.

## Pagina principala - Sporturi

![Pagina tema container](doc/paginaTemaContainer.png)

## Pagina elementului ales - Biliard

![Pagina element container](doc/paginaElementContainer.png)

## Pagina functie 1 - Informatii generale

![Pagina functie 1 container](doc/paginaFunctie1Container.png)

## Pagina functie 2 - Reguli de baza

![Pagina functie 2 container](doc/paginaFunctie2Container.png)

---

# Testare automata

Pentru testarea automată a fost folosit framework-ul `pytest`.

Fișierul de testare este:

```text
app/tests/test_biblioteca_sporturi.py
```

Testele implementate verifică următoarele aspecte:

- funcția `functie_1_biliard()` returnează conținut HTML;
- funcția `functie_1_biliard()` conține informații despre definiția biliardului;
- funcția `functie_2_biliard()` returnează o listă HTML;
- funcția `functie_2_biliard()` conține reguli de bază despre biliard.

Rularea testelor se face cu:

```bash
source ./activeaza_venv
pytest
```

Rezultatul așteptat este ca toate testele să treacă fără erori.

Exemplu rezultat așteptat:

```text
4 passed
```

Prin aceste teste se verifică faptul că biblioteca proiectului funcționează corect și returnează informațiile necesare pentru paginile aplicației.

---

# Containerizare Docker

Pentru rularea aplicației într-un mediu izolat a fost folosit Docker.

Containerizarea permite rularea aplicației într-un mediu controlat, fără a depinde direct de configurația sistemului local.

## Construirea imaginii Docker

Imaginea Docker se construiește cu următoarea comandă:

```bash
docker build -t sporturi:v01 .
```

## Verificarea imaginii Docker

După build, imaginea poate fi verificată cu:

```bash
docker images | grep sporturi
```

Captură imagine Docker:

![Imagine Docker](doc/dockerimages.png)

## Pornirea containerului

Containerul se pornește cu următoarea comandă:

```bash
docker run --name sporturi1 -p 8021:5012 sporturi:v01
```

Prin această comandă, portul `5012` din container este mapat pe portul `8021` al sistemului local.

Aplicația rulează în container și poate fi accesată în browser la:

```text
http://127.0.0.1:8021/sporturi
```

## Consola containerului

În consola containerului se poate observa pornirea aplicației Flask.

![Consola Docker](doc/dockerconsola.png)

## Verificarea containerului activ

Containerul activ poate fi verificat cu:

```bash
docker ps
```

Captură container activ:

![Docker ps](doc/dockerps.png)

## Oprirea containerului

Pentru oprirea și ștergerea containerului se folosesc comenzile:

```bash
docker stop sporturi1
docker rm sporturi1
```

---

# Integrare Jenkins

Pentru automatizarea procesului de build, testare și deploy a fost creat fișierul `Jenkinsfile`.

Pipeline-ul Jenkins conține următoarele etape:

## 1. Build

În această etapă se afișează folderul curent, se listează fișierele și se creează mediul virtual pentru Jenkins folosind scriptul:

```bash
./activeaza_venv_jenkins
```

Scopul acestei etape este pregătirea mediului de lucru și instalarea dependențelor necesare aplicației.

## 2. Pylint - calitate cod

În această etapă se verifică fișierele Python folosind `pylint`.

Comenzile folosite în pipeline sunt:

```bash
pylint --exit-zero app/lib/*.py
pylint --exit-zero app/tests/*.py
pylint --exit-zero sporturi.py
```

Opțiunea `--exit-zero` permite afișarea avertismentelor fără oprirea pipeline-ului. Astfel, pipeline-ul continuă chiar dacă apar avertismente de stil.

## 3. Unit Testing cu pytest

În această etapă sunt rulate testele automate:

```bash
pytest
```

Această etapă verifică funcționalitatea celor două funcții din biblioteca proiectului.

## 4. Deploy

În această etapă Jenkins construiește imaginea Docker și creează containerul:

```bash
docker build -t sporturi:v${BUILD_NUMBER} .
docker create --name sporturi${BUILD_NUMBER} -p 8021:5012 sporturi:v${BUILD_NUMBER}
```

Prin folosirea variabilei `${BUILD_NUMBER}`, fiecare build primește o etichetă diferită.

---

# Comenzi Git utilizate

Pentru acest proiect s-a lucrat pe branch separat, pentru a nu modifica direct branch-ul principal al repository-ului.

Branch-ul de dezvoltare folosit:

```text
dev_andriu_cosmin
```

Branch-ul personal de main:

```text
main_andriu_cosmin
```

## Configurare Git

```bash
git config --global user.name "andriu_cosmin"
git config --global user.email "emailul_contului_github"
git config --global credential.helper store
```

## Clonare repository

```bash
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
```

## Trecere pe branch-ul personal de dezvoltare

```bash
git checkout dev_andriu_cosmin
```

## Verificarea branch-ului curent

```bash
git branch
```

## Salvarea modificărilor

```bash
git status
git add .
git commit -m "mesaj commit"
git push
```

---

# Pull Request

La finalul implementării, se creează un Pull Request din branch-ul de dezvoltare personal către branch-ul personal de main:

```text
dev_andriu_cosmin → main_andriu_cosmin
```

Acest Pull Request conține implementarea proiectului pentru elementul ales, **Biliard**.

După verificare, Pull Request-ul poate fi aprobat și făcut merge în branch-ul personal `main_andriu_cosmin`.

Dacă este necesară integrarea în branch-ul principal al grupei, se poate crea ulterior un Pull Request separat, conform regulilor stabilite pentru proiect.

---

# Concluzii

În cadrul proiectului a fost realizată o aplicație WEB simplă, folosind Python și Flask. Aplicația prezintă tema **Sporturi**, cu elementul ales **Biliard**, și include patru rute principale, două funcții separate în bibliotecă și teste automate.

Prin realizarea acestui proiect au fost parcurse etape importante dintr-un flux software complet:

- dezvoltare aplicație Flask;
- organizarea codului în module;
- versionare folosind Git și GitHub;
- lucru pe branch separat;
- testare automată cu `pytest`;
- verificare cod cu `pylint`;
- containerizare Docker;
- integrare Jenkins.

Proiectul este modular, ușor de rulat local și poate fi executat și într-un container Docker, ceea ce permite portabilitate și reproducerea mediului de rulare.

---

# Bibliografie

- Documentație Flask: https://flask.palletsprojects.com/
- Documentație Docker: https://docs.docker.com/
- Documentație Jenkins: https://www.jenkins.io/doc/
- Documentație pytest: https://docs.pytest.org/
- Repository model: https://github.com/crchende/sysinfo.git
