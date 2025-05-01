from catalogo.catalogo_manager import CatalogoManager

def mostrar_menu():
    print("\n--- Menú del gestor de catálogo ---")
    print("1. Insertar producto")
    print("2. Listar productos")
    print("3. Eliminar producto")
    print("4. Modificar producto")
    print("5. Buscar producto")
    print("6. Salir")

def main():
    gestor = CatalogoManager()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            gestor.insertar_item({"nombre": nombre, "precio": precio})
            print(" Producto insertado correctamente.")

        elif opcion == "2":
            print(" Productos en el catálogo:")
            for item in gestor.listar_items():
                print(item)

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            resultado = gestor.eliminar_item({"nombre": nombre})
            print(" Producto eliminado." if resultado.deleted_count > 0 else "❌ No se encontró el producto.")

        elif opcion == "4":
            nombre = input("Nombre del producto a modificar: ")
            nuevo_nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deja vacío para no cambiar): ")

            nuevos_valores = {}
            if nuevo_nombre:
                nuevos_valores["nombre"] = nuevo_nombre
            if nuevo_precio:
                nuevos_valores["precio"] = float(nuevo_precio)

            if nuevos_valores:
                resultado = gestor.actualizar_item({"nombre": nombre}, nuevos_valores)
                if resultado.modified_count > 0:
                    print(" Producto actualizado.")
                else:
                    print(" No se encontró el producto o no se modificó nada.")
            else:
                print("️ No se indicó ningún cambio.")

        elif opcion == "5":
            nombre = input("Nombre del producto a buscar: ")
            resultados = gestor.buscar_item({"nombre": nombre})
            if resultados:
                print(" Productos encontrados:")
                for item in resultados:
                    print(item)
            else:
                print(" No se encontraron productos con ese nombre.")

        elif opcion == "6":
            print(" Saliendo del programa...")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.")

    gestor.cerrar_conexion()

if __name__ == "__main__":
    main()
