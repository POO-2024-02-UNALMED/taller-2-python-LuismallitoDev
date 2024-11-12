class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, nuevoColor:str):
        coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevoColor in coloresPermitidos:
            self.color = nuevoColor