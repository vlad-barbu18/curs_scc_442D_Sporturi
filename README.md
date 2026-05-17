# Proiect SCC - Sporturi

## Dezvoltator

- **Nume:** Andriu Cosmin
- **Grupa:** 442D
- **Element ales:** Biliard
- **Branch de lucru:** `dev_andriu_cosmin`

---

## Cuprins

1. [Descriere generală](#descriere-generală)
2. [Funcționalitate implementată](#funcționalitate-implementată)
3. [Structura aplicației](#structura-aplicației)
4. [Rulare locală](#rulare-locală)
5. [Pagini disponibile](#pagini-disponibile)
6. [Testare automată cu pytest](#testare-automată-cu-pytest)
7. [Containerizare Docker](#containerizare-docker)
8. [Integrare Jenkins](#integrare-jenkins)
9. [Concluzii](#concluzii)
10. [Bibliografie](#bibliografie)

---

## Descriere generală

Acest proiect are ca scop realizarea unei aplicații web simple folosind framework-ul Flask. Tema generală a proiectului este **Sporturi**, iar elementul ales pentru implementare este **biliardul**.

Proiectul urmărește parcurgerea unui flux complet de dezvoltare software: versionare cu Git și GitHub, implementare în Python/Flask, testare automată cu pytest, containerizare cu Docker și automatizare CI/CD prin Jenkins.

---

## Funcționalitate implementată

În cadrul proiectului a fost implementată o aplicație Flask care conține pagini HTML pentru tema aleasă și pentru elementul selectat.

Funcționalitățile implementate sunt:

- pagină principală pentru tema **Sporturi**;
- pagină dedicată sportului **Biliard**;
- două funcții Python în biblioteca `app/lib/biblioteca_sporturi.py`;
- două rute separate care afișează rezultatul funcțiilor;
- teste automate pentru verificarea funcțiilor;
- rulare locală și rulare în container Docker;
- pipeline Jenkins cu etape de build, pylint, pytest și deploy.

---

## Structura aplicației

Fișierele principale ale proiectului sunt:

```text
sporturi.py
app/
  lib/
    biblioteca_sporturi.py
  tests/
    test_biblioteca_sporturi.py
Dockerfile
dockerstart.sh
Jenkinsfile
quickrequirements.txt
pytest.ini
README.md
doc/
