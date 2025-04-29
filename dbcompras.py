import compra as com
import conexion as con
import detalle_compra as det_com


class dbcompras:
    def guardarCompra(self, com: com.Compra):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO compras (folio, fecha, proveedor_id) VALUES (%s, %s, %s)"
        self.datos=(com.get_folio(),
                    com.get_fecha(),
                    com.get_proveedor_id())
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
    
    def buscarCompra(self, com: com.Compra, usrLogged: list = []):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "SELECT * FROM compras WHERE folio=%s"
        self.datos=(com.get_folio(), )
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = com
            aux.set_folio(int(row[0]))
            aux.set_fecha(row[1])
            aux.set_proveedor_id(int(row[2]))
        return aux
    
    def editarCompra(self, com: com.Compra):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE compras SET fecha = %s, proveedor_id = %s WHERE folio = %s"
            valores = (com.get_fecha(), com.get_proveedor_id(), com.get_folio())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarCompra(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM compras WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def guardarDetalleCompra(self, detalle_compra: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO det_compra (det_id, folio, cantidad, articulo_id) VALUES (%s, %s, %s, %s)"
        self.datos=(detalle_compra[0],
                    detalle_compra[1],
                    detalle_compra[2],
                    detalle_compra[3])
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
        
    def detallesCom(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT * FROM det_compra WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False
        
    def eliminarDetalleCompra(self, detalle_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM det_compra WHERE det_id = %s"
            valores = (detalle_id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False