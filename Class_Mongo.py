import pymongo
class Mongodb:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb =self.myclient["Prueba"]
        self.mycol = self.mydb["personas"]
        self.mycol2 = self.mydb["material"]
        self.mycol3 = self.mydb["pedidos"]
        self.list = []
    def comprobarcollecion(self):
        collist = self.mydb.list_collection_names()
        for i in collist:
          if i=="personas":
              self.mycol.drop()
          if i == "material":
            self.mycol2.drop()
          if i=="pedidos":
            self.mycol3.drop()
    def ingresarpersona(self,id,nombre,edad,celular):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["Prueba"]
        self.mycol = self.mydb["personas"]
        self.mydict = {"_id": id, "nombre": nombre, "edad": edad, "celular": celular}
        self.mycol.insert_one(self.mydict)
    def actualizarpersona(self,id,edad,celular):
        self.myquery = {"_id":id}
        self.newvalues = {"$set": {"edad": edad, "celular": celular}}
        self.mycol.update_one( self.myquery, self.newvalues)
    def eliminarpersona(self,id):
        myquery = {"_id": id}
        self.mycol.delete_one(myquery)
    def verificardatos(self):
        return  self.mycol
    #materiales
    def ingresarmaterial(self, id, nombre,fechadecaducacion):
        self.mydict = {"_id": id, "nombre": nombre, "fechadecaducacion": fechadecaducacion}
        self.mycol2.insert_one(self.mydict)
    def actualizarmaterial(self,id,fechadecaducacion):
        self.myquery = {"_id":id}
        self.newvalues = {"$set": { "fechadecaducacion": fechadecaducacion}}
        self.mycol2.update_one( self.myquery, self.newvalues)
    def eliminarmaterial(self,id):
        myquery = {"_id": id}
        self.mycol2.delete_one(myquery)
    def verificarmaterial(self):
        return  self.mycol2
    #pedidos
    def ingresarpedido(self, id, nombre,producto):
        self.mydict = {"_id": id, "nombre": nombre, "producto": producto}
        self.mycol3.insert_one(self.mydict)
    def actualizarpedido(self,id,producto):
        self.myquery = {"_id":id}
        self.newvalues = {"$set": { "producto": producto}}
        self.mycol3.update_one( self.myquery, self.newvalues)
    def eliminarpedido(self,id):
        myquery = {"_id": id}
        self.mycol3.delete_one(myquery)
    def verificarpedido(self):
        return  self.mycol3