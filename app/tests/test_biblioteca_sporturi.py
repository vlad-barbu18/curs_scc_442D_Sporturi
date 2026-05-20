"""
Teste pentru cele 2 functii din app.lib.biblioteca_sporturi.
"""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    """Verifica daca functia 1 returneaza HTML non-gol."""

    rezultat = bs.functie_1_tenis()

    assert len(rezultat) > 0
    assert "<p>" in rezultat


def test_functie_1_contine_marker():
    """Verifica prezenta unui marker specific in HTML."""

    rezultat = bs.functie_1_tenis()

    assert "Tenis" in rezultat or "tenis" in rezultat


def test_functie_1_contine_html():
    """Verifica daca exista tag HTML h2."""

    rezultat = bs.functie_1_tenis()

    assert "<h2>" in rezultat


def test_functie_2_returneaza_html():
    """Verifica daca functia 2 returneaza HTML non-gol."""

    rezultat = bs.functie_2_tenis()

    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_marker():
    """Verifica prezenta unui marker specific."""

    rezultat = bs.functie_2_tenis()

    assert "Serviciul" in rezultat


def test_functie_2_contine_lista():
    """Verifica existenta elementelor de lista."""

    rezultat = bs.functie_2_tenis()

    assert "<li>" in rezultat
