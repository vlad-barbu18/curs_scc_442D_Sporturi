# Proiect SCC - Sporturi

## Dezvoltator

- **Nume:** Iordanescu Razvan
- **Grupa:** 442D
- **Element alocat:** Padel

## Cuprins

- [Descriere generală](#descriere-generală)
- [Funcționalitate implementată](#funcționalitate-implementată)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuală în browser](#testare-manuală-în-browser)
- [Testare automată cu pytest](#testare-automată-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI](#devops-ci)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

## Descriere generală

Obiectivul proiectului a fost realizarea unei aplicații web folosind framework-ul Flask, împreună cu un flux complet de dezvoltare software bazat pe GitHub, Docker, Jenkins, pytest și pylint.

Tema proiectului este **sporturi**, iar elementul ales pentru implementare este **padel**.

Aplicația prezintă informații generale despre padel, echipamentul folosit și câteva reguli specifice acestui sport.

## Funcționalitate implementată

În acest branch am adăugat și personalizat aplicația pentru tema **sporturi** și elementul **padel**.

Fișierul `app/lib/biblioteca_sporturi.py` conține cele două funcții cerute:

- `functie_1_padel()` - returnează informații generale despre padel.
- `functie_2_padel()` - returnează informații despre echipament și reguli în padel.

Fișierul principal `sporturi.py` conține cele patru rute cerute:

- `/sporturi` - pagina principală a temei.
- `/sporturi/padel` - pagina elementului ales.
- `/sporturi/padel/functie_1_padel` - pagina cu prima informație despre padel.
- `/sporturi/padel/functie_2_padel` - pagina cu a doua informație despre padel.

Fișierul `app/tests/test_biblioteca_sporturi.py` conține testele automate pentru cele două funcții din bibliotecă.

## Stadiu dezvoltare

- Funcționalitate complet implementată.
- Cod adăugat în branch-ul `dev_iordanescu_razvan`.
- Aplicația Flask rulează local.
- Testele automate cu `pytest` trec cu succes.
- Verificarea codului cu `pylint` este integrată.
- Dockerfile și Jenkinsfile sunt funcționale.
- Aplicația rulează și în container Docker.
- Pipeline-ul Jenkins include etapele Build, pylint, Unit Testing și Deploy.

## Testare manuală în browser

Pentru rularea locală a aplicației:

```bash
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_iordanescu_razvan
source ./activeaza_venv
source ./ruleaza_aplicatia
```

Aplicația se accesează la:

```text
http://127.0.0.1:5012/sporturi
```

Rutele testate manual:

```text
http://127.0.0.1:5012/sporturi
http://127.0.0.1:5012/sporturi/padel
http://127.0.0.1:5012/sporturi/padel/functie_1_padel
http://127.0.0.1:5012/sporturi/padel/functie_2_padel
```

Capturi de ecran pentru rularea locală:

![Pagina tema - local](doc/paginaTemaLocal.png)
![Pagina element - local](doc/paginaElementLocal.png)
![Pagina functia 1 - local](doc/paginaFunctie1Local.png)
![Pagina functia 2 - local](doc/paginaFunctie2Local.png)

## Testare automată cu pytest

Testele automate se rulează cu:

```bash
pytest
```

Fișierul de teste este:

```text
app/tests/test_biblioteca_sporturi.py
```

Testele verifică dacă funcțiile:

- returnează conținut HTML valid;
- conțin informațiile specifice despre padel;
- returnează conținut nenul.

Captură rezultate pytest:

![Rezultate pytest](doc/pytest.png)

## Validare cod cu pylint

Verificarea codului se face cu:

```bash
pylint --exit-zero app/lib/biblioteca_sporturi.py
pylint --exit-zero app/tests/test_biblioteca_sporturi.py
pylint --exit-zero sporturi.py
```

Flag-ul `--exit-zero` permite afișarea avertismentelor fără oprirea pipeline-ului Jenkins.

Captură rezultate pylint:

![Rezultate pylint](doc/pylint.png)

## Testare cu Docker

Construirea imaginii Docker:

```bash
docker build -t sporturi:v01 .
```

Verificarea imaginii create:

```bash
docker images | grep sporturi
```

Rularea containerului:

```bash
docker run --name sporturi1 -p 8021:5012 sporturi:v01
```

Aplicația din container se accesează la:

```text
http://127.0.0.1:8021/sporturi
```

Rutele testate în container:

```text
http://127.0.0.1:8021/sporturi
http://127.0.0.1:8021/sporturi/padel
http://127.0.0.1:8021/sporturi/padel/functie_1_padel
http://127.0.0.1:8021/sporturi/padel/functie_2_padel
```

Oprirea și ștergerea containerului:

```bash
docker stop sporturi1
docker rm sporturi1
```

Capturi Docker:

![Imagine Docker](doc/dockerimages.png)
![Consola container](doc/dockerconsola.png)
![Container Docker](doc/dockerps.png)

Capturi aplicație rulată în container:

![Pagina tema - container](doc/paginaTemaContainer.png)
![Pagina element - container](doc/paginaElementContainer.png)
![Pagina functia 1 - container](doc/paginaFunctie1Container.png)
![Pagina functia 2 - container](doc/paginaFunctie2Container.png)

## DevOps CI

Pipeline-ul Jenkins este definit în fișierul `Jenkinsfile`.

Pipeline-ul conține patru etape:

1. **Build** - creează/activează mediul virtual și instalează dependențele.
2. **pylint - calitate cod** - rulează analiza statică a codului.
3. **Unit Testing cu pytest** - rulează testele automate.
4. **Deploy** - construiește imaginea Docker și creează containerul.

Repository-ul folosit în Jenkins:

```text
https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
```

Branch-ul folosit în Jenkins:

```text
*/dev_iordanescu_razvan
```

Capturi Jenkins:

![Pipeline Blue Ocean](doc/jenkinsBlueOcean.png)
![Pipeline Jenkins clasic](doc/jenkinsSimplu.png)

## Concluzii

Prin acest proiect am realizat o aplicație Flask simplă, organizată modular, pentru tema **sporturi** și elementul **padel**.

Proiectul folosește:

- Flask pentru aplicația web;
- GitHub pentru versionare;
- pytest pentru testare automată;
- pylint pentru verificarea calității codului;
- Docker pentru containerizare;
- Jenkins pentru automatizarea procesului de build, testare și deploy.

Aplicația poate fi rulată atât local, cât și într-un container Docker.

## Bibliografie

- https://github.com/crchende/sysinfo.git
- https://flask.palletsprojects.com/
- https://docs.docker.com/
- https://www.jenkins.io/doc/
