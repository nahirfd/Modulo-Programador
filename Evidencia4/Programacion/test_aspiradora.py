from aspiradora_inalambrica import AspiradoraRobot;

def test_bateria():
    aspiradora = AspiradoraRobot()
    assert aspiradora.agotar_bateria(100) == "bateria llena"