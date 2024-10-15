#importamos la clase Ropa
from ropa import Ropa

class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self.__tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Tela: {self.__tipo_tela}")
