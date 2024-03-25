class Compra:
    def __init__(self, monto_total, porcentaje_descuento=10):
        self.monto_total = monto_total
        self.porcentaje_descuento = porcentaje_descuento

    def calcular_descuento(self):
        """
        Calcula el descuento aplicando el porcentaje al monto total de la compra.

        Devuelve:
        float: El monto del descuento calculado.
        """
        descuento = self.monto_total * (self.porcentaje_descuento / 100)
        return descuento

    def monto_con_descuento(self):
        """
        Calcula el monto total de la compra con el descuento aplicado.

        Devuelve:
        float: El monto total de la compra con el descuento aplicado.
        """
        return self.monto_total - self.calcular_descuento()


# Función para solicitar al usuario el monto total de la compra
def obtener_monto_total():
    while True:
        try:
            monto = float(input("Ingrese el monto total de la compra: "))
            if monto <= 0:
                print("El monto total de la compra debe ser mayor que cero.")
            else:
                return monto
        except ValueError:
            print("Por favor, ingrese un monto válido.")


def main():
    monto_total = obtener_monto_total()
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (opcional, presione Enter para 10%): ") or 10)

    compra = Compra(monto_total, porcentaje_descuento)

    descuento = compra.calcular_descuento()
    monto_final = compra.monto_con_descuento()

    print(f"El monto del descuento calculado es: {descuento}")
    print(f"El monto total de la compra con el descuento aplicado es: {monto_final}")


if __name__ == "__main__":
    main()