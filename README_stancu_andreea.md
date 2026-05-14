
# Formula 1 - Stancu Andreea

Acest proiect reprezintă o aplicație de monitorizare a datelor din Formula 1, dezvoltată ca parte a laboratorului de Servicii Cloud și Containerizare.

## 1. Funcționalitate adaugata
Am implementat o aplicație web folosind **Flask** care permite vizualizarea datelor despre Formula 1:
- **Podium Actual**: Afișeaza primii trei piloți din clasament.
- **Detalii Circuite**: Ofera informatii specifice despre circuite faimoase (ex: Monaco, Spa, Monza).
- **Interfata Interactiva**: Navigare prin butoane stilizate direct din browser.

## 2. Stadiul implementarii
- [x] Cod logica F1 (`app/lib/f1_logic.py`) - **Finalizat**
- [x] Aplicatie Flask (`sporturi.py`) - **Finalizat**
- [x] Teste Unitare (`test_f1.py`) - **Finalizat**
- [x] Dockerfile pentru containerizare - **Finalizat**
- [x] Configurare Pipeline Jenkins - **Finalizat**

## 3. Testare
Testarea automata este realizata cu **Pytest** prin intermediul **Jenkins**.
- **Rezultat Jenkins**: PASS
  <img width="1600" height="643" alt="BlueOcean_pass" src="https://github.com/user-attachments/assets/39298652-5cd7-440c-8fe7-0ec6ac180e8f" />

- **Unit Tests**: Toate testele pentru verificarea listei de piloti si a lungimii podiumului au trecut cu succes.
  <img width="272" height="488" alt="teste_passed" src="https://github.com/user-attachments/assets/9142e612-70ab-41a7-9461-bedadea96f88" />


## 4. Integrare (Pull Requests)
- **PR catre main**: Creat pentru integrarea functionalitatii din branch-ul `dev_stancu_andreea`.
- **Review-uri oferite**: Am efectuat review pentru colegul [Nume Coleg] la PR-ul cu ID #123.

## 5. Containerizare
Aplicația este complet containerizata si poate fi rulata pe orice sistem cu Docker instalat.

### Dovezi execuție:

**A. Imaginea de container creata**
Se observa imaginea `f1-app-stancu-andreea` in lista de imagini locale.
<img width="512" height="73" alt="imagine_docker" src="https://github.com/user-attachments/assets/46de0efd-e699-4144-a337-ff78c887e711" />


**B. Containerul creat pe baza imaginii**
Containerul `container_f1_andreea` in stare **Up**, cu portul 5000 mapat.
<img width="1600" height="183" alt="container_creat_up" src="https://github.com/user-attachments/assets/fc56c09d-93f3-448b-afd1-6412df64984f" />


**C. Browserul care acceseaza aplicatia**
Interfata cu butoane accesata la `http://localhost:5000/formula1`.


**D. Mesajele afisate in consola**
Log-urile `GET` care atesta comunicarea dintre browser si container.
<img width="1600" height="371" alt="mesaje_consola" src="https://github.com/user-attachments/assets/3c3c0bf0-cc44-46b5-95e2-af3b358c2dd7" />


---
*Proiect realizat de: Stancu Andreea (Grupă 442D)*
