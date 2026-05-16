from app.lib.biblioteca_sporturi import reguli_volei, echipament_volei


def test_reguli_volei():
    assert "6 jucători" in reguli_volei()


def test_echipament_volei():
    assert "minge" in echipament_volei()
