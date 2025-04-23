class Venta:
    def __init__(self):
        self.folio = 0
        self.fecha = ""
        self.cliente_id = 0

    # Getter and Setter for _folio
    def get_folio(self):
        return self.folio

    def set_folio(self, _folio):
        self.folio = _folio

    # Getter and Setter for _fecha
    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    # Getter and Setter for _cliente_id
    def get_cliente_id(self):
        return self.cliente_id

    def set_cliente_id(self, _cliente_id):
        self.cliente_id = _cliente_id

