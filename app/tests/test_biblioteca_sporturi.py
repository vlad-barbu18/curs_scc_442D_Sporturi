"""Teste pentru cele doua functii din app.lib.biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_reguli_volei_returneaza_html():
    """Verifica faptul ca functia pentru reguli returneaza HTML non-gol."""
    rezultat = bs.reguli_volei()

    assert len(rezultat) > 0
    assert "<ul" in rezultat
    assert "</ul>" in rezultat


def test_reguli_volei_contine_marker_specific():
    """Verifica prezenta unui marker specific pentru regulile jocului."""
    rezultat = bs.reguli_volei()

    assert "6 jucatori" in rezultat
    assert "25 de puncte" in rezultat


def test_echipament_volei_returneaza_html():
    """Verifica faptul ca functia pentru echipament returneaza HTML non-gol."""
    rezultat = bs.echipament_volei()

    assert len(rezultat) > 0
    assert "<ul" in rezultat
    assert "</ul>" in rezultat


def test_echipament_volei_contine_marker_specific():
    """Verifica prezenta unui marker specific pentru echipamentul de volei."""
    rezultat = bs.echipament_volei()

    assert "Mingea de volei" in rezultat
    assert "Genunchierele" in rezultat
