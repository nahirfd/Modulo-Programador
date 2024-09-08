class AspiradoraRobot:
    def __init__(self, capacidad_polvo=100):
        self.capacidad_polvo = capacidad_polvo
        self.polvo_recogido = 0
        self.encendida = False

    def encender(self):
        self.encendida = True
        print("La aspiradora está encendida.")

    def recoger_polvo(self, cantidad=10):
        if self.encendida:
            if self.polvo_recogido + cantidad <= self.capacidad_polvo:
                self.polvo_recogido += cantidad
                print(f"Recogidos {cantidad} gramos de polvo. Polvo recogido total: {self.polvo_recogido}g")
            else:
                print("El contenedor de polvo está lleno. Vacíalo antes de continuar.")
        else:
            print("La aspiradora está apagada. No puede recoger polvo.")

    def apagar(self):
        self.encendida = False
        print("La aspiradora está apagada.")

    def __str__(self):
        capacidad_restante = self.capacidad_polvo - self.polvo_recogido
        estado = "encendida" if self.encendida else "apagada"
        return (f"AspiradoraRobot(estado={estado}, polvo_recogido={self.polvo_recogido}g, "
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

