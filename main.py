class Motor:
    def __init__(self, numeroRegistro, tipo):
        self.registro = numeroRegistro
        self.tipo = tipo

    def cambiarRegistro(self, nuevoRegistro:int):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo:str):
        tipos_permitidos = ["electrico", "gasolina"]
        if nuevoTipo in tipos_permitidos:
            self.tipo = nuevoTipo

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, nuevoColor:str):
        coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevoColor in coloresPermitidos:
            self.color = nuevoColor
            
class Auto:
    cantidadCreados = "0"
    
    def __init__(self, modelo, precio, asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))
    
    def verificarIdentidad(self):
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return "Las piezas no son originales"
            
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        
        return "Auto original"