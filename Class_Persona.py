from datetime import datetime
from io import open
import pandas as pd
from Class_MYSQL import Database as Mysql
from Class_Mongo import Mongodb
import pymongo
mydb=Mysql()
mongo=Mongodb()


class Persona:

    def __init__(self,id=None,nombre="", edad="",celular=""):
        self.idp=id
        self.nombre = nombre
        self.edad = edad
        self.celular=celular
        self.list = []
        self.x=0
        self.y=0
        self.importacion = pd.read_csv('Personas.csv')
        self.id = self.importacion['idp']
        self.nombre2 = self.importacion['nombre']
        self.edad2= self.importacion['edad']
        self.celular2 = self.importacion['celular']
        self.personas=''
    def agregarpersona(self,nombre,edad,celular):
                 basededatos = Persona.regreso(self)
                 for i in basededatos:
                       bd = int(i)
                 self.personas=open("Personas.csv", "a",newline='')
                 self.x+=1
                 self.idp=self.x
                 new=Persona(self.idp,nombre,edad,celular)
                 self.personas.write(str(self.idp)+","+nombre+","+edad+","+celular+'\n')
                 self.personas.close()
                #mysql
                 if bd==1:
                   mydb.agregarapersona(str(self.idp),nombre,edad,celular)
                 #mongodb
                 if bd==2:
                   mongo.ingresarpersona(str(self.idp),nombre, edad, celular)
                 return self.list.append(new)


    def actualizarpersona(self,nombre,edad,celular):
        basededatos = Persona.regreso(self)
        for i in basededatos:
            bd = int(i)
        c=0
        e=0
        s=0
        for element in self.list:

          if(element.nombre==nombre):

            g=element.idp
            s=1
          else:
              if (element.idp != ""):
                  if(s==0):
                     c+=1
        if (s == 1):
               d = 0
               print(g)
               new = Persona(g, nombre, edad, celular)
               self.personas = open('Personas.csv', 'r+')
               texto = self.personas.readlines()
               texto[c+1] =(str(g)+","+nombre+","+edad+","+celular+'\n')
               #mysql
               if bd == 1:
                mydb.actualizarpersona(edad,celular,g)
               #mongodb
               if bd == 2:
                 mongo.actualizarpersona(g,edad,celular)
               self.personas.seek(0)
               self.personas.writelines(texto)
               self.personas.close()
               self.list[c] = new
        e=1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")


    def eliminarpersona(self, nombre=None):
        basededatos = Persona.regreso(self)
        for i in basededatos:
            bd = int(i)
        c = 0
        for element in self.list:

            if (element.nombre == nombre):
                self.personas = open("Personas.csv", "r+")
                lineas =self.personas.readlines()
                self.personas.close()
                self.personas= open("Personas.csv", "w")
                for linea in lineas:
                    if linea!= (str(element.idp)+","+nombre+","+element.edad+","+element.celular+'\n'):
                        self.personas.write(linea)
                self.list.pop(c)
                #mysql
                if bd==1:

                  mydb.eliminarpersona(element.idp)

                #mongodb
                if bd == 2:
                   mongo.eliminarpersona(element.idp)

                self.personas.close()
            c += 1

    def verpersonas(self, nombre=None):
        c = 0
        a=0
        if(nombre!=None):

          for element in self.list:

            if (element.nombre == nombre):
                return self.list[c]
                a=1
            c += 1
          if(a==0):
              nombre =""
              edad=""
              idp=""
              celular=""
              new = Persona(idp, nombre, edad, celular)

              return new
        else :
            return self.list

    def pasarpersona(self, id=None):
        c = 0
        a = 0
        if (id != None):
            for element in self.list:

                if (element.idp == id):
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
    def pasardatospersonas(self):
        basededatos = Persona.regreso(self)
        for i in basededatos:
           bd=int(i)
        if bd == 1:
          desigualdad=mydb.verificardatoserroneos()
        if bd == 2:
          mongodesigualdad=mongo.verificardatos()
        cont=0
        for j in range(len(self.nombre2)):
            id=self.id[j]
            nombre3 = str(self.nombre2[j])
            edad3 = str(self.edad2[j])
            celular3 = str(self.celular2[j])
            self.x =id
            self.idp = self.x
            new = Persona(str(self.idp), nombre3, edad3, celular3)
          #condicion mysql
            if bd == 1:
              for x in desigualdad:
                for i in x:
                    if id == i:
                        cont=1
              if cont==0:
                mydb.agregarapersona(str(self.idp),nombre3, edad3, celular3)
              cont=0
        #condicion mongodb
            if bd == 2:
               for x in mongodesigualdad.find():
                    d =int(x['_id'])
                    if d == id:
                       cont=1

               if cont==0:

                  mongo.ingresarpersona(str(self.idp),nombre3, edad3, celular3)
               cont=0
            self.list.append(new)
    def basededatos(self,opcion):
        self.y=opcion
    def regreso(self):
       return  self.y
    def persona(self, idp=""):
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