class Cliente:
    def __init__(self):
        self.id=0
        self.usuario_id=0
        self.nombre=""
        self.rfc=""
        self.direccion=""
        self.puntos=0

    def setID(self, id):
        self.id=id

    def getID(self):
        return self.id
    
    def setUsuarioID(self, usuario_id):
        self.usuario_id=usuario_id

    def getUsuarioID(self):
        return self.usuario_id
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getNombre(self):
        return self.nombre
    
    def setRfc(self, rfc):
        self.rfc=rfc

    def getRfc(self):
        return self.rfc
    
    def setDireccion(self, direccion):
        self.direccion=direccion

    def getDireccion(self):
        return self.direccion
    
    def setPuntos(self, puntos):
        self.puntos=puntos

    def getPuntos(self):
        return self.puntos

