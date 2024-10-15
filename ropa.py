#importamos la clase Producto
from producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.__talla}")
