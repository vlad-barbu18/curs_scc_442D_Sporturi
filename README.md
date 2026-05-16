# curs_scc_442D_Sporturi — Volei

---

# Cuprins

1. [Student](#student)
2. [Prezentare proiect](#prezentare-proiect)
3. [Functionalitate implementata](#functionalitate-implementata)
4. [Structura aplicatiei](#structura-aplicatiei)
5. [Rulare locala](#rulare-locala)
6. [Pagini WEB disponibile](#pagini-web-disponibile)
7. [Testare automata](#testare-automata)
8. [Analiza statica cu pylint](#analiza-statica-cu-pylint)
9. [Containerizare Docker](#containerizare-docker)
10. [Integrare Jenkins](#integrare-jenkins)
11. [Utilizare GitHub](#utilizare-github)
12. [Review pentru Pull Request-uri](#review-pentru-pull-request-uri)
13. [Stadiul proiectului](#stadiul-proiectului)
14. [Posibile imbunatatiri](#posibile-imbunatatiri)
15. [Resurse utilizate](#resurse-utilizate)

---

# Student

- Bocai Alexandra

---

# Prezentare proiect

Acest proiect a fost realizat folosind limbajul Python si framework-ul Flask.
Tema aleasa pentru implementare este sportul Volei.

Aplicatia WEB permite utilizatorului sa navigheze intre mai multe pagini
care contin informatii despre:
- sportul Volei
- regulile de joc
- echipamentele utilizate

Scopul proiectului este dezvoltarea unei aplicatii simple folosind concepte
de programare, testare automata si containerizare Docker.

---

# Functionalitate implementata

In cadrul aplicatiei au fost dezvoltate urmatoarele functionalitati:

- pagina principala pentru sporturi
- pagina dedicata sportului Volei
- prezentarea regulilor principale din volei
- prezentarea echipamentelor utilizate
- utilizarea imaginilor statice
- navigare intre pagini prin link-uri si butoane
- stilizare HTML/CSS simpla

Aplicatia foloseste Flask pentru gestionarea rutelor si afisarea template-urilor HTML.

---

# Structura aplicatiei

```text
app/
static/
templates/
sporturi.py
requirements.txt
Dockerfile
Jenkinsfile
README.md
```
