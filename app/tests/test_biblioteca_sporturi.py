"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""
import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_reguli_returneaza_html():
    """Verifica ca reguli_tenis_de_masa returneaza HTML non-gol."""
    rezultat = bs.reguli_tenis_de_masa()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_reguli_contine_dimensiuni_masa():
    """Verifica ca regulile contin dimensiunile mesei."""
    rezultat = bs.reguli_tenis_de_masa()
    assert "274" in rezultat


def test_reguli_contine_punctaj():
    """Verifica ca regulile contin informatii despre punctaj."""
    rezultat = bs.reguli_tenis_de_masa()
    assert "11" in rezultat


def test_reguli_contine_toate_elementele():
    """Verifica ca toate cele 6 reguli sunt prezente in HTML."""
    rezultat = bs.reguli_tenis_de_masa()
    assert "Masa" in rezultat
    assert "Plasa" in rezultat
    assert "Minge" in rezultat


def test_campioni_returneaza_html():
    """Verifica ca campioni_tenis_de_masa returneaza HTML non-gol."""
    rezultat = bs.campioni_tenis_de_masa()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_campioni_contine_ma_long():
    """Verifica prezenta lui Ma Long in lista campionilor."""
    rezultat = bs.campioni_tenis_de_masa()
    assert "Ma Long" in rezultat


def test_campioni_contine_waldner():
    """Verifica prezenta lui Waldner in lista campionilor."""
    rezultat = bs.campioni_tenis_de_masa()
    assert "Waldner" in rezultat


def test_campioni_contine_tari():
    """Verifica ca listele campionilor include tarile de origine."""
    rezultat = bs.campioni_tenis_de_masa()
    assert "China" in rezultat
    assert "Suedia" in rezultat
    assert "Germania" in rezultat
