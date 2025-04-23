class Articulo:
    def __init__(self):
        self.id = 0
        self.descripcion = ""
        self.precio_unitario = 0.0
        self.precio_venta = 0.0

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    def set_precio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario

    def get_precio_unitario(self):
        return self.precio_unitario

    def set_precio_venta(self, precio_venta):
        self.precio_venta = precio_venta

    def get_precio_venta(self):
        return self.precio_venta

