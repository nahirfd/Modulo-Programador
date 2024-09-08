class AspiradoraRobot:
    def __init__(self, bateria=100, capacidad_polvo=100):
        self.bateria = bateria
        self.capacidad_polvo = capacidad_polvo
        self.estado = "apagada"
        self.polvo_recogido = 0


    def agotar_bateria(self, porcentaje):
        if self.bateria == 100:
            return "bateria llena"
            
