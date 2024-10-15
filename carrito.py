from producto import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        print("Resumen de la Compra:")
        for producto in self.productos:
            producto.mostrar_info()
            total += producto.get_precio()
        print(f"Total a Pagar: {total}")
