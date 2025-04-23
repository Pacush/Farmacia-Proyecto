class Compra:
    def __init__(self):
        self.folio = 0
        self.fecha = ""
        self.proveedor_id = 0

    # Getter and Setter for folio
    def get_folio(self):
        return self.folio

    def set_folio(self, folio):
        self.folio = folio

    # Getter and Setter for fecha
    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    # Getter and Setter for proveedor_id
    def get_proveedor_id(self):
        return self.proveedor_id

    def set_proveedor_id(self, proveedor_id):
        self.proveedor_id = proveedor_id
