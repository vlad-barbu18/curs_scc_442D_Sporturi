import logging

logger = logging.getLogger(__name__)

from app.lib.biblioteca_sporturi import (
    discipline_echitatie,
    echipamente_echitatie,
)


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


def test_discipline_contine_sarituri():
    """
    Verifica daca informatiile despre discipline contin sarituri.
    """

    rezultat = discipline_echitatie()

    if "obstacole" in rezultat:
        logger.info("Informatiile despre sarituri au fost gasite.")
        assert True
    else:
        logger.error("Nu am gasit informatii despre sarituri.")
        assert False


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
