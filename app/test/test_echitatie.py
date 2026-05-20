"""
Teste pentru functionalitatea Echitatie.
"""

import logging

from app.lib.biblioteca_sporturi import (
    discipline_echitatie,
    echipamente_echitatie,
)

logger = logging.getLogger(__name__)


def test_discipline_returneaza_html():
    """
    Verifica daca functia returneaza HTML.
    """

    rezultat = discipline_echitatie()

    assert len(rezultat) > 0
    assert "<html>" in rezultat


def test_discipline_contine_dresaj():
    """
    Verifica daca informatiile despre discipline contin Dresaj.
    """

    rezultat = discipline_echitatie()

    if "Dresaj" in rezultat:
        logger.info("Informatiile despre Dresaj au fost gasite.")
        assert True
    else:
        logger.error("Nu am gasit informatii despre Dresaj.")
        assert False


def test_discipline_contine_polo():
    """
    Verifica daca informatiile despre discipline contin Polo.
    """

    rezultat = discipline_echitatie()

    if "Polo" in rezultat:
        logger.info("Informatiile despre Polo au fost gasite.")
        assert True
    else:
        logger.error("Nu am gasit informatii despre Polo.")
        assert False


def test_discipline_contine_obstacole():
    """
    Verifica daca informatiile contin obstacole.
    """

    rezultat = discipline_echitatie()

    if "obstacole" in rezultat:
        logger.info("Informatiile despre obstacole au fost gasite.")
        assert True
    else:
        logger.error("Nu am gasit informatii despre obstacole.")
        assert False


def test_echipamente_returneaza_lista():
    """
    Verifica daca functia returneaza lista HTML.
    """

    rezultat = echipamente_echitatie()

    assert "<ul>" in rezultat


def test_echipamente_contine_casca():
    """
    Verifica daca informatiile despre echipamente contin Casca.
    """

    rezultat = echipamente_echitatie()

    if "Casca" in rezultat:
        logger.info("Informatiile despre Casca au fost gasite.")
        assert True
    else:
        logger.error("Nu am gasit informatii despre Casca.")
        assert False
