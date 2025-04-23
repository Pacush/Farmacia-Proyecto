import conexion as con
import proveedor as pro


class dbproveedores:
    def guardarProveedor(self, pro: pro.Proveedor):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO proveedores (proveedor_id, nombre, empresa, telefono) VALUES (%s, %s, %s, %s)"
        self.datos=(pro.get_proveedor_id(),
                    pro.get_nombre(),
                    pro.get_empresa(),
                    pro.get_telefono())
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
    
    def buscarProveedor(self, pro: pro.Proveedor):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = f"SELECT * FROM proveedores WHERE proveedor_id='{pro.get_proveedor_id()}'"
        self.cursor1.execute(self.sql)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = pro
            aux.set_proveedor_id(int(row[0]))
            aux.set_nombre(row[1])
            aux.set_empresa(row[2])
            aux.set_telefono(row[3])
        return aux
    
    def editarProveedor(self, pro: pro.Proveedor):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE proveedores SET nombre = %s, empresa = %s, telefono = %s WHERE proveedor_id = %s"
            valores = (pro.get_nombre(), pro.get_empresa(), pro.get_telefono(), pro.get_proveedor_id())
            
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarProveedor(self, pro_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM proveedores WHERE proveedor_id = %s"
            valores = (pro_id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
