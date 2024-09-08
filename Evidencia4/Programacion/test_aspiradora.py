from aspiradora_inalambrica import AspiradoraRobot;

def test_bateria():
    aspiradora = AspiradoraRobot()
    assert aspiradora.agotar_bateria(100) == "bateria llena"
    

def test_capacidad():
    aspiradora = AspiradoraRobot()
    assert aspiradora.recoger_polvo(0) == "El contenedor de polvo está lleno. Vacíalo antes de continuar."
    
    
    
    