"""Teste pentru cele doua functii din biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_functie_1_biliard_returneaza_html():
    """Verifica daca functia 1 returneaza continut HTML."""
    rezultat = bs.functie_1_biliard()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "Informatii generale despre biliard" in rezultat


def test_functie_1_biliard_contine_definitie():
    """Verifica daca functia 1 contine informatii despre definitia biliardului."""
    rezultat = bs.functie_1_biliard()

    assert "Definitie" in rezultat
    assert "sport de precizie" in rezultat


def test_functie_2_biliard_returneaza_lista_html():
    """Verifica daca functia 2 returneaza o lista HTML."""
    rezultat = bs.functie_2_biliard()

    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_functie_2_biliard_contine_reguli():
    """Verifica daca functia 2 contine reguli de baza despre biliard."""
    rezultat = bs.functie_2_biliard()

    assert "Lovirea bilei albe" in rezultat
    assert "Fault" in rezultat
