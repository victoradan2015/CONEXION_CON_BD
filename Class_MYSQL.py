import mysql.connector
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        self.mycursor = self.mydb.cursor()
    def compruebalabasededatos(self):

        self.mycursor.execute("SHOW DATABASES")
        creardb = 0
        for x in  self.mycursor:
            for i in x:
                if i == "prueba":
                    creardb = 1
        if creardb==1:
            self.mycursor.execute("DROP DATABASE Prueba")
            creardb = 0
        if creardb == 0:
            self.mycursor.execute("CREATE DATABASE Prueba")
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor =  self.mydb.cursor()

        self.mycursor.execute("SHOW TABLES")
        tablapersonas = 0
        tablamaterial = 0
        tablapedidos = 0
        for x in  self.mycursor:
            for i in x:
                if i == "personas":
                    tablapersonas = 1
                if i == "material":
                    tablamaterial = 1
                if i == "pedidos":
                    tablapedidos = 1
        if tablapersonas == 0:
            self.mycursor.execute(
                "CREATE TABLE Personas (id INT  PRIMARY KEY, nombre VARCHAR(255), edad VARCHAR(255), "
                "celular VARCHAR(255))")
        if tablamaterial == 0:
            self.mycursor.execute(
                "CREATE TABLE Material (id INT  PRIMARY KEY, nombre VARCHAR(255), fechadecaducacion VARCHAR(255))")
        if tablapedidos == 0:
            self.mycursor.execute(
                "CREATE TABLE Pedidos (id INT  PRIMARY KEY, nombre INT, producto INT,FOREIGN KEY (nombre) REFERENCES Personas(id),FOREIGN KEY (producto) REFERENCES Material(id))")
    def agregarapersona(self,id,nombre,edad,celular):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO personas (id,nombre, edad,celular) VALUES (%s,%s, %s,%s)"
        val = [
            (id,nombre, edad, celular),
        ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()

    def verificardatoserroneos(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT id FROM personas")
        myresult = self.mycursor.fetchall()
        return myresult
    def actualizarpersona(self,edad,celular,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )

        mycursor = mydb.cursor()

        sql = "UPDATE personas SET edad = %s,celular=%s WHERE id = %s"
        val = (edad,celular,id)

        mycursor.execute(sql, val)

        mydb.commit()
    def eliminarpersona(self,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM Personas WHERE id = %s"
        adr = (id,)
        mycursor.execute(sql, adr)

        mydb.commit()

    def agregarproducto(self, id,nombre, fechadecaducacion):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO material (id,nombre, fechadecaducacion) VALUES (%s,%s, %s)"
        val = [
            (id,nombre, fechadecaducacion),
        ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()

    def verificarproductoserroneos(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT id FROM material")
        myresult = self.mycursor.fetchall()
        return myresult
    def actualizarproducto(self,fechadecaducacion,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )

        mycursor = mydb.cursor()

        sql = "UPDATE material SET fechadecaducacion = %s WHERE id = %s"
        val = (fechadecaducacion,id)

        mycursor.execute(sql, val)

        mydb.commit()
    def eliminarproducto(self,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM material WHERE id = %s"
        adr = (id,)
        mycursor.execute(sql, adr)

        mydb.commit()
    def agregarpedidos(self,id, nombre, producto):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO pedidos (id,nombre, producto) VALUES (%s,%s, %s)"
        val = [
            (id,nombre, producto),
        ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()

    def verificarpedidoserroneos(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT id FROM pedidos")
        myresult = self.mycursor.fetchall()
        return myresult
    def actualizarpedido(self,producto,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )

        mycursor = mydb.cursor()

        sql = "UPDATE pedidos SET producto = %s WHERE id = %s"
        val = (producto,id)

        mycursor.execute(sql, val)

        mydb.commit()
    def eliminarpedido(self,id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="Prueba"
        )
        mycursor = mydb.cursor()
        sql = "DELETE FROM pedidos WHERE id = %s"
        adr = (id,)
        mycursor.execute(sql, adr)

        mydb.commit()