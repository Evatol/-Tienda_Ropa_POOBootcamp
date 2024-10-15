Este proyecto es un sistema de gestión de productos de ropa implementado en Java, siguiendo principios de Programación Orientada a Objetos (POO). 

## Clases Implementadas

1) **Producto**: Clase base que representa un producto general.
2) **Ropa**: Hereda de Producto y añade características específicas de la ropa.
3) **Camisa, Pantalon, Zapato**: Clases específicas que heredan de Ropa, con atributos particulares.
4) **Tienda**: Maneja los productos disponibles y las compras.
5) **Carrito**: Almacena los productos seleccionados para la compra.

## Pilares de POO Implementados
1) **Encapsulamiento**: Atributos encapsulados con métodos getters y setters.
2) **Herencia**: Ropa hereda de Producto, y las clases específicas heredan de Ropa.
3) **Polimorfismo**: Método `mostrar_info` sobrescrito en cada clase hija.
4) **Abstracción**: Oculta detalles internos del proceso de compra.

## Interacción con el Usuario
El programa permite a los usuarios seleccionar productos de un menú, almacenarlos en un carrito y al finalizar la compra, mostrar un resumen con los productos seleccionados y el total a pagar.

## Uso
Para ejecutar el programa, utiliza un IDE compatible con Java y asegúrate de tener configurada la versión correcta de Java.
