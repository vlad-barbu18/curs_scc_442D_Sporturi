"""
Teste unitare pentru biblioteca_sporturi.py.
"""

from app.lib.biblioteca_sporturi import (
    sarituri_patinaj_artistic,
    echipamente_patinaj_artistic,
)


def test_sarituri_contine_axel():
    """
    Verifica daca informatiile despre sarituri contin Axelul.
    """
    rezultat = sarituri_patinaj_artistic()
    assert "Axelul" in rezultat


def test_sarituri_contine_rotatii():
    """
    Verifica daca informatiile despre sarituri contin ROTATII.
    """
    rezultat = sarituri_patinaj_artistic()
    assert "rotatii in aer" in rezultat


def test_echipamente_contine_patine():
    """
    Verifica daca informatiile despre sarituri contin PATINE.
    """
    rezultat = echipamente_patinaj_artistic()
    assert "Patine" in rezultat


def test_echipamente_contine_costum():
    """
    Verifica daca informatiile despre sarituri contin COSTUM.
    """
    rezultat = echipamente_patinaj_artistic()
    assert "Costum de concurs" in rezultat
