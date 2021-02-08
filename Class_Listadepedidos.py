import pandas as pd
from Class_MYSQL import Database as Mysql
from Class_Mongo import Mongodb
mongo=Mongodb()
mydb=Mysql()
class Listadepedidos:
    def __init__(self, id=None, nombre="",producto=""):
        self.idp = id
        self.nombre = nombre
        self.producto = producto
        self.list = []
        self.x = 0
        self.y = 0
        self.importacion = pd.read_csv('Listadepedidos.csv')
        self.id = self.importacion['idp']
        self.nombre2 = self.importacion['nombre']
        self.producto2 = self.importacion['producto']
        self.Listadepedidos =''
    def agregarlistadepedido(self, nombre, producto):
        basededatos = Listadepedidos.regreso(self)
        for i in basededatos:
            bd = int(i)
        self.Listadepedidos = open("Listadepedidos.csv", "a", newline='')
        self.x += 1
        self.idp = self.x
        new = Listadepedidos(self.idp, nombre, producto)
        self.Listadepedidos.write(str(self.idp) + "," + nombre + "," + producto + '\n')
        self.Listadepedidos.close()
        if bd == 1:
          mydb.agregarpedidos(str(self.idp),nombre, producto)
        #mongo
        if bd == 2:
            mongo.ingresarpedido(str(self.idp), nombre, producto)
        self.list.append(new)

    def actualizarproducto(self,  nombre, producto):
        basededatos = Listadepedidos.regreso(self)
        for i in basededatos:
            bd = int(i)
        c = 0
        e = 0
        s = 0
        for element in self.list:
            if (element.idp == nombre):
                g = element.idp
                s = 1
            else:
                if (element.idp != ""):
                    if (s == 0):
                        c += 1
            if (s == 1):
                d = 0
                new = Listadepedidos(g, nombre,producto)
                self.Listadepedidos = open('Listadepedidos.csv', 'r+')
                texto = self.Listadepedidos.readlines()
                texto[c + 1] = (str(g) + "," + nombre + "," + producto + '\n')
                if bd == 1:
                  mydb.actualizarpedido(producto, g)
                # mongodb
                if bd == 2:
                  mongo.actualizarpedido(g, producto)
                self.Listadepedidos.seek(0)
                self.Listadepedidos.writelines(texto)
                self.Listadepedidos.close()
                self.list[c] = new
            e = 1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")

    def eliminarpedido(self, nombre=None):
        basededatos = Listadepedidos.regreso(self)
        for i in basededatos:
            bd = int(i)
        c = 0
        for element in self.list:

            if (element.nombre == nombre):
                self.Listadepedidos = open("Listadepedidos.csv", "r+")
                lineas = self.Listadepedidos.readlines()
                self.Listadepedidos.close()
                self.Listadepedidos = open("Listadepedidos.csv", "w")
                for linea in lineas:
                    if linea != (str(element.idp) + "," + nombre + "," + element.producto + '\n'):
                        self.Listadepedidos.write(linea)
                self.list.pop(c)
                if bd == 1:
                  mydb.eliminarpedido(element.idp)
                # mongodb
                if bd == 2:
                    mongo.eliminarpedido(element.idp)
                self.Listadepedidos.close()


            c += 1

    def verlistadepedios(self, nombre=None):
        c = 0
        a = 0
        if (nombre != None):

            for element in self.list:

                if (element.nombre == nombre):
                    return self.list[c]
                    a = 1
                c += 1
            if (a == 0):
                nombre = ""
                idp = ""
                producto = ""
                new = Listadepedidos(idp, nombre, producto)

                return new

        else:
            return self.list
    def verlistadepedios2(self, nombre=None):
        c = 0
        a = 0
        if (nombre != None):
            for element in self.list:
                if (element.producto == nombre):
                    return self.list[c]
                    a = 1
                c += 1
            if (a == 0):
                nombre = ""
                idp = ""
                producto = ""
                new = Listadepedidos(idp, nombre, producto)

                return new

        else:
            return self.list
    def pasardatospedidos(self):
        basededatos = Listadepedidos.regreso(self)
        for i in basededatos:
            bd = int(i)
        if bd == 1:
            desigualdad = mydb.verificarpedidoserroneos()
        if bd == 2:
          mongodesigualdad=mongo.verificarpedido()
        cont = 0
        for j in range(len(self.nombre2)):
            id = self.id[j]
            nombre3 = str(self.nombre2[j])
            producto3 = str(self.producto2[j])
            self.x = id
            self.idp = self.x
            new = Listadepedidos(str(self.idp), nombre3, producto3)
            if bd == 1:
              for x in desigualdad:
                for i in x:
                    if id == i:
                        cont = 1
              if cont == 0:
                mydb.agregarpedidos(str(self.idp),nombre3, producto3)
              cont = 0
            # condicion mongodb
            if bd == 2:
              for x in mongodesigualdad.find():
                 d = int(x['_id'])
                 if d == id:
                    cont = 1

              if cont == 0:
                mongo.ingresarpedido(str(self.idp), nombre3, producto3)
              cont = 0
            self.list.append(new)
    def basededatos(self, opcion):
        self.y = opcion

    def regreso(self):
        return self.y