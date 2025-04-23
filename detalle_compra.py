class DetalleCompra:
    def __init__(self):
        self.det_id = 0
        self.folio = 0
        self.cantidad = 0
        self.articulo_id = 0

    # Getter and Setter for det_id
    def get_det_id(self):
        return self.det_id

    def set_det_id(self, det_id):
        self.det_id = det_id

    # Getter and Setter for folio
    def get_folio(self):
        return self.folio

    def set_folio(self, folio):
        self.folio = folio

    # Getter and Setter for cantidad
    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Getter and Setter for articulo_id
    def get_articulo_id(self):
        return self.articulo_id

    def set_articulo_id(self, articulo_id):
        self.articulo_id = articulo_id