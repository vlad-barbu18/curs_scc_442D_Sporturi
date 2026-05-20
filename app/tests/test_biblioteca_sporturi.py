"""Teste pentru functiile din app.lib.biblioteca_sporturi."""

from app.lib import biblioteca_sporturi as bs


def test_functie_1_returneaza_html():
    rezultat = bs.functie_1_biatlon()
    assert len(rezultat) > 0
    assert "<" in rezultat


def test_functie_1_contine_biatlon():
    rezultat = bs.functie_1_biatlon()
    assert "Biatlon" in rezultat or "biatlon" in rezultat


def test_functie_1_contine_sport_de_iarna():
    rezultat = bs.functie_1_biatlon()
    assert "sport de iarna" in rezultat


def test_functie_2_returneaza_html():
    rezultat = bs.functie_2_biatlon()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_tir():
    rezultat = bs.functie_2_biatlon()
    assert "Tir sportiv" in rezultat


def test_functie_2_contine_penalizari():
    rezultat = bs.functie_2_biatlon()
    assert "Penalizari" in rezultat
