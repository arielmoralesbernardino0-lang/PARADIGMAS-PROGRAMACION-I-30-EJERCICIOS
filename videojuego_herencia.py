class Personaje:
    def __init__(self, nombre:str, nivel:int):
        self.nombre = nombre
        self.nivel = nivel 
        
    def atacar(self):
        print(f"{self.nombre} de nivel {self.nivel} está atacando....")
        
class Jugador(Personaje):
    def __init__(self, nombre, nivel, clase:str):
        super().__init__(nombre, nivel)
        self.clase = clase
        
    def usar_habilidad_especial(self):
        print(f"{self.nombre} está usando la habilidad especial de {self.clase}......")
        
class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo:str):
        super().__init__(nombre, nivel)
        self.tipo = tipo
        
    def gritar(self):
        print(f"{self.nombre} gritando con su tipo de grito {self.tipo}.....")
    
def main():
    jugador_1 = Jugador("Ojo de halcón", 1, "Arquero")
    enemigo_1 = Enemigo("Balgron", 10, "Dragón")
    
    jugador_1.atacar()
    jugador_1.usar_habilidad_especial()
    
    enemigo_1.atacar()
    enemigo_1.gritar()
    
if __name__ == "__main__":
    main()