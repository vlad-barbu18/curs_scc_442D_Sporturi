"""Teste pentru functiile din app.lib.biblioteca_sporturi."""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    """Verifica daca functia 1 returneaza HTML non-gol."""

    rezultat = bs.functie_1_biatlon()

    assert len(rezultat) > 0
    assert "<" in rezultat


def test_functie_1_contine_marker():
    """Verifica prezenta unui marker specific in HTML."""

    rezultat = bs.functie_1_biatlon()

    assert "Biatlon" in rezultat


def test_functie_1_contine_descriere():
    """Verifica daca exista descriere despre sport."""

    rezultat = bs.functie_1_biatlon()

    assert "sport de iarna" in rezultat


def test_functie_1_contine_introducere():
    """Verifica prezenta introducerii despre sporturi."""

    rezultat = bs.functie_1_biatlon()

    assert "Sporturile reprezinta activitati fizice" in rezultat


def test_functie_2_returneaza_html():
    """Verifica daca functia 2 returneaza HTML non-gol."""

    rezultat = bs.functie_2_biatlon()

    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_marker():
    """Verifica prezenta unui marker specific."""

    rezultat = bs.functie_2_biatlon()

    assert "Competitii" in rezultat


def test_functie_2_contine_reguli():
    """Verifica daca functia 2 contine reguli despre biatlon."""

    rezultat = bs.functie_2_biatlon()

    assert "Penalizari" in rezultat


def test_functie_2_contine_tir():
    """Verifica daca functia 2 contine informatii despre tir."""

    rezultat = bs.functie_2_biatlon()

    assert "Tir sportiv" in rezultat
