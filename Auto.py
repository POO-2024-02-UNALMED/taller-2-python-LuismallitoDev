import Motor
import Asiento
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