import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_functie_1_returneaza_html():
    rezultat = bs.functie_1_box()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_functie_1_contine_marker():
    rezultat = bs.functie_1_box()
    assert "valoare1" in rezultat


def test_functie_2_returneaza_html():
    rezultat = bs.functie_2_box()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_marker():
    rezultat = bs.functie_2_box()
    assert "titlu1" in rezultat
