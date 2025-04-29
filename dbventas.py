import conexion as con
import detalle_venta as det_ven
import venta as ven


class dbventas:
    def guardarVenta(self, ven: ven.Venta):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO ventas (folio, fecha, cliente_id) VALUES (%s, %s, %s)"
        self.datos=(ven.get_folio(),
                    ven.get_fecha(),
                    ven.get_cliente_id())
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
    
    def buscarVenta(self, ven: ven.Venta, usrLogged: list = []):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "SELECT * FROM ventas WHERE folio=%s"
        self.datos=(ven.get_folio(), )
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = ven
            aux.set_folio(int(row[0]))
            aux.set_fecha(row[1])
            aux.set_cliente_id(int(row[2]))
        return aux
    
    def editarVenta(self, ven: ven.Venta):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE ventas SET fecha = %s, cliente_id = %s WHERE folio = %s"
            valores = (ven.get_fecha(), ven.get_cliente_id(), ven.get_folio())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarVenta(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM ventas WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def guardarDetalleVenta(self, detalle_venta: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO det_venta (det_id, folio, articulo_id, cantidad) VALUES (%s, %s, %s, %s)"
        self.datos = (detalle_venta[0],
                      detalle_venta[1],
                      detalle_venta[3],
                      detalle_venta[2])
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
        
    def detallesVenta(self, folio: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT * FROM det_venta WHERE folio = %s"
            valores = (folio,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False
        
    def eliminarDetalleVenta(self, detalle_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM det_venta WHERE det_id = %s"
            valores = (detalle_id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False