class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: No se pueden depositar cantidades negativas o nulas.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: No se pueden retirar cantidades negativas o nulas.")
        elif cantidad > self.__saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular



if __name__ == "__main__":
    nombre = input("Ingrese el nombre del titular: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))

    cuenta = CuentaBancaria(nombre, saldo_inicial)

    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar titular")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Saldo actual:", cuenta.consultar_saldo())
        elif opcion == "2":
            cantidad = float(input("Ingrese cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Ingrese cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "4":
            print("Titular:", cuenta.consultar_titular())
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

