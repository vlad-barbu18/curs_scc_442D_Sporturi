"""
Teste pentru cele doua functii din app.lib.biblioteca_sporturi.
"""

import logging

from app.lib import biblioteca_sporturi as bs

logger = logging.getLogger(__name__)


def test_afiseaza_luptatori_mma_returneaza_html():
    """Verifica daca functia pentru luptatori returneaza HTML."""
    rezultat = bs.afiseaza_luptatori_mma()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert 'class="grid"' in rezultat
    assert 'class="stat-card"' in rezultat


def test_afiseaza_luptatori_mma_contine_conor():
    """Verifica daca in rezultat apare Conor McGregor."""
    rezultat = bs.afiseaza_luptatori_mma()

    assert "Conor McGregor" in rezultat


def test_afiseaza_luptatori_mma_contine_khabib():
    """Verifica daca in rezultat apare Khabib Nurmagomedov."""
    rezultat = bs.afiseaza_luptatori_mma()

    assert "Khabib Nurmagomedov" in rezultat


def test_afiseaza_tehnici_mma_returneaza_html():
    """Verifica daca functia pentru tehnici returneaza HTML cu carduri."""
    rezultat = bs.afiseaza_tehnici_mma()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert 'class="grid"' in rezultat
    assert 'class="stat-card"' in rezultat


def test_afiseaza_tehnici_mma_contine_striking():
    """Verifica daca in rezultat apare tehnica Striking."""
    rezultat = bs.afiseaza_tehnici_mma()

    assert "Striking" in rezultat


def test_afiseaza_tehnici_mma_contine_grappling():
    """Verifica daca in rezultat apare tehnica Grappling."""
    rezultat = bs.afiseaza_tehnici_mma()

    assert "Grappling" in rezultat