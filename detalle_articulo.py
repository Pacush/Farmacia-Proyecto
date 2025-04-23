class DetalleArticulo:
    def __init__(self):
        self.det_id = 0
        self.proveedor_id = 0
        self.articulo_id = 0
        self.existencia = 0

    # Getter and Setter for det_id
    def get_det_id(self):
        return self.det_id

    def set_det_id(self, det_id):
        self.det_id = det_id

    # Getter and Setter for proveedor_id
    def get_proveedor_id(self):
        return self.proveedor_id

    def set_proveedor_id(self, proveedor_id):
        self.proveedor_id = proveedor_id

    # Getter and Setter for articulo_id
    def get_articulo_id(self):
        return self.articulo_id

    def set_articulo_id(self, articulo_id):
        self.articulo_id = articulo_id

    # Getter and Setter for existencia
    def get_existencia(self):
        return self.existencia

    def set_existencia(self, existencia):
        self.existencia = existencia
