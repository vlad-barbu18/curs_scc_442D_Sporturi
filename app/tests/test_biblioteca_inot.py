"""
Teste unitare pentru functiile din app/lib/inot.py.
"""

from app.lib.inot import get_concursuri_inot, get_inotatori_profesionisti


def test_concursuri_returneaza_lista():
    rezultat = get_concursuri_inot()
    assert isinstance(rezultat, list)


def test_concursuri_are_5_elemente():
    rezultat = get_concursuri_inot()
    assert len(rezultat) == 5


def test_concursuri_au_chei_corecte():
    rezultat = get_concursuri_inot()
    chei_asteptate = {"nume", "organizator", "frecventa", "descriere"}
    for concurs in rezultat:
        assert set(concurs.keys()) == chei_asteptate


def test_concursuri_contine_jocuri_olimpice():
    rezultat = get_concursuri_inot()
    nume = [c["nume"] for c in rezultat]
    assert "Jocurile Olimpice" in nume


def test_concursuri_contine_world_aquatics():
    rezultat = get_concursuri_inot()
    organizatori = " ".join(c["organizator"] for c in rezultat)
    assert "World Aquatics" in organizatori


def test_inotatori_returneaza_lista():
    rezultat = get_inotatori_profesionisti()
    assert isinstance(rezultat, list)


def test_inotatori_are_6_elemente():
    rezultat = get_inotatori_profesionisti()
    assert len(rezultat) == 6


def test_inotatori_au_chei_corecte():
    rezultat = get_inotatori_profesionisti()
    chei_asteptate = {"nume", "tara", "specialitate", "realizare"}
    for sportiv in rezultat:
        assert set(sportiv.keys()) == chei_asteptate


def test_inotatori_contine_phelps():
    rezultat = get_inotatori_profesionisti()
    nume = [i["nume"] for i in rezultat]
    assert "Michael Phelps" in nume


def test_inotatori_contine_popovici():
    rezultat = get_inotatori_profesionisti()
    nume = [i["nume"] for i in rezultat]
    assert "David Popovici" in nume


def test_inotatori_are_cel_putin_un_roman():
    rezultat = get_inotatori_profesionisti()
    tari = [i["tara"] for i in rezultat]
    assert "Romania" in tari
