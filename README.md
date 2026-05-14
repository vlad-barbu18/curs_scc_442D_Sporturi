# curs_scc_442D_Sporturi — Patinaj artistic

## Cuprins
 
1. [Student](#student)
2. [Descriere aplicație](#descriere-aplicație)
3. [Funcționalitate adăugată](#funcționalitate-adăugată)
4. [Structura proiectului](#structura-proiectului)
5. [Configurare și rulare locală](#configurare-și-rulare-locală)
6. [Pagini WEB](#pagini-web)
7. [Testare cu pytest](#testare-cu-pytest)
8. [Verificare statică cu pylint](#verificare-statică-cu-pylint)
9. [Containerizare Docker](#containerizare-docker)
10. [DevOps CI — Jenkins](#devops-ci--jenkins)
11. [Integrare GitHub](#integrare-github)
12. [Pull Request-uri la care am făcut review](#pull-request-uri-la-care-am-făcut-review)
13. [Stadiul implementării](#stadiul-implementării)
14. [Ce mai este de făcut](#ce-mai-este-de-făcut)
15. [Bibliografie](#bibliografie)


## Student

**Nume:** Oprea Andreea 
**Grupă:** 442D
**Temă:** Sporturi
**Element ales:** Patinaj artistic


## Descriere aplicație

Aplicație WEB realizată în **Python / Flask** pentru tema **Sporturi**, elementul ales fiind **Patinaj artistic**.

Aplicația expune patru rute:

| Rută | Conținut |
|------|----------|
| `/sporturi` | Prezentare generală temă |
| `/sporturi/patinaj-artistic` | Prezentare element ales |
| `/sporturi/patinaj-artistic/sarituri` | Sărituri în patinaj artistic |
| `/sporturi/patinaj-artistic/echipamente` | Echipamente folosite |


## Funcționalitate adăugată

Fișier modificat: `app/lib/biblioteca_sporturi.py`

Funcții adăugate:

```python
sarituri_patinaj_artistic()   # informații despre Toe Loop, Salchow, Loop, Flip, Lutz, Axel
echipamente_patinaj_artistic() # informații despre patine, costum, mănuși, protecții, huse lame
```

Fișiere adăugate / modificate față de scheletul inițial:

```
sporturi.py
app/lib/biblioteca_sporturi.py
app/test/test_biblioteca_sporturi.py
static/images/poza_generala.jpeg
static/images/poza_sarituri.jpeg
static/images/poza_echipamente.png
Dockerfile
Jenkinsfile
requirements.txt
activeaza_venv
activeaza_venv_jenkins
README.md
```


## Structura proiectului

```
curs_scc_442D_Sporturi/
├── app/
│   ├── lib/
│   │   └── biblioteca_sporturi.py
│   └── test/
│       └── test_biblioteca_sporturi.py
├── doc/
│   └── screenshots/
├── static/
│   └── images/
│       ├── poza_generala.jpeg
│       ├── poza_sarituri.jpeg
│       └── poza_echipamente.png
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── activeaza_venv
├── activeaza_venv_jenkins
├── sporturi.py
└── README.md
```


## Configurare și rulare locală

**Dependențe** (`requirements.txt`): `flask`, `pytest`, `pylint`

```bash
# Activare / creare mediu virtual
. ./activeaza_venv

# Pornire aplicație
python3 sporturi.py
```

Aplicația este accesibilă la: `http://127.0.0.1:5000/sporturi`

## Pagini WEB

### `/sporturi`

![Pagina Sporturi](doc/screenshots/pagina_sporturi.png)

### `/sporturi/patinaj-artistic`

![Pagina Patinaj artistic](doc/screenshots/pagina_patinaj_artistic.png)

### `/sporturi/patinaj-artistic/sarituri`

![Pagina Sarituri](doc/screenshots/pagina_sarituri.png)

### `/sporturi/patinaj-artistic/echipamente`

![Pagina Echipamente](doc/screenshots/pagina_echipamente.png)


## Testare cu pytest

Fișier de test: `app/test/test_biblioteca_sporturi.py`

Funcții testate: `sarituri_patinaj_artistic()`, `echipamente_patinaj_artistic()`

Testarea verifică dacă funcțiile create în biblioteca aplicației returnează informațiile așteptate.
Astfel ne asigurăm că partea de funcționalitate adăugată pentru patinaj artistic merge corect înainte să fie integrată în branch-ul principal.

```bash
PYTHONPATH=. python3 -m pytest app/test
```

Rezultat:

![Testare pytest](doc/screenshots/testare_pytest.png)


## Verificare statică cu pylint

Pentru verificarea calității codului am folosit `pylint`.
Acesta analizează fișierele Python și afișează observații despre stil, structură, docstring-uri și posibile probleme de cod.
Opțiunea `--exit-zero` permite afișarea observațiilor fără ca rularea să fie considerată eșuată.

```bash
pylint --exit-zero app/lib/*.py app/test/*.py sporturi.py
```

![Testare pylint](doc/screenshots/testare_pylint.png)


## Containerizare Docker

### Build imagine

Pentru containerizarea aplicației am construit o imagine Docker pe baza fișierului `Dockerfile`. Prima comandă creează imaginea cu numele `sporturi-patinaj-app`, iar a doua verifică dacă imaginea apare în lista imaginilor locale.

```bash
docker build -t sporturi-patinaj-app .
docker images
```

![Docker images](doc/screenshots/docker_images.png)
### Rulare container

După crearea imaginii, am pornit aplicația într-un container Docker. Prima comandă rulează containerul `sporturi-patinaj-container` pe portul `5000`, iar a doua verifică dacă acesta este pornit.

```bash
docker run -d -p 5000:5000 --name sporturi-patinaj-container sporturi-patinaj-app
docker ps
```

![Docker ps](doc/screenshots/docker_ps.png)

Aplicația rulată din container este accesibilă în browser la:

```text
http://127.0.0.1:5000/sporturi
```

### Loguri container

Pentru a verifica faptul că aplicația este accesată din container, am afișat logurile containerului:

```bash
docker logs sporturi-patinaj-container
```

În loguri se văd cererile făcute din browser către rutele aplicației. Codul `200` indică încărcarea cu succes a paginii, iar `304` poate apărea pentru fișiere deja salvate în cache.

![Docker logs](doc/screenshots/docker_logs.png)

## DevOps CI — Jenkins

Pipeline-ul este definit în fișierul `Jenkinsfile` și rulează automat pașii principali pentru verificarea aplicației.

| Etapă | Descriere |
|-------|-----------|
| Build | Creează mediul virtual `.venv` și instalează dependențele folosind `activeaza_venv_jenkins` |
| pylint | Verifică static fișierele `app/lib/*.py`, `app/test/*.py` și `sporturi.py` |
| Unit Testing | Rulează testele cu `pytest app/test`; rezultatul așteptat este `4 passed` |
| Deploy | Etapă demonstrativă, unde se afișează un mesaj de deploy |

Screenshot rulare Jenkins:

![Jenkins pass](doc/screenshots/testare_j.png)



## Integrare GitHub

| Branch | Rol |
|--------|-----|
| `main_oprea_andreea` | Branch personal principal |
| `dev_oprea_andreea` | Branch personal de dezvoltare |

Fluxul de lucru:
1. Cod dezvoltat pe `dev_oprea_andreea`
2. Pull Request din `dev_oprea_andreea` → `main_oprea_andreea`
3. Minim un review de la un coleg înainte de merge
4. README integrat în `main` al grupei prin Pull Request separat

## Pull Request-uri la care am făcut review

<!-- Completeaz după review: -->
```
PR #<id> — <descriere scurtă PR coleg>
```

## Stadiul implementării

| Componentă | Status |
|-----------|--------|
| Cod aplicație Flask | Finalizat |
| Funcții `biblioteca_sporturi.py` | Finalizat |
| Rute WEB (4 rute) | Finalizat |
| Imagini locale | Finalizat |
| Teste pytest (4 passed) | Finalizat |
| Dockerfile | Finalizat |
| Container Docker | Finalizat |
| Jenkinsfile | Finalizat |
| Rulare Jenkins (screenshot PASS) | Finalizat |
| Pull Request `dev` → `main` | De creat |
| Review la PR coleg | De completat |
| README integrat în `main` grupă | De completat |


## Ce mai este de făcut

- [ ] Crea Pull Request din `dev_oprea_andreea` în `main_oprea_andreea`
- [ ] Obține minim un review de la un coleg
- [ ] Face review la Pull Request-ul unui coleg și nota ID-ul
- [ ] Integra README în branch-ul `main` al grupei

