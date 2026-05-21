# Proiect SCC - Sporturi

## Dezvoltator
- **Nume:** Baditeanu Madalina
- **Grupa:** 442D
- **Element alocat:** Tir cu arcul

## Cuprins
- [Descriere generala](#descriere-generala)
- [Functionalitate implementata](#functionalitate-implementata)
- [Stadiu dezvoltare](#stadiu-dezvoltare)
- [Testare manuala in browser (rulare locala)](#testare-manuala-in-browser-rulare-locala)
- [Testare automata cu pytest](#testare-automata-cu-pytest)
- [Validare cod cu pylint](#validare-cod-cu-pylint)
- [Testare cu Docker](#testare-cu-docker)
- [DevOps CI](#devops-ci)
- [Pull Requests review](#pull-requests-review)
- [Concluzii](#concluzii)
- [Bibliografie](#bibliografie)

## Descriere generala

Obiectivul proiectului a fost realizarea unei aplicatii web folosind framework-ul Flask, parcurgerea unui proces complet de dezvoltare software in care folosim Jenkins, Docker, Python, GitHub pentru versionare, containerizare, programare si automatizare.

## Functionalitate implementata

In acest branch am adaugat si personalizat:

- Fisierul `app/lib/biblioteca_sporturi.py` cu cele doua functii cerute:
  - `reguli_tir_cu_arcul()` - returneaza HTML cu regulile de baza ale tirului cu arcul.
  - `campioni_tir_cu_arcul()` - returneaza HTML cu campioni mondiali celebri 
- Fisierul principal `sporturi.py` cu cele patru rute conform cerintei:
  - `/sporturi` - pagina principala a temei.
  - `/sporturi/tir_cu_arcul` - pagina elementului ales.
  - `/sporturi/tir_cu_arcul/reguli_tir_cu_arcul` - regulile tirului cu arcul.
  - `/sporturi/tir_cu_arcul/campioni_tir_cu_arcul` - campionii la tir cu arcul.

- Fisierul `app/tests/test_biblioteca_sporturi.py` cu 8 teste automate.

## Stadiu dezvoltare

- Functionalitate complet implementata.
- Cod adaugat in branch-ul `dev_baditeanu_madalina`.
- Dockerfile si Jenkinsfile sunt functionale.
- Testare locala, automata si containerizata realizata cu succes.

## Testare manuala in browser (rulare locala)

```bash
git clone <url-repo>
cd <folder-repo>
git checkout dev_baditeanu_madalina
. ./activeaza_venv
./ruleaza_aplicatia
```

Aplicatia se acceseaza la: `http://127.0.0.1:5012/sporturi`

![Pagina sporturi - local](doc/paginaSporturiLocal.png)
![Pagina tir cu arcul - local](doc/paginaTirCuArculLocal.png)
![Pagina reguli - local](doc/paginaReguliLocal.png)
![Pagina campioni - local](doc/paginaCampioniLocal.png)

## Testare automata cu `pytest`

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

![Imagine Docker](doc/dockerimages.png)
![Consola container](doc/dockerconsola.png)

Aplicatia din container, accesata la `http://localhost:8021/sporturi`:

![Pagina sporturi - container](doc/paginaSporturiContainer.png)
![Pagina tir cu arcul - container](doc/paginaTirCuArculContainer.png)
![Pagina reguli - container](doc/paginaReguliContainer.png)
![Pagina campioni - container](doc/paginaCampioniContainer.png)

## DevOps CI

Pipeline declarativ definit in `Jenkinsfile`, cu 4 stages:
1. **Build** - creare venv si instalare dependente
2. **pylint** - analiza statica a codului (warning-only, `--exit-zero`)
3. **Unit Tests** - rulare teste cu pytest
4. **Deploy** - build imagine Docker si creare container

![Jenkins pipeline](doc/jenkins.png)
![Jenkins pipeline1](doc/jenkins1.png)


## Concluzii

- **Dezvoltare modulara:** aplicatie Flask cu separarea datelor si logicii in fisiere dedicate.
- **Portabilitate:** Docker asigura rulare consistenta indiferent de mediu.
- **Automatizare:** Jenkins automatizeaza testarea si deploy-ul la fiecare push.
- **Asigurarea calitatii:** pytest si pylint integrate in pipeline CI/CD.

## Bibliografie

https://github.com/crchende/sysinfo.git
