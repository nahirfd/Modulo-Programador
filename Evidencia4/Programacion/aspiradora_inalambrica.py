class AspiradoraRobot:
    def __init__(self, capacidad_polvo=100):
        self.__capacidad_polvo = capacidad_polvo
        self.__polvo_recogido = 0
        self.__encendida = False

    @property
    def capacidad_polvo(self):
        return self.__capacidad_polvo

    @property
    def polvo_recogido(self):
        return self.__polvo_recogido

    @property
    def encendida(self):
        return self.__encendida

    def encender(self):
        self.__encendida = True
        print("La aspiradora está encendida.")

    def recoger_polvo(self, cantidad=10):
        if self.__encendida:
            if self.__polvo_recogido + cantidad <= self.__capacidad_polvo:
                self.__polvo_recogido += cantidad
                print(f"Recogidos {cantidad} gramos de polvo. Polvo recogido total: {self.__polvo_recogido}g")
            else:
                print("El contenedor de polvo está lleno. Vacíalo antes de continuar.")
        else:
            print("La aspiradora está apagada. No puede recoger polvo.")

    def apagar(self):
        self.__encendida = False
        print("La aspiradora está apagada.")

    def __str__(self):
        capacidad_restante = self.__capacidad_polvo - self.__polvo_recogido
        estado = "encendida" if self.__encendida else "apagada"
        return (f"AspiradoraRobot(estado={estado}, polvo_recogido={self.__polvo_recogido}g, "
                f"capacidad_restante={capacidad_restante}g)")

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Encender aspiradora")
    print("2. Recoger polvo")
    print("3. Apagar aspiradora")
    print("4. Mostrar estado de la aspiradora")
    print("5. Salir")

def main():
    aspiradora = AspiradoraRobot()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            aspiradora.encender()
        elif opcion == "2":
            aspiradora.recoger_polvo()
        elif opcion == "3":
            aspiradora.apagar()
        elif opcion == "4":
            print(aspiradora)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
