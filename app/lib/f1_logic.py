def primii_trei_piloti():
    podium = {
        1: "Max Verstappen",
        2: "Lando Norris",
        3: "Lewis Hamilton"
    }
    return podium

def detalii_circuit(nume):
    circuite = {
        "Monaco": "Circuit stradal, foarte îngust.",
        "Spa": "Cel mai lung circuit din calendar."
    }
    return circuite.get(nume, "Circuit necunoscut")
