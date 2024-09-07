class AspiradoraRobot:
    def __init__(self, bateria=100, capacidad_polvo=100):
        self.bateria = bateria
        self.capacidad_polvo = capacidad_polvo
        self.estado = "apagada"
        self.polvo_recogido = 0

    def iniciar(self):
        if self.bateria >= 10:
            self.estado = "limpiando"
            print("La aspiradora ha comenzado a limpiar.")
        else:
            print("Batería insuficiente para iniciar la limpieza.")

    def recoger_polvo(self, cantidad=10):
        if self.estado == "limpiando":
            if self.polvo_recogido + cantidad <= self.capacidad_polvo:
                self.polvo_recogido += cantidad
                self.agotar_bateria(10)
                print(f"Recogidos {cantidad} gramos de polvo. Batería restante: {self.bateria}%")
            else:
                print("El contenedor de polvo está lleno. Vacíalo antes de continuar.")
        else:
            print("La aspiradora no está encendida, por favor inicie la limpieza.")

    def agotar_bateria(self, porcentaje):
        self.bateria -= porcentaje
        if self.bateria <= 0:
            self.bateria = 0
            self.apagar()

    def apagar(self):
        self.estado = "apagada"
        print("La aspiradora se ha apagado debido a batería baja.")

    def __str__(self):
        return (f"AspiradoraRobot(estado={self.estado}, bateria={self.bateria}%, "
                f"polvo_recogido={self.polvo_recogido}g)")

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Iniciar limpieza")
    print("2. Recoger polvo")
    print("3. Mostrar estado de la aspiradora")
    print("4. Salir")

def main():
    aspiradora = AspiradoraRobot()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            aspiradora.iniciar()
        elif opcion == "2":
            if aspiradora.estado == "limpiando":
                aspiradora.recoger_polvo()
            else:
                print("La aspiradora no está encendida, por favor inicie la limpieza.")
        elif opcion == "3":
            print(aspiradora)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
