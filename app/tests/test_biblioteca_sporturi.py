"""Testez dupa elemente din functii, daca apare elementul atunci trece testul"""
import logging
from app.lib import biblioteca_sporturi as bs
logger = logging.getLogger(__name__)

def test_competitii_contine_world_cup():
    """Se cauta World Cup"""
    html = bs.competitii_fotbal()
    assert "World Cup" in html

def test_competitii_contine_champions_league():
    """Se cauta Champions League"""
    html = bs.competitii_fotbal()
    assert "Champions League" in html

def test_competitii_contine_premier_league():
    """Se cauta Premier League"""
    html = bs.competitii_fotbal()
    assert "Premier League" in html

def test_competitii_contine_romania():
    """Se cauta Romania"""
    html = bs.competitii_fotbal()
    assert "Romania" in html

def test_echipament_contine_toate_categoriile():
    """Se cauta toate cele 5 categorii de echipament"""
    html = bs.echipament_fotbal()
    for sectiune in ["jucator", "portar", "arbitru", "Mingea", "Terenul"]:
        assert sectiune in html, f"Lipseste sectiunea: {sectiune}"

def test_echipament_contine_dimensiuni_poarta():
    """Se cauta dimensiunile portii"""
    html = bs.echipament_fotbal()
    assert "7.32" in html and "2.44" in html

def test_echipament_contine_manusi_portar():
    """Se cauta manusi sau Manusi"""
    html = bs.echipament_fotbal()
    assert "Manusi" in html or "manusi" in html

def test_echipament_contine_cartonase():
    """se cauta cartonase sau Cartonase"""
    html = bs.echipament_fotbal()
    assert "Cartonase" in html or "cartonase" in html
