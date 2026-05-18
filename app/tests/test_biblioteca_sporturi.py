"""
Teste unitare pentru biblioteca_sporturi.py.
"""

from app.lib.biblioteca_sporturi import competitii_ciclism, echipament_ciclism


def test_competitii_ciclism_contine_tour_de_france():
    """
    Verifica daca informatiile despre competitii contin Tour de France.
    """
    rezultat = competitii_ciclism()
    assert "Tour de France" in rezultat


def test_competitii_ciclism_contine_giro():
    """
    Verifica daca informatiile despre competitii contin Giro d'Italia.
    """
    rezultat = competitii_ciclism()
    assert "Giro d'Italia" in rezultat


def test_echipament_ciclism_contine_casca():
    """
    Verifica daca informatiile despre echipament contin casca.
    """
    rezultat = echipament_ciclism()
    assert "Casca" in rezultat


def test_echipament_ciclism_contine_bicicleta():
    """
    Verifica daca informatiile despre echipament contin bicicleta.
    """
    rezultat = echipament_ciclism()
    assert "Bicicleta" in rezultat