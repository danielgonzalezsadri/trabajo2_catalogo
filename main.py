from catalogo.catalogo_manager import CatalogoManager

def mostrar_menu():
    print("\n--- Menú del gestor de catálogo ---")
    print("1. Insertar producto")
    print("2. Listar productos")
    print("3. Eliminar producto")
    print("4. Salir")

def main():
    gestor = CatalogoManager()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            gestor.insertar_item({"nombre": nombre, "precio": precio})
            print("Producto insertado correctamente.")

        elif opcion == "2":
            print("Productos en el catálogo:")
            for item in gestor.listar_items():
                print(item)

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            resultado = gestor.eliminar_item({"nombre": nombre})
            print("Producto eliminado." if resultado.deleted_count > 0 else "No se encontró el producto.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

    gestor.cerrar_conexion()

if __name__ == "__main__":
    main()

