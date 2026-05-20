"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""
import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    """Verifica daca functia 1 returneaza HTML non-gol."""
    rezultat = bs.functie_1_ski()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "<p>" in rezultat


def test_functie_1_contine_marker():
    """Verifica prezenta unui marker specific despre ski."""
    rezultat = bs.functie_1_ski()

    assert "Sport de iarna" in rezultat
    assert "Echipament" in rezultat
    assert "Abilitati importante" in rezultat


def test_functie_2_returneaza_html():
    """Verifica daca functia 2 returneaza HTML non-gol."""
    rezultat = bs.functie_2_ski()

    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "<li>" in rezultat


def test_functie_2_contine_marker():
    """Verifica prezenta unui marker specific despre tipurile de ski."""
    rezultat = bs.functie_2_ski()

    assert "Ski alpin" in rezultat
    assert "Ski fond" in rezultat
    assert "Ski freestyle" in rezultat