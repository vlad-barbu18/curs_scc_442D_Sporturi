"""Teste pentru rutele aplicatiei Flask."""

from sporturi import app


def test_rutele_principale_functioneaza():
    """Verifica rutele cerute pentru aplicatia despre sah."""
    client = app.test_client()
    rute = [
        "/sporturi",
        "/sporturi/sah",
        "/sporturi/sah/regulament",
        "/sporturi/sah/competitii",
    ]

    for ruta in rute:
        raspuns = client.get(ruta)
        assert raspuns.status_code == 200


def test_paginile_contin_continut_despre_sah():
    """Verifica markerii principali din pagini."""
    client = app.test_client()

    assert b"Sahul, sportul mintii" in client.get("/sporturi").data
    assert b"Reguli de baza" in client.get("/sporturi/sah/regulament").data
    assert b"Campionatul Mondial" in client.get("/sporturi/sah/competitii").data
