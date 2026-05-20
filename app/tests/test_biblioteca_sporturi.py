from app.lib import biblioteca_sporturi as bs


def test_functie_1_returneaza_html():
    rezultat = bs.functie_1_padel()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "<p>" in rezultat


def test_functie_1_contine_origine():
    rezultat = bs.functie_1_padel()

    assert "Origine" in rezultat
    assert "Mexic" in rezultat
    assert "Spania" in rezultat


def test_functie_1_contine_informatii_despre_teren():
    rezultat = bs.functie_1_padel()

    assert "Teren" in rezultat
    assert "pereti" in rezultat
    assert "sticla" in rezultat


def test_functie_2_returneaza_html():
    rezultat = bs.functie_2_padel()

    assert len(rezultat) > 0
    assert "<h2>" in rezultat
    assert "<p>" in rezultat


def test_functie_2_contine_racheta():
    rezultat = bs.functie_2_padel()

    assert "Racheta" in rezultat
    assert "padel" in rezultat
    assert "corzi" in rezultat


def test_functie_2_contine_reguli():
    rezultat = bs.functie_2_padel()

    assert "Reguli" in rezultat
    assert "Serviciul" in rezultat
    assert "peretii" in rezultat


def test_functie_2_contine_strategie():
    rezultat = bs.functie_2_padel()

    assert "Strategie" in rezultat
    assert "tehnica" in rezultat
    assert "coordonare" in rezultat
