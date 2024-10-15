from producto import Producto

class Zapato(Producto):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio)
        self.__talla = talla
        self.__tipo_material = tipo_material  # Ejemplo: 'Cuero', 'Sintético'

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.__talla}, Tipo de Material: {self.__tipo_material}")
