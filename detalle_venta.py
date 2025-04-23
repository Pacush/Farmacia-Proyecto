class DetalleVenta:
    def __init__(self):
        self.detalle_id = 0
        self.folio = 0
        self.articulo_id = 0
        self.cantidad = 0

    # Getters
    def get_detalle_id(self):
        return self.detalle_id

    def get_folio(self):
        return self.folio

    def get_articulo_id(self):
        return self.articulo_id

    def get_cantidad(self):
        return self.cantidad

    # Setters
    def set_detalle_id(self, detalle_id):
        self.detalle_id = detalle_id

    def set_folio(self, folio):
        self.folio = folio

    def set_articulo_id(self, articulo_id):
        self.articulo_id = articulo_id

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

