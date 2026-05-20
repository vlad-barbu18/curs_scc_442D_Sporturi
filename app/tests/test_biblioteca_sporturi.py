"""Teste pentru continutul HTML din app.lib.biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_genereaza_regulament_sah_returneaza_html():
    """Verifica sectiunea de regulament."""
    rezultat = bs.genereaza_regulament_sah()

    assert '<section class="content-grid">' in rezultat
    assert "Obiectiv" in rezultat
    assert "Rocada" in rezultat


def test_genereaza_competitii_sah_returneaza_html():
    """Verifica sectiunea de competitii."""
    rezultat = bs.genereaza_competitii_sah()

    assert '<section class="competition-list">' in rezultat
    assert "Campionatul Mondial" in rezultat
    assert "Olimpiada de Sah" in rezultat
