from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from superclase.vehiculo import Vehiculo

def ejecutar_programa():
    
    coche = Coche("rojo", 4, 180, 2000)
    bicicleta = Bicicleta("verde", 2, "urbana")
    camioneta = Camioneta("negra", 4, 160, 3000, 1000)
    motocicleta = Motocicleta("azul", 2, "deportiva", 220, 1000)

    vehiculos = [coche, bicicleta, camioneta, motocicleta]


    print("Todos los vehículos:")
    Vehiculo.catalogar(vehiculos)

    print("\nFiltrar por vehículos tipo 'Coche':")
    Vehiculo.catalogar(vehiculos, "Coche")

    print("\nFiltrar por vehículos tipo 'Bicicleta':")
    Vehiculo.catalogar(vehiculos, "Bicicleta")

    print("\nFiltrar por vehículos tipo 'Camioneta':")
    Vehiculo.catalogar(vehiculos, "Camioneta")

    print("\nFiltrar por vehículos tipo 'Motocicleta':")
    Vehiculo.catalogar(vehiculos, "Motocicleta")

