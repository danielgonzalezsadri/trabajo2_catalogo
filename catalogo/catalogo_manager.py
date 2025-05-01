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
        return self.coleccion.delete_one(criterio)

    def actualizar_item(self, filtro, nuevos_valores):
        return self.coleccion.update_one(filtro, {'$set': nuevos_valores})

    def buscar_item(self, filtro):
        return list(self.coleccion.find(filtro))

    def cerrar_conexion(self):
        self.client.close()
