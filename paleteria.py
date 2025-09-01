class Paleta:
    def __init__(self, sabor:str, precio:float):
        self.sabor = sabor
        self.precio = precio
    
    def precio_final(self):
        return self.precio  


class PaletaAgua(Paleta):
    def __init__(self, sabor, precio):
        super().__init__(sabor, precio)
    
    def precio_final(self):
        return self.precio + 2


class PaletaCrema(Paleta):
    def __init__(self, sabor, precio):
        super().__init__(sabor, precio)
    
    def precio_final(self):
        return self.precio + 6


def main():
    paletas = [
        PaletaAgua("Limón", 15),
        PaletaCrema("Chocolate", 34)
    ]
    
    print("Lista de Paletas y Precios Finales")
    print("-"*40)
    for p in paletas:
        print(f"Paleta de {p.sabor:<10} | Precio Final = ${p.precio_final()}")


if __name__ == "__main__":
    main()