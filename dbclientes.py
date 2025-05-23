import cliente as cli
import conexion as con


class dbclientes:
    def guardarCliente(self, cli: cli.Cliente):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "insert into clientes (cliente_id, usuario_id, nombre, rfc, direccion, puntos) values (%s, %s, %s, %s, %s)"
        self.datos=(cli.getID(),
                    cli.getUsuarioID(),
                    cli.getNombre(),
                    cli.getRfc(),
                    cli.getDireccion(),
                    0)
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()

    def maxSQL(self, columna: str, tabla: str):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = f"SELECT MAX({columna}) FROM {tabla}"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.con.close()
        return row
    
    def buscarCliente(self, cli: cli.Cliente, usrLogged: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        if usrLogged[1] == "Administrador":
            self.sql = "select * from clientes where cliente_id=%s"
            self.datos=(cli.getID(),)
        else:
            self.sql = "select * from clientes where cliente_id=%s"
            self.datos=(cli.getID())
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = cli
            aux.setID(int(row[0]))
            aux.setUsuarioID(int(row[4]))
            aux.setNombre(row[1])
            aux.setRfc(row[2])
            aux.setDireccion(row[3])
        return aux
    
    def editarCliente(self, cli: cli.Cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE clientes SET nombre = %s, rfc = %s, direccion = %s WHERE cliente_id = %s"
            valores = (cli.getNombre(), cli.getRfc(), cli.getDireccion(), cli.getID())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarCliente(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM clientes WHERE cliente_id = %s"
            valores = (id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def dictClientesId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT nombre, cliente_id FROM clientes"
            self.cursor1.execute(self.sql)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False

    def rfcsClientes(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT rfc nombre FROM clientes"
            #valores = (usrLoggedId,)
            self.cursor1.execute(self.sql)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return []
        
    def getPuntos(self, cliente_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT puntos FROM clientes WHERE cliente_id = %s"
            valores = (cliente_id,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return []
        
    def actualizarPuntos(self, cliente_id: int, nuevos_puntos: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE clientes SET puntos = %s WHERE cliente_id = %s"
            valores = (nuevos_puntos, cliente_id)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
        except Exception as e:
            print(e)
        
db = dbclientes()

db.actualizarPuntos(1, 10)