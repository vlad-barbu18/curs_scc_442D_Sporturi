# 1. Plecăm de la o imagine oficială de Python (varianta slim e mai mică și rapidă)
FROM python:3.12-slim

# 2. Stabilim folderul din interiorul containerului unde va sta codul nostru
WORKDIR /app

# 3. Copiem fișierul de dependențe în container
COPY requirements.txt .

# 4. Instalăm bibliotecile necesare (pytest, flask etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiem tot restul fișierelor din folderul curent (app, test_f1.py etc.) în container
COPY . .

# 6. Setăm variabila de mediu pentru ca Python să găsească folderul 'app' (fix-ul pentru erorile de import)
ENV PYTHONPATH=/app

# 7. Comanda care se execută când pornește containerul. 
# Aici rulăm scriptul tău principal.
CMD ["python3", "sporturi.py"]
