# Bot de Gestión de Inventario - Proyecto Final Python Básico (Science Link)

# Estructura inicial del inventario como diccionario
inventario = {
    'Manzanas': {'cantidad': 50, 'precio': 1.50},
    'Leche': {'cantidad': 20, 'precio': 2.75},
    'Pan': {'cantidad': 10, 'precio': 3.00}
}

# Función para añadir un nuevo producto
def anadir_producto():
    print("\n--- Añadir Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    if nombre in inventario:
        print(f"Error: El producto '{nombre}' ya existe en el inventario.")
        return
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal.")
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print(f"Producto '{nombre}' añadido exitosamente.")

# Función para actualizar el stock de un producto existente
def actualizar_stock():
    print("\n--- Actualizar Stock de Producto ---")
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
    if nombre not in inventario:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return
    print(f"Producto '{nombre}' encontrado. Cantidad actual: {inventario[nombre]['cantidad']}")
    while True:
        try:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombre}': "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    inventario[nombre]['cantidad'] = nueva_cantidad
    print(f"Stock de '{nombre}' actualizado a {nueva_cantidad}.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
    if nombre not in inventario:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return
    confirmacion = input(f"¿Está seguro de que desea eliminar '{nombre}' del inventario? (s/n): ").lower()
    if confirmacion == 's':
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print("Eliminación cancelada.")

# Función para mostrar todos los productos del inventario
def ver_inventario():
    print("\n--- Ver Inventario ---")
    if not inventario:
        print("El inventario está vacío.")
        return
    for nombre, detalles in inventario.items():
        print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")

# Función para buscar productos por nombre o parte del nombre
def buscar_producto():
    print("\n--- Buscar Producto ---")
    termino = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
    encontrados = []
    for nombre, detalles in inventario.items():
        if termino in nombre.lower():
            encontrados.append((nombre, detalles))
    if encontrados:
        print("--- Resultados de la Búsqueda ---")
        for nombre, detalles in encontrados:
            print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")
    else:
        print(f"No se encontraron productos que coincidan con '{termino}'.")

# Función para mostrar el resumen del inventario
def resumen_inventario():
    print("\n--- Resumen del Inventario ---")
    valor_total = sum(det['cantidad'] * det['precio'] for det in inventario.values())
    print(f"Valor Total del Inventario: ${valor_total:.2f}")
    
    umbral = 5
    bajos = [nombre for nombre, det in inventario.items() if det['cantidad'] < umbral]
    if bajos:
        print(f"Productos con bajo stock (cantidad < {umbral}):")
        for nombre in bajos:
            print(f"- {nombre} (Cantidad: {inventario[nombre]['cantidad']})")
    else:
        print("No hay productos con bajo stock.")
    
    if any(det['cantidad'] == 0 for det in inventario.values()):
        print("¡Advertencia! Hay al menos un producto agotado.")
    else:
        print("No hay productos agotados.")
    
    if inventario:
        if all(det['cantidad'] > 0 for det in inventario.values()):
            print("Todos los productos tienen stock positivo.")
        else:
            print("Algunos productos tienen stock cero o negativo.")
    else:
        print("El inventario está vacío.")

# Función principal con menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir Producto")
        print("2. Actualizar Stock")
        print("3. Eliminar Producto")
        print("4. Ver Inventario")
        print("5. Buscar Producto")
        print("6. Resumen de Inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            anadir_producto()
        elif opcion == '2':
            actualizar_stock()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            ver_inventario()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            resumen_inventario()
        elif opcion == '7':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
