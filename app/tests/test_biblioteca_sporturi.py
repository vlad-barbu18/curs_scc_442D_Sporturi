"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    """Verifica ca functia 1 returneaza HTML non-gol."""
    rezultat = bs.functie_1_sport()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_functie_1_contine_marker():
    """Verifica prezenta unui marker specific in HTML."""
    rezultat = bs.functie_1_sport()
    assert "valoare1" in rezultat


def test_functie_2_returneaza_html():
    """Verifica ca functia 2 returneaza HTML non-gol."""
    rezultat = bs.functie_2_sport()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_marker():
    """Verifica prezenta unui marker specific."""
    rezultat = bs.functie_2_sport()
    assert "titlu1" in rezultat
