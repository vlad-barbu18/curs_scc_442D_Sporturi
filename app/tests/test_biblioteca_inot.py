"""
Teste pentru cele 2 functii publice din app.lib.biblioteca_inot.
"""
import logging

from app.lib import biblioteca_inot as bi

logger = logging.getLogger(__name__)


# ----------------------------- Functia 1 -----------------------------


def test_concursuri_returneaza_string():
    """concursuri_inot() trebuie sa returneze un sir non-gol."""
    rezultat = bi.concursuri_inot()
    assert isinstance(rezultat, str)
    assert len(rezultat) > 0


def test_concursuri_contine_html():
    """Rezultatul functiei concursuri trebuie sa contina taguri HTML."""
    rezultat = bi.concursuri_inot()
    assert "<h2>" in rezultat
    assert "<div" in rezultat
    assert "</div>" in rezultat


def test_concursuri_contine_principalele():
    """concursuri_inot() trebuie sa mentioneze cele 3 concursuri majore."""
    rezultat = bi.concursuri_inot()
    assert "Jocurile Olimpice" in rezultat
    assert "Campionatele Mondiale" in rezultat
    assert "Campionatele Europene" in rezultat


def test_concursuri_referinte_imagini():
    """Fiecare concurs trebuie sa aiba o imagine asociata."""
    rezultat = bi.concursuri_inot()
    assert "/static/images/" in rezultat
    assert "olympics.jpg" in rezultat
    assert "mondiale.jpg" in rezultat


def test_concursuri_numar_carduri():
    """Lista interna CONCURSURI trebuie reflectata in numarul de carduri."""
    rezultat = bi.concursuri_inot()
    nr_concursuri = len(bi.CONCURSURI)
    nr_carduri = rezultat.count('class="card"')
    assert nr_carduri == nr_concursuri


# ----------------------------- Functia 2 -----------------------------


def test_inotatori_returneaza_string():
    """inotatori_inot() trebuie sa returneze un sir non-gol."""
    rezultat = bi.inotatori_inot()
    assert isinstance(rezultat, str)
    assert len(rezultat) > 0


def test_inotatori_contine_html():
    """Rezultatul functiei inotatori trebuie sa contina taguri HTML."""
    rezultat = bi.inotatori_inot()
    assert "<h2>" in rezultat
    assert "<div" in rezultat
    assert "<img" in rezultat


def test_inotatori_contine_celebri():
    """inotatori_inot() trebuie sa mentioneze cativa inotatori de top."""
    rezultat = bi.inotatori_inot()
    assert "Michael Phelps" in rezultat
    assert "Katie Ledecky" in rezultat
    assert "David Popovici" in rezultat


def test_inotatori_referinte_imagini():
    """Fiecare inotator trebuie sa aiba o imagine asociata."""
    rezultat = bi.inotatori_inot()
    assert "phelps.jpg" in rezultat
    assert "ledecky.jpg" in rezultat
    assert "popovici.jpg" in rezultat


def test_inotatori_numar_carduri():
    """Lista interna INOTATORI trebuie reflectata in numarul de carduri."""
    rezultat = bi.inotatori_inot()
    nr_inotatori = len(bi.INOTATORI)
    nr_carduri = rezultat.count('class="card"')
    assert nr_carduri == nr_inotatori
