import articulo as art
import conexion as con
import detalle_articulo as det_art


class dbarticulos:
    def guardarArticulo(self, art: art.Articulo):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO articulos (articulo_id, descripcion, precio_unitario, precio_venta) VALUES (%s, %s, %s, %s)"
        self.datos=(art.get_id(),
                    art.get_descripcion(),
                    art.get_precio_unitario(),
                    art.get_precio_venta())
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
    
    def buscarArticulo(self, art: art.Articulo, usrLogged: list = []):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "SELECT * FROM articulos WHERE articulo_id=%s"
        self.datos=(art.get_id(), )
        self.cursor1.execute(self.sql, self.datos)
        aux = None
        row = self.cursor1.fetchone()
        if row is not None:
            aux = art
            aux.set_id(int(row[0]))
            aux.set_descripcion(row[1])
            aux.set_precio_unitario(int(row[2]))
            aux.set_precio_venta(int(row[3]))
        return aux
    
    def editarArticulo(self, art: art.Articulo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE articulos SET descripcion = %s, precio_unitario = %s, precio_venta = %s WHERE articulo_id = %s"
            valores = (art.get_descripcion(), art.get_precio_unitario(), art.get_precio_venta(), art.get_id())
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def eliminarArticulo(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM articulos WHERE articulo_id = %s"
            valores = (id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def dictArtIDs(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT descripcion, articulo_id FROM articulos"
            self.cursor1.execute(self.sql)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False
        
    def dictArtIDsFromProveedor(self, id_proveedor: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT a.descripcion, a.articulo_id FROM articulos a JOIN det_articulo d ON a.articulo_id = d.articulo_id WHERE d.proveedor_id = %s"
            valores = (id_proveedor, )
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False

    def actualizarCantArticulo(self, proovedor_id: int, articulo_id: int, nuevaCantidad: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE det_articulo SET existencia = %s WHERE proveedor_id = %s AND articulo_id = %s;"
            valores = (nuevaCantidad, proovedor_id, articulo_id)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def actualizarCantArticulo2(self, proovedor_id: int, articulo_id: int, nuevaCantidad: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "UPDATE articulos SET existencia = %s WHERE articulo_id = %s;"
            valores = (nuevaCantidad, articulo_id)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            self.con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def getCantidadArticulo(self, articulo_id: int, proovedor_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT existencia FROM det_articulo WHERE articulo_id = %s AND proveedor_id = %s;"
            valores = (articulo_id, proovedor_id)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchone()
            return rows
    
        except Exception as e:
            print(e)
            return False
    
    def guardarDetalleArticulo(self, detalle_articulo: list):
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "INSERT INTO det_articulo (det_id, proveedor_id, articulo_id, existencia) VALUES (%s, %s, %s, %s)"
        self.datos=(detalle_articulo[0],
                    detalle_articulo[1],
                    detalle_articulo[2],
                    detalle_articulo[3])
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
        
    def detallesArt(self, id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT * FROM det_articulo WHERE articulo_id = %s"
            valores = (id,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False
        
    def getPrecioVenta(self, art_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "SELECT precio_venta FROM articulos WHERE articulo_id = %s"
            valores = (art_id,)
            self.cursor1.execute(self.sql, valores)
            rows = self.cursor1.fetchall()
            return rows
        except Exception as e:
            print(e)
            return False
        
    def eliminarDetalleArticulo(self, detalle_id: int):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            self.sql = "DELETE FROM det_articulo WHERE det_id = %s"
            valores = (detalle_id,)
            self.cursor1.execute(self.sql, valores)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
db = dbarticulos()

print(int(db.getCantidadArticulo(1, 1)[0]))