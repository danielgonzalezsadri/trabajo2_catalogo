from catalogo.catalogo_manager import CatalogoManager


def main():
    gestor = CatalogoManager()

    print("Insertando un nuevo ítem de prueba...")
    gestor.insertar_item({"nombre": "Producto 1", "precio": 9.99})

    print("Items en el catálogo:")
    for item in gestor.listar_items():
        print(item)

    gestor.cerrar_conexion()


if __name__ == "__main__":
    main()
