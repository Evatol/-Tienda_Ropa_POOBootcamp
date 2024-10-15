from camisa import Camisa
from pantalon import Pantalon  
from zapato import Zapato      
from carrito import Carrito

def main():
    carrito = Carrito()

    # Agregue productos de ejemplo
    camisa1 = Camisa("Camisa Azul", 30.000, "M", "Algodón")
    carrito.agregar_producto(camisa1)
    pantalon1 = Pantalon("Pantalón Negro", 79000, "L", "Denim", "Regular")
    carrito.agregar_producto(pantalon1)
    zapato1 = Zapato("Zapato Deportivo", 230000, "44", "Sintético")
    carrito.agregar_producto(zapato1)
    

    # Mostrar resumen
    carrito.mostrar_resumen()

if __name__ == "__main__":
    main()
