from app.lib import biblioteca_sporturi as bs


def test_functie_1_returneaza_html():
    rezultat = bs.functie_1_padel()
    assert len(rezultat) > 0
    assert "<h2>" in rezultat


def test_functie_1_contine_origine():
    rezultat = bs.functie_1_padel()
    assert "Origine" in rezultat
    assert "Mexic" in rezultat


def test_functie_2_returneaza_html():
    rezultat = bs.functie_2_padel()
    assert len(rezultat) > 0
    assert "<ul>" in rezultat


def test_functie_2_contine_racheta():
    rezultat = bs.functie_2_padel()
    assert "Racheta" in rezultat
    assert "padel" in rezultat
