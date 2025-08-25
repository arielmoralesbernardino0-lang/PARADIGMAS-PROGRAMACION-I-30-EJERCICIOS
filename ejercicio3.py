# Definición de la clase Nota
class Nota:
    def __init__(self, nota, nombreEstudiante):
        self.nota = nota
        self.nombreEstudiante = nombreEstudiante

    def ha_pasado(self):
        if self.nota > 75:
            print(f"El/La estudiante {self.nombreEstudiante} aprobo.")
        else:
            print(f"El/La estudiante {self.nombreEstudiante} reprobo.")

# Ejemplo de uso
nota_1 = Nota(80, "Julien")
nota_1.ha_pasado()

nota_2 = Nota(35, "Amélie")
print(f"La nota obtenida por {nota_2.nombreEstudiante} en la primera corrección es: {nota_2.nota}")

# Actualizamos la nota tras una segunda corrección
nota_2.nota = 70
print(f"Después de una segunda corrección, la nota de {nota_2.nombreEstudiante} es: {nota_2.nota}")

nota_2.ha_pasado()
