"""Teste pentru cele 2 functii din app.lib.biblioteca_badminton."""

import logging

from app.lib import biblioteca_badminton as bs

logger = logging.getLogger(__name__)


def test_reguli_badminton_returneaza_html():
    """Verifica daca functia reguli_badminton returneaza HTML non-gol."""
    rezultat = bs.reguli_badminton()
    assert len(rezultat) > 0
    assert "<" in rezultat
    assert "<h2>" in rezultat


def test_reguli_badminton_contine_serviciul():
    """Verifica prezenta unui marker specific in HTML."""
    rezultat = bs.reguli_badminton()
    assert "Serviciul" in rezultat


def test_reguli_badminton_contine_fluturasul():
    """Verifica daca apare informatia despre fluturas."""
    rezultat = bs.reguli_badminton()
    assert "Fluturasul" in rezultat


def test_reguli_badminton_contine_punctajul():
    """Verifica daca apare informatia despre punctaj."""
    rezultat = bs.reguli_badminton()
    assert "Punctajul" in rezultat


def test_echipament_badminton_returneaza_html():
    """Verifica daca functia echipament_badminton returneaza HTML non-gol."""
    rezultat = bs.echipament_badminton()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_echipament_badminton_contine_racheta():
    """Verifica prezenta unui marker specific."""
    rezultat = bs.echipament_badminton()
    assert "Racheta" in rezultat


def test_echipament_badminton_contine_fileul():
    """Verifica daca apare informatia despre fileu."""
    rezultat = bs.echipament_badminton()
    assert "Fileul" in rezultat


def test_echipament_badminton_contine_terenul():
    """Verifica daca apare informatia despre teren."""
    rezultat = bs.echipament_badminton()
    assert "Terenul" in rezultat
