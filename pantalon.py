from ropa import Ropa

class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, largo):
        super().__init__(nombre, precio, talla)
        self.__tipo_tela = tipo_tela
        self.__largo = largo  # Ejemplo: 'Corto', 'Regular', 'Largo'

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Tela: {self.__tipo_tela}, Largo: {self.__largo}")
