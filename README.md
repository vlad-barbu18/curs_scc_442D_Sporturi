Proiect SCC - Sporturi
Dezvoltator
Nume: Dumitrașcu Alexandru
Grupa: 442D
Element alocat: Polo pe apă
Branch dezvoltare: dev_dumitrascu_alexandru
Branch personal main: main_dumitrascu_alexandru

--------------------------------------------------------------------------------
Cuprins
Descriere generală
Funcționalitate implementată
Stadiu dezvoltare
Testare manuală în browser (rulare locală)
Testare automată cu pytest
Validare cod cu pylint
Testare cu Docker
DevOps CI cu Jenkins
Probleme întâlnite și rezolvări
Concluzii
Bibliografie

--------------------------------------------------------------------------------
Descriere generală
Obiectivul acestui proiect a fost realizarea unei aplicații web folosind framework-ul Flask și parcurgerea unui proces complet de dezvoltare software, în care sunt utilizate tehnologii precum Python, GitHub, Docker și Jenkins. Tema generală a proiectului este Sporturi, iar elementul ales pentru implementare este Polo pe apă. Aplicația prezintă informații generale despre regulamentul jocului și echipamentul utilizat de jucători.
Funcționalitate implementată
În cadrul proiectului am implementat o aplicație Flask, iar funcționalitatea principală este împărțită în mai multe fișiere:
sporturi.py - fișierul principal al aplicației Flask cu cele 4 rute definite;
app/lib/biblioteca_sporturi.py - biblioteca în care sunt definite funcțiile pentru polo pe apă (reguli_polo() și echipament_polo());
app/tests/test_biblioteca_sporturi.py - fișierul cu teste automate;
Dockerfile - fișierul folosit pentru containerizarea aplicației;
dockerstart.sh - scriptul de pornire a aplicației în container;
Jenkinsfile - fișierul folosit pentru automatizarea procesului de build, testare și deploy;
quickrequirements.txt - fișierul cu dependențele Python.
Stadiu dezvoltare
Stadiul actual al proiectului este complet funcțional.
Rutele Flask și funcțiile bibliotecii sunt testate automat cu pytest și validate cu pylint.
Aplicația a fost rulată local în browser.
Aplicația a fost containerizată cu succes utilizând Docker (imaginea construită și container rulat).
Pipeline-ul Jenkins pentru build, testare și deploy a funcționat cu succes.
Cele 16 capturi de ecran au fost adăugate în documentație.

--------------------------------------------------------------------------------
Testare manuală în browser (rulare locală)
Pentru rularea locală a proiectului:
git clone https://github.com/vlad-barbu18/curs_scc_442D_Sporturi.git
cd curs_scc_442D_Sporturi
git checkout dev_dumitrascu_alexandru
. ./activeaza_venv
./ruleaza_aplicatia
Aplicația se accesează la adresa: http://127.0.0.1:5012/sporturi
Capturile de mai jos prezintă cele patru rute ale aplicației, accesate în browser în timpul rulării locale:    

--------------------------------------------------------------------------------
Testare automată cu pytest
Pentru verificarea funcțiilor implementate, au fost scrise teste automate:
pytest
Rezultatul testelor automate: 

--------------------------------------------------------------------------------
Validare cod cu pylint
Pentru verificarea calității codului a fost utilizat pylint:
pylint --exit-zero app/lib/biblioteca_sporturi.py
pylint --exit-zero app/tests/test_biblioteca_sporturi.py
pylint --exit-zero sporturi.py
Rezultatul analizei statice: 

--------------------------------------------------------------------------------
Testare cu Docker
Aplicația a fost containerizată pentru a asigura portabilitatea.
docker build -t sporturi:v01 .
docker run --name sporturi1 -p 8021:5012 sporturi:v01
Mai jos regăsiți dovezile containerizării cu succes (creare imagine, pornire și rulare container):   
Aplicația din container se accesează la http://localhost:8021/sporturi. Capturile de mai jos prezintă funcționarea perfectă a aplicației direct din interiorul containerului Docker:    

--------------------------------------------------------------------------------
DevOps CI cu Jenkins
A fost definit un pipeline declarativ în fișierul Jenkinsfile, format din 4 etape automatizate:
Build - activează mediul virtual și pregătește dependențele.
pylint - calitate cod - realizarea analizei statice a codului Python (warning-only).
Unit Testing cu pytest - rularea testelor automate pentru validarea funcționalității.
Deploy - construirea imaginii Docker și crearea noului container.
Execuția reușită a pipeline-ului Jenkins:   

--------------------------------------------------------------------------------
Probleme întâlnite și rezolvări
Erori la importul modulelor Python: S-a generat eroarea ModuleNotFoundError: No module named app.lib. S-a rezolvat prin adăugarea forțată a folderului ascuns folosind comanda git add -f app/lib/init.py.
Permisiuni Docker pe Jenkins: A fost necesară rularea comenzii sudo usermod -aG docker jenkins pentru ca etapa de Deploy să poată rula comenzi Docker fără restricții.
Port / Container deja existent: Dacă primeam eroare că numele este în uz, am curățat containerele vechi folosind docker rm -f sporturi1.

--------------------------------------------------------------------------------
Concluzii
Proiectul demonstrează utilizarea practică a unui flux complet de lucru DevOps. Am respectat principiile de dezvoltare modulară în Flask, asigurând portabilitatea prin Docker și o rată înaltă de automatizare prin testare continuă și livrare (CI/CD) folosind Jenkins.
Bibliografie
