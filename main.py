from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta

# Función catalogar
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print("Se han encontrado {} vehículos con {} ruedas:".format(len(vehiculos_filtrados), ruedas))
        for v in vehiculos_filtrados:
            print("{}: {}".format(type(v).__name__, v))  
    else:
        for v in vehiculos:
            print("{}: {}".format(type(v).__name__, v))  

# Objetos de cada subclase
coche = Coche("rojo", 4, 180, 2000)
bicicleta = Bicicleta("verde", 2, "urbana")
camioneta = Camioneta("negra", 4, 160, 3000, 1000)
motocicleta = Motocicleta("azul", 2, "deportiva", 220, 1000)

# Lista de vehículos
vehiculos = [coche, bicicleta, camioneta, motocicleta]


print("Todos los vehículos:")
catalogar(vehiculos)

print("\nVehículos con 2 ruedas:")
catalogar(vehiculos, 2)

print("\nVehículos con 4 ruedas:")
catalogar(vehiculos, 4)
