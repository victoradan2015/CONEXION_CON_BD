from Class_Persona import Persona
from Class_Material import  Material as Pe
from Class_Listadepedidos import Listadepedidos as L
from  Class_interface import Inteface
from colorama import *
from Class_MYSQL import Database as Mysql
from Class_Mongo import Mongodb
import random

if __name__ == "__main__":
 my=Mysql()
 mongo = Mongodb()
 opcion=0

 print("En que base de datos quieres guardar"
        "\n1)Mysql"
        "\n2)Mongo DB")
 opcion = (input(Fore.LIGHTRED_EX + "Seleccione una opcion:"))
#SE SELCCIONA BD ALETAORIAMENTE
 opcion = str(opcion)
 if opcion == "1":
    print("-----BD FUNCIONANDO CON MYSQL-----")
 elif opcion == "2":
     mongo.comprobarcollecion()
     print("-----BD FUNCIONANDO CON MongoDB-----")


 if opcion == "1":
   my.compruebalabasededatos()
 l=L()
 P=Pe()
lista = Persona()
lista.basededatos(opcion)
P.basededatos(opcion)
l.basededatos(opcion)
accion=0
lista.pasardatospersonas()
P.Extraerdatos()
l.pasardatospedidos()
while accion >=0 and accion <=16:
    i = Inteface()
    i.Menu()
    accion = int(input( Fore.LIGHTRED_EX+"Seleccione una opcion:"))
    if accion == 1:
        nombre = input("Ingrese su nombre: ")
        edad = input("su edad: ")
        celular = input("ingrese su celular:")
        lista.agregarpersona(nombre,edad,celular)
    elif accion == 2:
        print("<-----LISTA DE USUARIOS GUARDADOS----->")
        objeto = lista.verpersonas()
        for i in objeto:
            print("id|","nombre|","edad|","celular")
            print(str(i.idp) + "|" + i.nombre + "|  " + i.edad + "  |" + i.celular)
    elif accion == 3:
        p=0
        objeto = lista.verpersonas()
        for i in objeto:
            print("id|","nombre|","edad|","celular")
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
        numero = input("ingrese su nombre:")
        edad = input("su nueva edad: ")
        celular = input("su nuevo celular:")
        lista.actualizarpersona(numero,edad,celular)
    elif accion == 4:
        objeto = lista.verpersonas()
        for i in objeto:
            print("id|","nombre|","edad|","celular")
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
        nombre = input("Ingresa el nombre de usuario a eliminar:")
        objeto = lista.verpersonas(nombre)
        if (objeto.nombre != ""):
             condicion=l.verlistadepedios(objeto.idp)
             if condicion.nombre!="":
                print("No se puede eliminar la persona por que se encuentra el la tabla de pedidos")
             if condicion.nombre=="":
                    lista.eliminarpersona(nombre)
                    print("Usuario eliminado")
        else:
             print("No existe el usuario")
    elif accion == 5:
        nombre = input("Ingresa al usuario que deseas ver:")
        i = lista.verpersonas(nombre)
        if(i.nombre!=""):
            print("id|","nombre|","edad|","celular")
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
    elif accion == 6:
        nombre = input("Ingrese el Producto: ")
        fecha = input("fecha de caducacion: ")
        P.agregarproducto(nombre,fecha)
    elif accion == 7:
        print("<-----PRODCUTOS DISPONIBLES----->")
        objeto2 = P.verproductos()
        for i in objeto2:
            if (i.nombre != ""):
                 print("id|","nombre|","fecha de caducidad|")
                 print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
    elif accion == 8:
        objeto2 = P.verproductos()
        for i in objeto2:
            print("id|","nombre|","fecha de caducidad|")
            print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
        nombre = input("Ingrese el Producto: ")
        fecha = input("fecha de caducacion: ")
        P.actualizarproducto(nombre,fecha)
    elif accion == 9:
        objeto2 = P.verproductos()
        for i in objeto2:
            print("id|","nombre|","fecha de caducidad|")
            print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
        nombre = input("Ingrese el Producto a eliminar: ")
        i = P.verproductos(nombre)
        if (i.nombre != ""):
            condicion=l.verlistadepedios2(i.idp)
            if condicion.nombre != "":
                print("No se puede eliminar el material por que se encuentra en la tabla de pedidos")
            if condicion.nombre == "":
                P.eliminarproducto(nombre)
                print("Material eliminado")
        else:
         print("No existe ")
    elif accion == 10:
        nombre = input("Ingrese el Producto a ver: ")
        i = P.verproductos(nombre)
        if (i.nombre != ""):
             print("id|","nombre|","fecha de caducidad|")
             print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
    elif accion == 11:
        s=0
        f=0
        print("-----------------USUARIOS A SELECCIONAR--------------------")
        objeto = lista.verpersonas()
        for i in objeto:
            print("||"  + i.nombre + "||")
        print("-----------------PRODUCTOS A SELECCIONAR--------------------")
        objeto2 = P.verproductos()
        for i in objeto2:
            print("||"+ i.nombre +"||")
        print("***********************************************************")
        name = input("Ingresa al usuario de la lista:")
        objeto = lista.verpersonas()
        for i in objeto:
          if (i.nombre==name):
               s=1
               persona=i.idp
        if(s==1):
            producto = input("Ingrese el Producto: ")
            i = P.verproductos(producto)
            if (i.nombre != ""):
               l.agregarlistadepedido(persona,i.idp)
            else:
              f=1
        if(f==1):
            print("no se encuentra el producto")
        if(s==0):
         print("no existe el usuario")
    elif accion==12:
        print("<-----PRODUCTOS RENTADOS----->")
        objeto3=l.verlistadepedios()
        for i in objeto3:
            if (i.producto != ""):
                pro=str(i.producto)
                nombre=str(i.nombre)
                nombre=lista.persona(nombre)
                producto=P.productos(pro)
                print("nombre||producto")
                print(nombre +"||" + producto)

    elif accion==13:
        objeto3 = l.verlistadepedios()
        for i in objeto3:
            if (i.producto != ""):
                pro = str(i.producto)
                nombre = str(i.nombre)
                nombre = lista.persona(nombre)
                producto = P.productos(pro)
                print("nombre||producto")
                print(nombre + "||" + producto)
        name = input("Ingresa al usuario de la lista:")
        objeto = lista.verpersonas()
        for i in objeto:
            if (i.nombre == name):
                s = 1
                persona = i.idp
        if (s == 1):
            if (i.nombre != ""):
                l.eliminarpedido(persona)
        if (s == 0):
            print("no existe el usuario")
    elif accion == 14:
        s=0
        objeto3 = l.verlistadepedios()
        for i in objeto3:
            if (i.producto != ""):
                pro = str(i.producto)
                nombre = str(i.nombre)
                nombre = lista.persona(nombre)
                producto = P.productos(pro)
                print("nombre||producto")
                print(nombre + "||" + producto)
        name = input("Ingresa al usuario de la lista:")
        i = lista.verpersonas(name)
        print(i.nombre)
        if (i.nombre == name):
            persona=i.idp
            s = 1
        if (s == 1):
            print("-----------------PRODUCTOS A SELECCIONAR--------------------")
            objeto2 = P.verproductos()
            for i in objeto2:
                print("||nombre||fecha de caducidad||")
                print("||"+ i.nombre + "||" + i.fechacaducacion + "||")
            print("***********************************************************")
            producto = input("Ingrese el Producto nuevo: ")
            i = P.verproductos(producto)
            if(i.nombre!=""):
               l.actualizarproducto(persona,i.idp)
        if (s == 0):
                print("no existe el usuario")
    elif accion == 15:
        print("1.  Busqueda por persona")
        print("2.- Busqueda por producto")
        seleccion = int(input("Seleccione una opcion:"))
        if seleccion==1:
            s=0
            objeto3 = l.verlistadepedios()
            for i in objeto3:
                if (i.nombre != ""):
                    nombre = str(i.nombre)
                    nombre = lista.persona(nombre)
                    producto=P.productos(i.producto)
                    print("nombre||producto")
                    print(nombre + "||"  + producto)
            name = input("Ingresa al usuario a ver:")
            i = lista.verpersonas(name)
            if (i.nombre == name):
                print("id|nombre|edad|celular")
                print(str(i.idp) +"|" + i.nombre + "|" + i.edad +"|" + i.celular)
                s = 1
            if (s == 0):
                print("no existe el usuario")
        elif seleccion==2:
            s = 0
            objeto3 = l.verlistadepedios()
            for i in objeto3:
                if (i.nombre != ""):
                    nombre = str(i.nombre)
                    nombre = lista.persona(nombre)
                    producto = P.productos(i.producto)
                    print("nombre||producto")
                    print(nombre + "||" + producto)
            name = input("Ingresa al Producto a ver:")
            i = P.verproductos(name)
            if (i.nombre == name):
                print("id|nombre|fecha de caducidad|")
                print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
                s = 1
            if (s == 0):
                print("no existe el producto")
    elif accion == 16:

       accion=20
