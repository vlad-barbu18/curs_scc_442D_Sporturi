"""Teste pentru cele 2 functii din app.lib.biblioteca_sporturi."""
import logging
from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)

def test_reguli_returneaza_html():
    """Verifica ca functia 1 returneaza HTML non-gol."""
    rezultat = bs.reguli_polo()
    assert len(rezultat) > 0
    assert "<" in rezultat

def test_reguli_contine_marker():
    """Verifica prezenta unui marker specific in HTML."""
    rezultat = bs.reguli_polo()
    assert "Jucatori" in rezultat

def test_echipament_returneaza_html():
    """Verifica ca functia 2 returneaza HTML non-gol."""
    rezultat = bs.echipament_polo()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat

def test_echipament_contine_marker():
    """Verifica prezenta unui marker specific."""
    rezultat = bs.echipament_polo()
    assert "Casca" in rezultat
