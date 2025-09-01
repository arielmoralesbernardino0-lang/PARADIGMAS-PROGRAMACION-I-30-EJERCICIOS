class Personaje:
    def __init__(self, nombre:str, nivel:int):
        self.nombre = nombre
        self.nivel = nivel 
    
    def atacar(self):
        pass 


class Jugador(Personaje):
    def __init__(self, nombre, nivel, clase:str):
        super().__init__(nombre, nivel)
        self.clase = clase
    
    def atacar(self):
        print(f"{self.nombre} (Jugador {self.clase}) ataca con su habilidad especial.")


class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo:str):
        super().__init__(nombre, nivel)
        self.tipo = tipo
    
    def atacar(self):
        print(f"{self.nombre} (Enemigo {self.tipo}) lanza un ataque feroz.")


def main():
    personajes = [
        Jugador("Ojo de Halcón", 1, "Arquero"),
        Enemigo("Balgron", 10, "Dragón")
    ]
    
    print("Simulación de Batalla")
    print("-"*40)
    for p in personajes:
        p.atacar()  


if __name__ == "__main__":
    main()
