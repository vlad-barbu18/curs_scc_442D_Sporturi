from app.lib.biblioteca_sporturi import reguli_golf, echipament_golf, teren_golf


def test_reguli_golf():
    assert "golf" in reguli_golf()


def test_echipament_golf():
    assert "Crose" in echipament_golf()


def test_teren_golf():
    assert "9 sau 18" in teren_golf()
