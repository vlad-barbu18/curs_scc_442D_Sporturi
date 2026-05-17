# testez dupa elemente din functii, daca apare elementul atunci trece testul
import logging
logger = logging.getLogger(__name__)

from app.lib import biblioteca_sporturi as bs


def test_competitii_contine_world_cup():
    html = bs.competitii_fotbal()
    assert "World Cup" in html


def test_competitii_contine_champions_league():
    html = bs.competitii_fotbal()
    assert "Champions League" in html


def test_competitii_contine_premier_league():
    html = bs.competitii_fotbal()
    assert "Premier League" in html


def test_competitii_contine_romania():
    html = bs.competitii_fotbal()
    assert "Romania" in html


def test_echipament_contine_toate_categoriile():
    html = bs.echipament_fotbal()
    for sectiune in ["jucator", "portar", "arbitru", "Mingea", "Terenul"]:
        assert sectiune in html, f"Lipseste sectiunea: {sectiune}"


def test_echipament_contine_dimensiuni_poarta():
    html = bs.echipament_fotbal()
    assert "7.32" in html and "2.44" in html


def test_echipament_contine_manusi_portar():
    html = bs.echipament_fotbal()
    assert "Manusi" in html or "manusi" in html


def test_echipament_contine_cartonase():
    html = bs.echipament_fotbal()
    assert "Cartonase" in html or "cartonase" in html
