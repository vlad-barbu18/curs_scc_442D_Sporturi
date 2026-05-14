
# Formula 1 - Stancu Andreea

Acest proiect reprezinta o aplicatie de monitorizare a datelor din Formula 1, dezvoltata ca parte a laboratorului de Servicii Cloud și Containerizare.

## 1. Funcționalitate adaugata
Am implementat o aplicatie web folosind **Flask** care permite vizualizarea datelor despre Formula 1:
- **Podium Actual**: Afiseaza primii trei piloti din clasament.
- **Detalii Circuite**: Ofera informatii specifice despre circuite faimoase (ex: Monaco, Spa).
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
Aplicatia este complet containerizata si poate fi rulata pe orice sistem cu Docker instalat.

### Dovezi execuție:

**A. Imaginea de container creata**
Se observa imaginea `f1-app-stancu-andreea` in lista de imagini locale.
<img width="512" height="73" alt="imagine_docker" src="https://github.com/user-attachments/assets/46de0efd-e699-4144-a337-ff78c887e711" />


**B. Containerul creat pe baza imaginii**
Containerul `container_f1_andreea` in stare **Up**, cu portul 5000 mapat.
<img width="1600" height="183" alt="container_creat_up" src="https://github.com/user-attachments/assets/fc56c09d-93f3-448b-afd1-6412df64984f" />


**C. Browserul care acceseaza aplicatia**
Interfata cu butoane accesata la `http://localhost:5000/formula1`.
<img width="1027" height="334" alt="WhatsApp Image 2026-05-14 at 18 19 09" src="https://github.com/user-attachments/assets/8f929d1c-e453-4f36-89a8-e5a76fb74fbd" />

<img width="736" height="395" alt="WhatsApp Image 2026-05-14 at 18 19 35" src="https://github.com/user-attachments/assets/ad85b632-2524-4131-b402-e010a41e1aeb" />

<img width="994" height="414" alt="WhatsApp Image 2026-05-14 at 18 20 02" src="https://github.com/user-attachments/assets/b223cc3e-2ea5-4e64-b0f1-0d1c0ff7c0f4" />

<img width="1131" height="388" alt="WhatsApp Image 2026-05-14 at 18 20 26" src="https://github.com/user-attachments/assets/def081f4-b37c-47bb-9bfb-a8783aa1ff1c" />


**D. Mesajele afisate in consola**
Log-urile `GET` care atesta comunicarea dintre browser si container.
<img width="1600" height="371" alt="mesaje_consola" src="https://github.com/user-attachments/assets/3c3c0bf0-cc44-46b5-95e2-af3b358c2dd7" />


---
*Proiect realizat de: Stancu Andreea-Beatrice, grupa 442D*
