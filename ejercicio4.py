import math  # Importamos la librería math para usar pi

# Definición de la clase Circulo
class Circulo:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R

    def area(self):
        return round(math.pi * self.R ** 2, 2)  # Área = π * R^2, redondeado a 2 decimales

    def perimetro(self):
        return round(2 * math.pi * self.R, 2)  # Perímetro = 2 * π * R, redondeado a 2 decimales

    def mostrar_propiedades(self):
        return f"El círculo tiene un radio de {self.R} cm, y su centro es O({self.x},{self.y})"

# Ejemplo de uso
circulo_1 = Circulo(3, 4, 5)
print(circulo_1.mostrar_propiedades())
print("El perímetro del circulo_1 es:", circulo_1.perimetro())
print("El área del circulo_1 es:", circulo_1.area())
