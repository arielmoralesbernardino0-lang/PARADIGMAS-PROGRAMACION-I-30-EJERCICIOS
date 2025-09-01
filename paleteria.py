from abc import ABC, abstractmethod

class Paleta(ABC):
    def __init__(self, sabor):
        self.sabor = sabor

    @abstractmethod
    def mostrar_descripcion(self):
        pass

class PaletaAgua(Paleta):
    def mostrar_descripcion(self):
        print(f"Paleta de agua sabor {self.sabor} ")

class PaletaLeche(Paleta):
    def mostrar_descripcion(self):
        print(f"Paleta de leche sabor {self.sabor} ")

class PaletaMixta(Paleta):
    def mostrar_descripcion(self):
        print(f"Paleta mixta de {self.sabor} ")

# Uso
paletas = [
    PaletaAgua("Limón"),
    PaletaLeche("Fresa"),
    PaletaMixta("Mango con chile")
]

for p in paletas:
    p.mostrar_descripcion()
