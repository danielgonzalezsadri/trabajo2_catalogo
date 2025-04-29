def main():
    print("Bienvenido al gestor de catálogo")

if __name__ == "__main__":
    main()
from pymongo import MongoClient

class CatalogoManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="catalogo_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.coleccion = self.db["items"]

    def insertar_item(self, item):
        self.coleccion.insert_one(item)

    def listar_items(self):
        return list(self.coleccion.find())

    def eliminar_item(self, criterio):
        self.coleccion.delete_one(criterio)

    def cerrar_conexion(self):
        self.client.close()
