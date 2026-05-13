from app.lib.f1_logic import primii_trei_piloti, detalii_circuit

def test_podium_nu_este_gol():
    rezultat = primii_trei_piloti()
    assert len(rezultat) == 3
    assert rezultat[1] == "Max Verstappen"

def test_circuit_monaco():
    descriere = detalii_circuit("Monaco")
    assert "stradal" in descriere
