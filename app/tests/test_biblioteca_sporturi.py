"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    """Verifica daca functia 1 returneaza un string HTML."""
    rezultat = bs.functie_1_sport()

    logger.info("Rezultat functie_1_sport: %s", rezultat)

    assert isinstance(rezultat, str)
    assert len(rezultat) > 0
    assert "<" in rezultat
    assert ">" in rezultat


def test_functie_1_contine_competitii_baschet():
    """Verifica daca functia 1 contine competitii de baschet."""
    rezultat = bs.functie_1_sport()

    assert "NBA" in rezultat
    assert "EuroLeague" in rezultat
    assert "Campionatul Mondial FIBA" in rezultat


def test_functie_2_returneaza_html():
    """Verifica daca functia 2 returneaza un string HTML."""
    rezultat = bs.functie_2_sport()

    logger.info("Rezultat functie_2_sport: %s", rezultat)

    assert isinstance(rezultat, str)
    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_functie_2_contine_echipamente_baschet():
    """Verifica daca functia 2 contine echipamente de baschet."""
    rezultat = bs.functie_2_sport()

    assert "Minge de baschet" in rezultat
    assert "Cos de baschet" in rezultat
    assert "Pantofi de baschet" in rezultat
