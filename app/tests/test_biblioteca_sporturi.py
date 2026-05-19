"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""
import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_reguli_returneaza_html():
    """Verifica ca reguli_tir_cu_arcul returneaza HTML non-gol."""
    rezultat = bs.reguli_tir_cu_arcul()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_reguli_contine_distanta():
    """Verifica ca regulile contin informatii despre distanta de tragere."""
    rezultat = bs.reguli_tir_cu_arcul()
    assert "70m" in rezultat


def test_reguli_contine_punctaj():
    """Verifica ca regulile contin informatii despre punctaj."""
    rezultat = bs.reguli_tir_cu_arcul()
    assert "10" in rezultat


def test_reguli_contine_toate_elementele():
    """Verifica ca toate regulile sunt prezente in HTML."""
    rezultat = bs.reguli_tir_cu_arcul()
    assert "Distanta" in rezultat
    assert "Tinta" in rezultat
    assert "Sageti" in rezultat


def test_campioni_returneaza_html():
    """Verifica ca campioni_tir_cu_arcul returneaza HTML non-gol."""
    rezultat = bs.campioni_tir_cu_arcul()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_campioni_contine_ellison():
    """Verifica prezenta lui Brady Ellison in lista campionilor."""
    rezultat = bs.campioni_tir_cu_arcul()
    assert "Ellison" in rezultat


def test_campioni_contine_deepika():
    """Verifica prezenta lui Deepika Kumari in lista campionilor."""
    rezultat = bs.campioni_tir_cu_arcul()
    assert "Deepika" in rezultat


def test_campioni_contine_tari():
    """Verifica ca lista campionilor include tarile de origine."""
    rezultat = bs.campioni_tir_cu_arcul()
    assert "SUA" in rezultat
    assert "India" in rezultat
    assert "Coreea de Sud" in rezultat
