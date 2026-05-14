# Proiect SCC - Sistem Monitorizare Formula 1 (Grupă 442D)

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





---
*Proiect realizat de: Stancu Andreea-Beatrice, grupa 442D*
