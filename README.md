# curs_scc_442D_Sporturi

# Funcționalitate Volei - Bocai Alexandra

## 1. Prezentarea proiectului

Proiectul face parte din disciplina **Servicii Cloud și Containerizare**, grupa **442D**. Tema generală a proiectului este **Sporturi**, iar elementul implementat de mine este **Volei**.

Aplicația este realizată în Flask și prezintă informații despre sportul ales, regulile principale și echipamentul folosit. Pentru partea de dezvoltare și verificare am inclus teste automate, analiză statică, configurare Docker și pipeline Jenkins.

---

## 2. Funcționalități realizate

Pentru elementul Volei am implementat:

- pagina principală a temei Sporturi;
- pagina dedicată sportului Volei;
- pagina pentru regulile jocului de volei;
- pagina pentru echipamentul folosit în volei;
- două funcții publice în biblioteca proiectului:
  - `reguli_volei()`;
  - `echipament_volei()`;
- teste automate pentru funcțiile din bibliotecă;
- fișiere de configurare pentru rulare locală, Docker și Jenkins.

---

## 3. Structura implementării

```text
curs_scc_442D_Sporturi/
│
├── sporturi.py
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
├── quickrequirements.txt
├── pytest.ini
├── activeaza_venv
├── activeaza_venv_jenkins
├── ruleaza_aplicatia
├── dockerstart.sh
├── .gitignore
│
├── app/
│   ├── __init__.py
│   │
│   ├── lib/
│   │   ├── __init__.py
│   │   └── biblioteca_sporturi.py
│   │
│   └── tests/
│       ├── __init__.py
│       └── test_biblioteca_sporturi.py
│
├── templates/
│   ├── index.html
│   ├── volei.html
│   ├── reguli.html
│   └── echipament.html
│
├── static/
│   └── images/
│       ├── volei.jpg
│       ├── reguli.jpg
│       └── echipament.jpg
│
└── doc/
    └── screenshots/
        ├── home.png
        ├── volei.png
        ├── reguli.png
        └── echipament.png
```

---

## 4. Fișiere adăugate sau modificate

- `sporturi.py`
- `app/lib/biblioteca_sporturi.py`
- `app/tests/test_biblioteca_sporturi.py`
- `templates/reguli.html`
- `templates/echipament.html`
- `requirements.txt`
- `quickrequirements.txt`
- `pytest.ini`
- `Dockerfile`
- `dockerstart.sh`
- `Jenkinsfile`
- `activeaza_venv`
- `activeaza_venv_jenkins`
- `ruleaza_aplicatia`
- `README.md`

---

## 5. Rute disponibile

| Rută | Ce afișează |
|---|---|
| `/` | Pagina principală a aplicației |
| `/sporturi` | Pagina generală pentru tema Sporturi |
| `/sporturi/volei` | Pagina elementului ales, Volei |
| `/sporturi/volei/reguli` | Reguli generate prin `reguli_volei()` |
| `/sporturi/volei/echipament` | Echipamente generate prin `echipament_volei()` |

---

## 6. Stadiul proiectului

| Componentă | Stadiu |
|---|---|
| Aplicație Flask | Implementată |
| Rute pentru Volei | Implementate |
| Funcții în bibliotecă | Implementate |
| Teste cu pytest | Implementate și rulate local |
| Pylint | Rulat local |
| Dockerfile | Configurat |
| Jenkinsfile | Configurat |
| Capturi aplicație locală | Adăugate |
| Capturi Docker/Jenkins | De adăugat după rulare |

---

# Testare și rulare

## 7. Rulare locală

Pentru pregătirea mediului virtual se folosește:

```bash
. ./activeaza_venv_jenkins
```

Pentru pornirea aplicației:

```bash
. ./activeaza_venv
. ./ruleaza_aplicatia
```

Aplicația pornește pe portul `5000` și poate fi accesată la:

```text
http://127.0.0.1:5000/sporturi
```

Rutele verificate local:

- `http://127.0.0.1:5000/sporturi`
- `http://127.0.0.1:5000/sporturi/volei`
- `http://127.0.0.1:5000/sporturi/volei/reguli`
- `http://127.0.0.1:5000/sporturi/volei/echipament`

---

## 8. Capturi aplicație

### Pagina Sporturi

![Pagina Sporturi](doc/screenshots/home.png)

### Pagina Volei

![Pagina Volei](doc/screenshots/volei.png)

### Pagina Reguli Volei

![Pagina Reguli](doc/screenshots/reguli.png)

### Pagina Echipament Volei

![Pagina Echipament](doc/screenshots/echipament.png)

---

## 9. Testare automată cu pytest

Testele sunt în fișierul:

```text
app/tests/test_biblioteca_sporturi.py
```

Comanda de rulare:

```bash
pytest
```

Rezultatul obținut local:

```text
4 passed
```

Testele verifică faptul că funcțiile `reguli_volei()` și `echipament_volei()` returnează HTML și conțin informații relevante despre Volei.

![Rezultat pytest](doc/pytest.png)

---

## 10. Verificare cu pylint

Pentru analiza statică am folosit `pylint`.

Comenzi:

```bash
export PYLINTHOME=.pylint.d
pylint --exit-zero app/lib/*.py
pylint --exit-zero app/tests/*.py
pylint --exit-zero sporturi.py
```

Rezultatul obținut local:

```text
Your code has been rated at 10.00/10
```

![Rezultat pylint](doc/pylint.png)

---

## 11. Containerizare Docker

Aplicația este pregătită pentru rulare în container.

Construirea imaginii:

```bash
docker build -t sporturi:v01 .
```

Pornirea containerului:

```bash
docker run --name sporturi1 -p 5000:5000 sporturi:v01
```

Ruta aplicației din container:

```text
http://127.0.0.1:5000/sporturi
```

Oprirea containerului:

```bash
docker stop sporturi1
docker rm sporturi1
```

Capturi pentru rularea Docker:

![Imagine Docker](doc/dockerimages.png)

![Consolă container](doc/dockerconsola.png)

![Container Docker](doc/dockerps.png)

![Pagina temă în container](doc/paginaTemaContainer.png)

---

## 12. Pipeline Jenkins

Pipeline-ul este definit în `Jenkinsfile` și este pregătit pentru rulare pe branch-ul:

```text
dev_bocai_alexandra
```

Etapele configurate sunt:

| Stage | Rol |
|---|---|
| `Build` | Creează mediul virtual și instalează dependențele |
| `pylint - calitate cod` | Rulează analiza statică |
| `Unit Testing cu pytest` | Rulează testele automate |
| `Deploy` | Construiește imaginea Docker și creează containerul |

Capturi pentru rularea Jenkins:

![Pipeline Jenkins Blue Ocean](doc/jenkinsBlueOcean.png)

![Pipeline Jenkins clasic](doc/jenkinsSimplu.png)

---

## 13. Integrare GitHub

Branch-ul de dezvoltare folosit:

```text
dev_bocai_alexandra
```

Branch-ul către care se va face Pull Request:

```text
main_bocai_alexandra
```

Fluxul de integrare:

```text
dev_bocai_alexandra -> main_bocai_alexandra
```

Status actual:

```text
Modificările au fost pregătite pe branch-ul de dezvoltare și urmează integrarea prin Pull Request.
```

---

## 14. Review Pull Request-uri

Această secțiune va fi completată după ce voi face review pentru Pull Request-ul unui coleg.

Model de completare:

```text
PR #<id> - Review pentru funcționalitatea <elementului>.
```

---

## 15. Ce mai este de făcut

- Crearea Pull Request-ului către `main_bocai_alexandra`;
- Obținerea unui review de la un coleg;
- Realizarea unui review pentru Pull Request-ul unui coleg.
