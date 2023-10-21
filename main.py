class RegistroProducto:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        id = int(input("\nIngrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        costo = float(input("Ingrese el costo del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))
        margen_de_venta = float(input("Ingrese el margen de venta (porcentaje): ")) / 100  # Convierte a decimal

        precio_venta = round(costo / (1 - margen_de_venta), 2)

        producto = {
            'identificacion': id,
            'nombre_producto': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_venta': precio_venta,
            'margen_de_venta': margen_de_venta
        }
        self.productos.append(producto)
        self.productos.sort(key=lambda x: x['identificacion'])

    def imprimir_productos(self):
        print("\n <- Listado de productos:")
        for producto in self.productos:
            print(f"\nID: {producto['identificacion']}")
            print(f"Nombre: {producto['nombre_producto']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Costo: {producto['costo']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio de Venta: {producto['precio_venta']}")

registro = RegistroProducto()

while True:
    print("\nMenú:")
    print("1. Registrar un producto")
    print("2. Ver la lista de productos registrados")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        registro.registrar_producto()
    elif opcion == '2':
        registro.imprimir_productos()
        input("\n  enter para continuar ")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")