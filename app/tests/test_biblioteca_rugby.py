"""Teste pentru cele 2 functii din app.lib.biblioteca_rugby."""

import logging

from app.lib import biblioteca_rugby as bs

logger = logging.getLogger(__name__)


def test_reguli_rugby_returneaza_html():
    """Verifica faptul ca functia reguli_rugby returneaza HTML non-gol."""
    rezultat = bs.reguli_rugby()
    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "</p>" in rezultat


def test_reguli_rugby_contine_pasele():
    """Verifica daca regulile contin sectiunea Pasele."""
    rezultat = bs.reguli_rugby()
    assert "Pasele" in rezultat


def test_reguli_rugby_contine_eseul():
    """Verifica daca regulile contin sectiunea Eseul."""
    rezultat = bs.reguli_rugby()
    assert "Eseul" in rezultat


def test_reguli_rugby_contine_placajul():
    """Verifica daca regulile contin sectiunea Placajul."""
    rezultat = bs.reguli_rugby()
    assert "Placajul" in rezultat


def test_reguli_rugby_contine_lovitura_de_pedeapsa():
    """Verifica daca regulile contin sectiunea Lovitura de pedeapsa."""
    rezultat = bs.reguli_rugby()
    assert "Lovitura de pedeapsa" in rezultat


def test_echipament_rugby_returneaza_html():
    """Verifica faptul ca functia echipament_rugby returneaza HTML non-gol."""
    rezultat = bs.echipament_rugby()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_echipament_rugby_contine_toate_categoriile():
    """Verifica daca echipamentul contine toate categoriile definite."""
    rezultat = bs.echipament_rugby()

    for sectiune in ["Mingea", "Tricou", "Ghete", "Protectie dentara", "Terenul"]:
        assert sectiune in rezultat, f"Lipseste sectiunea: {sectiune}"


def test_echipament_rugby_contine_minge_ovala():
    """Verifica daca apare informatia despre mingea ovala."""
    rezultat = bs.echipament_rugby()
    assert "ovala" in rezultat


def test_echipament_rugby_contine_crampoane():
    """Verifica daca apare informatia despre crampoane."""
    rezultat = bs.echipament_rugby()
    assert "crampoane" in rezultat
