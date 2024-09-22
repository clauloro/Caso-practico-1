class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

    @staticmethod
    def catalogar(vehiculos, tipo=None):
        if tipo is not None:
            vehiculos_filtrados = [v for v in vehiculos if type(v).__name__ == tipo]
            print("Se han encontrado {} vehículos del tipo {}:".format(len(vehiculos_filtrados), tipo))
            for v in vehiculos_filtrados:
                print(v)
        else:
            for v in vehiculos:
                print("{}: {}".format(type(v).__name__, v))

