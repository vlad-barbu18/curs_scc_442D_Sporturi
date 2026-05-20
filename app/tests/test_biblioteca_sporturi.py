"""Teste pentru functiile din app.lib.biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_program_partie_returneaza_html():
    """Verifica daca functia de program returneaza HTML non-gol."""
    rezultat = bs.program_partie_ski()

    assert len(rezultat) > 0
    assert "<table>" in rezultat
    assert "Program de functionare" in rezultat


def test_program_partie_contine_marker():
    """Verifica prezenta unor informatii despre program."""
    rezultat = bs.program_partie_ski()

    assert "Luni - Joi" in rezultat
    assert "Nocturna" in rezultat
    assert "Stare partie" in rezultat


def test_tarife_skipass_returneaza_html():
    """Verifica daca functia de skipass returneaza HTML non-gol."""
    rezultat = bs.tarife_skipass_ski()

    assert len(rezultat) > 0
    assert "<table>" in rezultat
    assert "Tarife skipass" in rezultat


def test_tarife_skipass_contine_marker():
    """Verifica prezenta unor tarife de skipass."""
    rezultat = bs.tarife_skipass_ski()

    assert "Urcare individuala adult" in rezultat
    assert "Skipass 4 ore adult" in rezultat
    assert "Skipass zi completa copil" in rezultat


def test_tabel_inchirieri_contine_echipamente():
    """Verifica tabelul de inchirieri."""
    rezultat = bs.tabel_inchirieri_ski()

    assert "Set complet adult" in rezultat
    assert "Clapari" in rezultat
    assert "Casca" in rezultat


def test_reguli_partie_contine_lista():
    """Verifica lista de reguli."""
    rezultat = bs.reguli_partie_ski()

    assert "<ul>" in rezultat
    assert "echipament adecvat" in rezultat