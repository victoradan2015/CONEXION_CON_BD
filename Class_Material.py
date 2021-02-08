from datetime import datetime
from io import open
import pandas as pd
from Class_MYSQL import Database as Mysql
from Class_Mongo import Mongodb
from Class_Persona import Persona
p=Persona()
mongo=Mongodb()
mydb=Mysql()

class Material:
    def __init__(self, id=None, nombre="", fecha=""):
        self.idp = id
        self.nombre = nombre
        self.fechacaducacion = fecha
        self.list = []
        self.x = 0
        self.y=0
        self.importacion = pd.read_csv('Productos.csv')
        self.id = self.importacion['idp']
        self.nombre2 = self.importacion['nombre']
        self.fechadecaducacion2 = self.importacion['fechadecaducacion']
        self.Productos =''
    def agregarproducto(self, nombre, fecha):
        basededatos = Material.regreso(self)
        for i in basededatos:
            bd = int(i)
        self.Productos = open("Productos.csv", "a", newline='')
        self.x += 1
        self.idp = self.x
        new = Material(self.idp, nombre, fecha)
        self.Productos.write(str(self.idp) + "," + nombre + "," + fecha + '\n')
        self.Productos.close()
        if bd == 1:
           mydb.agregarproducto(str(self.idp),nombre, fecha)
        #mongo
        if bd == 2:
           mongo.ingresarmaterial(str(self.idp), nombre, fecha)

        self.list.append(new)

    def actualizarproducto(self,  nombre, fecha):
        basededatos = Material.regreso(self)
        for i in basededatos:
            bd = int(i)
        c = 0
        e = 0
        s = 0
        for element in self.list:

            if (element.nombre == nombre):

                g = element.idp
                s = 1
            else:
                if (element.idp != ""):
                    if (s == 0):
                        c += 1
            if (s == 1):
                d = 0
                new = Material(g, nombre,fecha)
                self.personas = open('Productos.csv', 'r+')
                texto = self.personas.readlines()
                texto[c + 1] = (str(g) + "," + nombre + "," + fecha + '\n')
                if bd == 1:
                   mydb.actualizarproducto(fecha,g)
                #mongo
                if bd == 2:
                  mongo.actualizarmaterial(g,fecha)
                self.personas.seek(0)
                self.personas.writelines(texto)
                self.personas.close()
                self.list[c] = new
            e = 1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")

    def eliminarproducto(self, nombre=None):
        basededatos = Material.regreso(self)
        for i in basededatos:
            bd = int(i)
        c = 0
        for element in self.list:

            if (element.nombre == nombre):
                self.Productos = open("Productos.csv", "r+")
                lineas = self.Productos.readlines()
                self.Productos.close()
                self.Productos = open("Productos.csv", "w")
                for linea in lineas:
                    if linea != (str(element.idp) + "," + nombre + "," + element.fechacaducacion+ '\n'):
                        self.Productos.write(linea)
                self.list.pop(c)
                if bd == 1:
                   mydb.eliminarproducto(element.idp)
                   #mongo
                if bd == 2:
                  mongo.eliminarmaterial(element.idp)
                self.Productos.close()
            c += 1

    def verproductos(self, nombre=None):
        c = 0
        a=0
        if (nombre != None):

            for element in self.list:

                if (element.nombre == nombre):
                    return self.list[c]
                    a = 1
                c += 1
            if (a == 0):
                nombre = ""
                edad = ""
                idp = ""
                celular = ""
                new = Persona(idp, nombre, edad, celular)

                return new
        else:
            return self.list
    def productos(self, idp=""):
        c = 0
        a = 0

        if (idp != ""):
            for element in self.list:
                if (element.idp == idp):
                    return element.nombre
                    a = 1
                c += 1
            if (a == 0):
                nombre = ""
                idp = ""
                fecha = ""

                return nombre

        else:
            return "fallido"
    def Extraerdatos(self):
        basededatos = Material.regreso(self)
        for i in basededatos:
            bd = int(i)
        if bd == 2:
           mongodesigualdad=mongo.verificarmaterial()
        if bd == 1:
          desigualdad = mydb.verificarproductoserroneos()
        cont = 0
        for j in range(len(self.nombre2)):
            id = self.id[j]
            nombre3 = str(self.nombre2[j])
            fechadecaducacion3 = str(self.fechadecaducacion2[j])
            self.x = id
            self.idp = self.x
            new = Material(str(self.idp), nombre3, fechadecaducacion3)
            if bd == 1:
              for x in desigualdad:
                for i in x:
                    if id == i:
                        cont=1
              if cont==0:
                mydb.agregarproducto(str(self.idp),nombre3, fechadecaducacion3)
              cont=0
            #mongodb
            if bd == 2:
              for x in mongodesigualdad.find():
                 d = int(x['_id'])
                 if d == id:
                    cont = 1

              if cont == 0:

                mongo.ingresarmaterial(str(self.idp), nombre3, fechadecaducacion3)
              cont = 0
            self.list.append(new)

    def basededatos(self, opcion):
        self.y = opcion

    def regreso(self):
        return self.y