class Paleta:
    def __init__(self, sabor:str, precio:float):
        self.sabor = sabor
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f"Sabor: {self.sabor}")
        print(f"Precio: ${self.precio}")
    
    
class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, base_agua=True):
        super().__init__(sabor, precio)
        self.base_agua = base_agua
        
    def mostrar_base_agua(self):
        if self.base_agua:
            print("Sí es a base de agua")
        else:
            print("No es a base de agua") 
            
    def precio_final(self):
        return self.precio + 2
            
        
class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa=True):
        super().__init__(sabor, precio)
        self.cremosa = cremosa
     
    def mostrar_base_cremosa(self):
        if self.cremosa:
            print("Sí es cremosa")
        else:
            print("No es cremosa")
            
    def precio_final(self):
        return self.precio + 6
            
            
def main():
    agua = PaletaAgua("Limón", 15)
    crema = PaletaCrema("Chocolate", 34) 
    
    agua.mostrar_informacion()
    agua.mostrar_base_agua()
    print(f"El precio final es de ${agua.precio_final()}")
    
    print("---------------")
    
    crema.mostrar_informacion()
    crema.mostrar_base_cremosa()
    print(f"El precio final es de ${crema.precio_final()}")
    
    
if __name__ == "__main__":
    main()
