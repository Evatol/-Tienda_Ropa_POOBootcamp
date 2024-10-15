#creamos la clase producto
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def mostrar_info(self):
        print(f"Producto: {self.__nombre}, Precio: {self.__precio}")
