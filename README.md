### Proiect SCC - Sporturi

#### Dezvoltator
*   **Nume:** Dumitrascu Alexandru
*   **Grupa:** 442D
*   **Element alocat:** Polo pe apa
*   **Branch dezvoltare:** dev_dumitrascu_alexandru
*   **Branch personal main:** main_dumitrascu_alexandru

---

#### Cuprins
1. [Descriere generala](#descriere-generala)
2. [Functionalitate implementata](#functionalitate-implementata)
3. [Rulare locala](#rulare-locala)
4. [Testare automata si analiza cod](#testare-automata-si-analiza-cod)
5. [Testare cu Docker](#testare-cu-docker)
6. [DevOps CI cu Jenkins](#devops-ci-cu-jenkins)
7. [Probleme intalnite si rezolvari](#probleme-intalnite-si-rezolvari)
8. [Concluzii](#concluzii)

---

#### 1. Descriere generala
Obiectivul acestui proiect a fost realizarea unei aplicatii web folosind framework-ul Flask si parcurgerea unui proces complet de dezvoltare software (DevOps), in care am utilizat tehnologii precum Git, GitHub, Docker si Jenkins.

Tema generala a proiectului este **Sporturi**, iar elementul pe care l-am ales si detaliat este **Polo pe apa**. Aplicatia ofera utilizatorilor detalii fascinante despre acest sport de echipa intens, prezentand regulamentul specific de joc si echipamentul necesar desfasurarii acestuia. Polo pe apa este recunoscut pentru cerintele sale fizice extreme, combinand inotul de rezistenta cu tactica handbalului.

Prin acest proiect s-a urmarit crearea unei aplicatii web functionale, cu o structura modulara, care sa respecte toate etapele unui flux de integrare si livrare continua (CI/CD).

---

#### 2. Functionalitate implementata
Aplicatia este construita pe baza framework-ului Flask si are o structura organizata, codul pentru date fiind separat de logica de rutare.

Fisierele principale dezvoltate:
*   `sporturi.py` - fisierul principal al aplicatiei Flask;
*   `app/lib/biblioteca_sporturi.py` - contine functiile `reguli_polo()` si `echipament_polo()`;
*   `app/tests/test_biblioteca_sporturi.py` - contine testele automate scrise cu pytest.

Aplicatia expune 4 rute functionale:
1.  `/sporturi` - pagina principala a temei Sporturi.
2.  `/sporturi/polo` - pagina dedicata sportului Polo pe apa.
3.  `/sporturi/polo/reguli_polo` - afiseaza detalii despre regulament.
4.  `/sporturi/polo/echipament_polo` - afiseaza detalii despre echipament.

---

#### 3. Rulare locala
Pentru a rula proiectul local pe masina de dezvoltare Ubuntu:
```bash
git clone https://github.com/crchende/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_dumitrascu_alexandru
source ./activeaza_venv
source ./ruleaza_aplicatia
Aplicatia poate fi accesata in browser la http://127.0.0.1:5012/sporturi.

--------------------------------------------------------------------------------
4. Testare automata si analiza cod
Pytest: Pentru a valida integritatea functiilor de backend, am implementat 4 teste unitare. Acestea verifica daca functiile returneaza continut HTML valid si daca informatiile specifice (markeri precum "Jucatori" sau "Casca") sunt prezente in raspunsul generat. Rularea testelor se face folosind comanda pytest, toate testele trecand cu succes.
Pylint: Am utilizat linter-ul pylint pentru a analiza calitatea codului din fisierele python, setand flag-ul --exit-zero pentru a afisa recomandarile de formatare fara a intrerupe pipeline-ul de build.

--------------------------------------------------------------------------------
5. Testare cu Docker
Pentru a asigura portabilitatea aplicatiei, am containerizat-o folosind Docker. Aceasta abordare garanteaza ca aplicatia va rula identic indiferent de mediul gazda.
Construire imagine: docker build -t sporturi:v01 .
Rulare container: docker run --name sporturi1 -p 8021:5012 sporturi:v01
Aplicația containerizata se acceseaza la http://localhost:8021/sporturi. Dovada rularii containerelor si imaginilor create este documentata prin capturile de ecran din folderul doc/ (dockerimages.png, dockerconsola.png, dockerps.png).

--------------------------------------------------------------------------------
6. DevOps CI cu Jenkins
Am automatizat ciclul de viata al aplicatiei printr-un pipeline declarativ definit in Jenkinsfile. Acesta contine 4 etape majore:
Build - preia codul si activeaza mediul virtual.
pylint - calitate cod - asigura o analiza statica a codului sursa.
Unit Testing cu pytest - ruleaza testele unitare pentru a preveni regresiile.
Deploy - incheie ciclul prin construirea automata a noii imagini Docker si lansarea noului container.

--------------------------------------------------------------------------------
7. Probleme intalnite si rezolvari
Pe parcursul dezvoltarii proiectului m-am lovit de cateva obstacole practice care au necesitat adaptare:
Limitari ale buffer-ului din terminalul Ubuntu: La copierea blocurilor mari de cod Python si HTML direct in terminalul masinii virtuale, buffer-ul tindea sa amestece si sa piarda caractere. Rezolvare: Am folosit un editor de text precum nano pentru a ocoli limitarile terminalului, asa cum este si procedura standard.
Erori la importul modulelor Python: Initial rularea testelor dadea eroare din cauza lipsei recunoasterii pachetelor. Rezolvare: Am adaugat fisiere goale __init__.py in folderele app, lib si tests, specificand astfel compilatorului Python ca acele directoare trebuie tratate ca pachete.

--------------------------------------------------------------------------------
8. Concluzii
Proiectul a demonstrat tranzitia cu succes de la un cod simplu scris pe o masina locala, la a avea o aplicatie distribuibila si containerizata. Implementarea fluxului CI/CD prin Jenkins si Docker ofera o perspectiva clara asupra modului in care se asigura calitatea, scalabilitatea si portabilitatea aplicatiilor in mediul enterprise.

--------------------------------------------------------------------------------
Bibliografie
Documentatie cerinte curs SCC: "CerinteProiectCursv2.pdf"
Flask Documentation: https://flask.palletsprojects.com/
Docker Hub Documentation: https://docs.docker.com/
Jenkins Pipeline Syntax: https://www.jenkins.io/doc/book/pipeline/syntax/

