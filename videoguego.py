from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def atacar(self):
        pass

class Guerrero(Personaje):
    def atacar(self):
        print(f"{self.nombre} ataca con espada")

class Mago(Personaje):
    def atacar(self):
        print(f"{self.nombre} lanza un hechizo")

class Arquero(Personaje):
    def atacar(self):
        print(f"{self.nombre} dispara una flecha")

personajes = [
    Guerrero("Thor"),
    Mago("Merlín"),
    Arquero("Legolas")
]

for p in personajes:
    p.atacar()
