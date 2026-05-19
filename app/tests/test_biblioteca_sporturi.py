"""Teste pentru continutul generat despre box."""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_echipament_box_returneaza_html():
    """Verifica faptul ca pagina de echipament produce HTML."""
    rezultat = bs.echipament_box()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_echipament_box_contine_manusi():
    """Verifica includerea manusilor de box."""
    rezultat = bs.echipament_box()
    assert "Manusi de box" in rezultat


def test_competitii_box_returneaza_html():
    """Verifica faptul ca pagina de competitii produce HTML."""
    rezultat = bs.competitii_box()
    assert len(rezultat) > 0
    assert "timeline-list" in rezultat


def test_competitii_box_contine_olimpiada():
    """Verifica includerea Jocurilor Olimpice."""
    rezultat = bs.competitii_box()
    assert "Jocurile Olimpice" in rezultat
