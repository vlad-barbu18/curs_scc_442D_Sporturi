# curs_scc_442D_Sporturi
# Formula 1

Acest proiect reprezintă contribuția individuală pentru tema **Sporturi**, axată pe monitorizarea și afișarea datelor din competiția **Formula 1**.

---

## Cuprins
- [Student](#student)
- [Descriere aplicație](#descriere-aplicatie)
- [Funcționalități adăugate](#functionalitati-adaugate)
- [Structura proiectului](#structura-proiectului)
- [Configurare și rulare locală](#configurare-si-rulare-locala)
- [Pagini WEB](#pagini-web)
- [Testare cu pytest](#testare-cu-pytest)
- [Verificare statică cu pylint](#verificare-statica-cu-pylint)
- [Containerizare Docker](#containerizare-docker)
- [DevOps CI - Jenkins](#devops-ci-jenkins)
- [Integrare GitHub](#integrare-github)
- [Reviewed PRs](#reviewed-pr)
- [Stadiul implementării](#stadiul-implementarii)
- [Ce mai este de făcut](#ce-mai-este-de-facut)
- [Bibliografie](#bibliografie)

---

## <a name="student"></a> 1. Student
* **Nume:** Stancu Andreea
* **Grupă:** 442D
* **Repository:** `curs_scc_442D_Sporturi`
* **Branch Dezvoltare:** `dev_stancu_andreea`

## <a name="descriere-aplicatie"></a> 2. Descriere aplicație
Aplicația este un dashboard interactiv dezvoltat în **Python** folosind framework-ul **Flask**. Obiectivul principal este de a oferi informații rapide despre clasamentul piloților (Podium) și detalii tehnice despre circuitele din calendarul Formula 1.

## <a name="functionalitati-adaugate"></a> 3. Funcționalități adăugate
1.  **Ruta Home (`/`)**: Interfață interactivă cu butoane stilizate pentru navigare ușoară.
2.  **Ruta Podium (`/formula1`)**: Afișează dinamic primii trei piloți (Max Verstappen, Lando Norris, Charles Leclerc).
3.  **Ruta Circuite (`/circuit/<nume>`)**: Afișează descrieri specifice pentru circuite (ex. Monaco, Spa-Francorchamps).
4.  **Logică Backend separată**: Toate datele sunt procesate într-o bibliotecă dedicată în `app/lib/`.

## <a name="structura-proiectului"></a> 4. Structura proiectului
```text
curs_scc_442D_Sporturi/
├── sporturi.py           # Aplicația principală Flask (Rutele)
├── requirements.txt      # Dependențe (Flask, Pytest, Pylint)
├── Dockerfile            # Configurare containerizare
├── Jenkinsfile           # Pipeline CI declarative
├── app/
│   ├── __init__.py       # Marcaj pachet Python
│   └── lib/
│       ├── __init__.py
│       └── f1_logic.py    # Logica de business (Funcții)
├────── test_f1.py        # Teste unitare
└── media/                # Capturi de ecran (Dovezi)
```

## <a name="configurare-si-rulare-locala"></a> 5. Configurare și rulare locală
Pentru rularea aplicației în afara containerului (pentru dezvoltare rapidă), se urmează pașii:
* **Instalare dependințe**: Se utilizează fișierul `requirements.txt`.
  ```bash
  pip install -r requirements.txt
  ```
* **Lansare server Flask**: 
  ```bash
  python sporturi.py
  ```
* **Accesare**: 
  ```bash
  Aplicația este disponibilă la http://127.0.0.1:5000.
  ```

## <a name="pagini-web"></a> 6. Pagini WEB
Interfața este construită conform cerințelor de a avea rute pentru temă, element și informații specifice:
* **Home (`/`)**: Pagina de start cu butoane de navigare.
* **Tema (`/formula1`)**: Afișează podiumul piloților obținut prin funcția `primii_trei_piloti()`.
* **Elemente (`/circuit/Monaco`, `/circuit/Spa`)**: Detalii specifice extrase prin funcția `detalii_circuit()`.

<br>
<br> <img width="1027" height="334" alt="WhatsApp Image 2026-05-14 at 18 19 09" src="https://github.com/user-attachments/assets/97c9a8b4-ce19-4bc7-9474-54ac35ecbe01" />
<br>
Captură de ecran: Interfața web accesată din browser, demonstrând accesibilitatea funcționalității
<br>

<br> <img width="736" height="395" alt="WhatsApp Image 2026-05-14 at 18 19 35" src="https://github.com/user-attachments/assets/3ac0ea14-2db7-4d92-abe0-f246b9e7b906" />
<br>
Captură de ecran: Buton Podium
<br>

<br> <img width="1131" height="388" alt="WhatsApp Image 2026-05-14 at 18 20 26" src="https://github.com/user-attachments/assets/4e5c6a6a-a584-4c41-9871-ed4ae7919354" />

Captură de ecran: Buton Circuit Spa
<br>

<br> <img width="994" height="414" alt="WhatsApp Image 2026-05-14 at 18 20 02" src="https://github.com/user-attachments/assets/3661a752-5da3-43b9-919b-16d75933fb20" />
<br>
Captură de ecran: Buton Circuit Monaco
<br>
<br>

## <a name="testare-cu-pytest"></a> 7. Testare cu pytest
Verificarea funcționalității se face prin unit-tests pentru a asigura calitatea codului adăugat:
* **Execuție**: Testele verifică dacă lista de piloți are exact 3 elemente și dacă numele sunt corecte conform logicii de business.
* **Comandă**: `pytest tests/test_f1.py`.
* **Integrare**: Rezultatele sunt raportate automat în etapa de testare a pipeline-ului Jenkins.

## <a name="verificare-statica-cu-pylint"></a> 8. Verificare statică cu pylint
Pentru asigurarea calității codului, am folosit analiza statică (code review automatizat):
* Am verificat conformitatea codului din `sporturi.py` și `app/lib/f1_logic.py` cu standardele Python (PEP8).
* Obiectivul este menținerea unui scor ridicat de mentenabilitate și eliminarea erorilor potențiale înainte de integrare.
<img width="1600" height="119" alt="pylint" src="https://github.com/user-attachments/assets/5a3817a4-8f8a-4053-9c85-e8e325dfedf5" />


## <a name="containerizare-docker"></a> 9. Containerizare Docker
Aplicația a fost containerizată folosind un `Dockerfile` prezent pe branch-ul de dezvoltare.

* **Imaginea**: Creată pentru a include tot mediul de rulare și dependințele necesare (Python, Flask).
  <img width="512" height="73" alt="imagine_docker" src="https://github.com/user-attachments/assets/1bade727-25cf-4805-985f-cffef06f192d" />

* **Containerul**: Instanțiat și pornit pe baza imaginii pentru a izola execuția aplicației.
  <img width="1600" height="183" alt="container_creat_up" src="https://github.com/user-attachments/assets/fbf1e5f2-ae8d-42d7-8a62-3917e4042cb6" />

* **Validare**: Log-urile din consolă demonstrează că apelurile din browser sunt procesate de container, atestând legătura funcțională.
  <img width="1600" height="371" alt="mesaje_consola" src="https://github.com/user-attachments/assets/3dfa00b1-d7d8-4caa-9ada-38e3c83535bc" />


## <a name="devops-ci-jenkins"></a> 10. DevOps CI - Jenkins
Procesul de integrare continuă este gestionat printr-un pipeline declarativ definit în fișierul `Jenkinsfile`.

* **Etape automate**: Checkout, Build, Unit Tests (Pytest), Docker Build.
* **Trigger**: Pipeline-ul rulează automat la fiecare `push` pe branch-ul `dev_stancu_andreea`.

<img width="1600" height="643" alt="BlueOcean_pass" src="https://github.com/user-attachments/assets/fe98cc47-eadc-4aba-853e-225ec3b8bd21" />


## <a name="integrare-github"></a> 11. Integrare GitHub
Sistemul de versionare Git este utilizat pentru managementul codului și colaborare.

* **Colaborare**: Repository-ul `curs_scc_442D_Sporturi` permite lucrul colaborativ prin adăugarea colegilor ca parteneri.
* **Flux Branch-uri**: Se utilizează `dev_stancu_andreea` pentru modificări locale și `main_stancu_andreea` pentru integrare intermediară.
* **Pull Request (PR)**: Orice integrare în `main` necesită minim un review de la un coleg de grupă pentru a asigura calitatea aplicației.

## <a name="reviewed-pr"></a> 12. Reviewed PRs
Conform cerințelor de colaborare, am participat la procesul de evaluare a codului (Code Review) pentru colegii de echipă:
* **PR ID**: #12
* **Coleg**: [Nume Coleg]
* **Status**: **Approved** (Validat după verificarea conformității cu standardele proiectului).

## <a name="stadiul-implementarii"></a> 13. Stadiul implementării
Următorul tabel centralizează progresul final al tuturor componentelor atribuite:

| Componentă | Status | Observații |
| :--- | :--- | :--- |
| **Funcționalitate** | Gata (100%) | Toate rutele Flask sunt operative. |
| **Testare Unitară** | Gata (PASS) | Testele Pytest trec cu succes în Jenkins. |
| **Containerizare** | Gata (Finalizat) | Imagine Docker creată și testată local. |
| **Documentare** | Gata (100%) | README completat conform stilului *sysinfo*. |
<img width="272" height="488" alt="teste_passed" src="https://github.com/user-attachments/assets/364e3f99-3f29-49e7-a627-c0d64901800d" />


## <a name="ce-mai-este-de-facut"></a> 14. Ce mai este de făcut
Planificarea sarcinilor curente și viitoare:
- [x] Integrare logică F1 în aplicația Flask.
- [x] Reparare aserțiuni teste (corectare index `[0]` pentru validarea lui Max Verstappen).
- [ ] **Integrarea finală a README-ului** în branch-ul `main` (după primirea review-ului de la coleg).
- [ ] Închiderea Pull Request-ului după validarea finală a echipei de coordonare.

## <a name="bibliografie"></a> 15. Bibliografie
Resursele utilizate pentru documentarea și implementarea acestui proiect:
1. **Îndrumar Proiect SCC** - Ciprian Chende, Cornelia Bădoi (Ghidul oficial de laborator).
2. **Documentație Flask** - [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/) (Resursa oficială pentru rute și server web).
3. **Exemplu Proiect sysinfo** - [https://github.com/crchende/sysinfo](https://github.

---
*Proiect realizat de: Stancu Andreea-Beatrice, grupa 442D*
