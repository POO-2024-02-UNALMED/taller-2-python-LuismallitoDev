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