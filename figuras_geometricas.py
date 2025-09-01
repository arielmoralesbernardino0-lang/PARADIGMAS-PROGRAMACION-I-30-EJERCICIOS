from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Uso
figuras = [
    Cuadrado(5),
    Rectangulo(4, 6),
    Circulo(3)
]

for f in figuras:
    print(f"{f.nombre} -> Área: {f.calcular_area():.2f}")
