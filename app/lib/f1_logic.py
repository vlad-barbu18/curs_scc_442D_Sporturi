def primii_trei_piloti():
    """
    Returnează o listă cu numele primilor trei piloți din clasament.
    """
    # Aceasta este lista pe care Flask o va parcurge pentru a crea butoanele/lista
    return ["Max Verstappen", "Lando Norris", "Charles Leclerc"]

def detalii_circuit(nume_circuit):
    """
    Returnează informații specifice despre un circuit dat ca parametru.
    """
    circuite = {
        "Monaco": "Circuit de Monaco este un circuit stradal faimos pentru virajele strânse și eleganță.",
        "Spa": "Circuit de Spa-Francorchamps este cunoscut pentru vremea imprevizibilă și virajul Eau Rouge.",
        "Monza": "Templul Vitezei, gazda Marelui Premiu al Italiei."
    }
    
    # Returnăm descrierea sau un mesaj default dacă numele nu e în listă
    return circuite.get(nume_circuit, "Informațiile despre acest circuit vor fi adăugate în curând.")
