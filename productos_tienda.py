# Programa: Registro de productos de una tienda
# Uso de listas en Python

# Lista inicial de productos
productos = ["Arroz", "Azúcar", "Leche"]

# Mostrar productos registrados
print("PRODUCTOS REGISTRADOS")
print("---------------------")

for producto in productos:
    print(producto)

# Agregar un nuevo producto
nuevo_producto = input("\nIngrese un nuevo producto: ")
productos.append(nuevo_producto)

print("\nProducto agregado correctamente.")

# Mostrar lista actualizada
print("\nLISTA ACTUALIZADA")

for producto in productos:
    print(producto)

# Buscar un producto
buscar = input("\nIngrese el producto que desea buscar: ")

if buscar in productos:
    print("El producto sí se encuentra registrado.")
else:
    print("El producto no se encuentra registrado.")

# Eliminar un producto
eliminar = input("\nIngrese el producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado correctamente.")
else:
    print("El producto no existe en la lista.")

# Mostrar lista final
print("\nPRODUCTOS FINALES")

for producto in productos:
    print(producto)
