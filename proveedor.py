class Proveedor:
    def __init__(self):
        self.proveedor_id = 0
        self.nombre = ""
        self.empresa = ""
        self.telefono = ""

    # Getters
    def get_proveedor_id(self):
        return self.proveedor_id

    def get_nombre(self):
        return self.nombre

    def get_empresa(self):
        return self.empresa

    def get_telefono(self):
        return self.telefono

    # Setters
    def set_proveedor_id(self, proveedor_id):
        self.proveedor_id = proveedor_id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_empresa(self, empresa):
        self.empresa = empresa

    def set_telefono(self, telefono):
        self.telefono = telefono