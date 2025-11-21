class Beneficio: #cree una clase llamada beneficio, defino que nombre y costo lo van a tener todas las clases que se hereden de esta
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

class CambiarFecha(Beneficio): #cree una clase de cambiarfecha y hereda de beneficios
    def __init__(self):
        nombre="Cambio de fecha de entrega de tarea"
        costo=100
        super().__init__(nombre=nombre,costo=costo ) #super()._init_ recorre los atributos de la clase padre, y t dice q el nombre es"cambio de fecha de entrega" y su costo de coins es de 100

class PuntosExtra(Beneficio):
    def __init__(self):
        nombre="Puntos extras de evaluacion"
        costo=150
        super().__init__(nombre=nombre, costo=costo)

class Tutorias(Beneficio):
    def __init__(self):
         nombre="Faltar a tutorias"
         costo=200
         super().__init__(nombre=nombre, costo=costo)
