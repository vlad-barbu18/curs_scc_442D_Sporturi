"""Teste pentru functiile despre sailing din biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_competitii_sailing_returneaza_html():
    """Verifica daca functia competitii_sailing returneaza HTML."""
    rezultat = bs.competitii_sailing()
    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "</p>" in rezultat


def test_competitii_sailing_contine_america_cup():
    """Verifica prezenta competitiei America's Cup."""
    rezultat = bs.competitii_sailing()
    assert "America" in rezultat
    assert "Cup" in rezultat


def test_competitii_sailing_contine_jocuri_olimpice():
    """Verifica prezenta competitiei olimpice."""
    rezultat = bs.competitii_sailing()
    assert "Olympic" in rezultat
    assert "Sailing" in rezultat


def test_echipament_sailing_returneaza_lista_html():
    """Verifica daca functia echipament_sailing returneaza o lista HTML."""
    rezultat = bs.echipament_sailing()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_echipament_sailing_contine_barca():
    """Verifica prezenta barcii cu vele."""
    rezultat = bs.echipament_sailing()
    assert "Barca cu vele" in rezultat


def test_echipament_sailing_contine_vesta():
    """Verifica prezenta vestei de salvare."""
    rezultat = bs.echipament_sailing()
    assert "Vesta de salvare" in rezultat

