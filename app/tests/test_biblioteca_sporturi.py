"""Teste pentru biblioteca proiectului Sporturi - Balet."""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_stiluri_balet_returneaza_html():
    """Verifica daca functia stiluri_balet returneaza continut HTML."""
    rezultat = bs.stiluri_balet()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "Stiluri de balet" in rezultat


def test_stiluri_balet_contine_balet_clasic():
    """Verifica prezenta stilului Balet clasic."""
    rezultat = bs.stiluri_balet()

    assert "Balet clasic" in rezultat
    assert "postura corecta" in rezultat


def test_stiluri_balet_contine_balet_contemporan():
    """Verifica prezenta stilului Balet contemporan."""
    rezultat = bs.stiluri_balet()

    assert "Balet contemporan" in rezultat
    assert "coregrafii variate" in rezultat


def test_stiluri_balet_are_mai_multe_paragrafe():
    """Verifica daca HTML-ul contine mai multe paragrafe."""
    rezultat = bs.stiluri_balet()

    assert rezultat.count("<p>") >= 4


def test_echipament_balet_returneaza_html():
    """Verifica daca functia echipament_balet returneaza continut HTML."""
    rezultat = bs.echipament_balet()

    assert len(rezultat) > 0
    assert "<ul>" in rezultat
    assert "</ul>" in rezultat


def test_echipament_balet_contine_poante():
    """Verifica prezenta poantelor in echipamentul de balet."""
    rezultat = bs.echipament_balet()

    assert "Poante" in rezultat
    assert "varful degetelor" in rezultat


def test_echipament_balet_contine_tutu():
    """Verifica prezenta fustei tutu."""
    rezultat = bs.echipament_balet()

    assert "Fusta tutu" in rezultat
    assert "rol scenic" in rezultat


def test_echipament_balet_are_lista():
    """Verifica daca echipamentul este afisat sub forma de lista."""
    rezultat = bs.echipament_balet()

    assert rezultat.count("<li>") >= 4
