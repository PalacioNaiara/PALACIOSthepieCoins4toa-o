from tareas import trabajoPractico
from mailAutomation import EmailSender

class usuario():
    def __init__(self,id,nombre,apellido,password,email,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.email = email
        self.edad = edad

class profesor(usuario):
    def __init__(self,id,nombre,apellido,password,email,edad,especialidad):
        super().__init__(id,nombre,apellido,password,email,edad)
        self.especialidad = especialidad
        self.estudiantes= []

    def asignarTarea(self,tarea):
        for estudiante in self.estudiantes:
            email=EmailSender(self.mail, self.password)
            email.enviar_mail(destinatario=estudiante.email, 
                          asunto=tarea.descripcion,
                          mensaje=f"hola {estudiante.nombre}, se te asigno {tarea.consigna}, que tendra la siguiente consigna {tarea.consigna}")
        estudiante.tareas.append(tarea)

    def chequearEntrega(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                print(f"La tarea '{t.descripcion}' ha sido marcada como entregada: {t.entrega}")



    def aprobarTarea(self,estudiante,tarea):
        for t in estudiante.tareas:
            if t == tarea:
                estudiante.coins=tarea.valor
                t.aprobado=True
            print(f"El estudiante {estudiante.nombre} posee {estudiante.coins} mondedas")



def verBeneficiosDeEstudiantes(self): #defini una funcion para q el profesor pueda ver todos los beneficos que fueron canjeados por cada uno de los estudiantes

    print("Beneficios canjeados por los estudiantes") #muestra  en pantalla un tipo titulo para saber d q trata

    for estudiante in self.estudiantes:  #el for recorre la lista  "estudiantes" uno por uno que tiene el profesor
        print(f"Estudiante: {estudiante.nombre}") # se imprime el nombre del estudiante actual 
      
        if not estudiante.beneficios_canjeados: #esta condición pregunta si la lista beneficios_canjeados esta vacia, y si si esta vacia esq el estudiante no canjeo nada
            print("No canjeó ningún beneficio.") #si eso pasa, se imprime eso

        else: #esto se ejecuta si la lista no esta vacia, osea si el estudiante si canjeo beneficios
                
          for b in estudiante.beneficios_canjeados: #el for recorre tdos los beneficios que ese estudiante canjeo, cada elemento "b" es un beneicio x ej cambiarFecha,tutorias,etc
            print(f"{b.nombre} ({b.costo})") #esto te muestra en pantalla el nombre del beneficio (b.nombre) y el costo osea el valor (b.costo)







        
class estudiante(usuario):
    def __init__(self,id,nombre,apellido,password,correo,edad,curso,legajo,profesor,coins=0):
        super().__init__(id,nombre,apellido,password,correo,edad)
        self.curso = curso
        self.legajo = legajo
        self.coins = coins
        self.tareas = []
        self.beneficios_canjeados = []   #esto es la lista donde guardo todos los beneficios que el estudiante haya usado
        profesor.estudiantes.append(self)

    def entregarTarea(self,tarea):
        for t in self.tareas:
            if t == tarea:
                t.entrega = True

    def checkearTareas(self): #Define el método que sirve para revisar las tareas del estudiante
        if not self.tareas: #Si la lista de tareas del estudiante está vacía, osea no tiene tareas asignadas
            print(f"{self.nombre} no tiene tareas asignadas.") #muestra un mensaje avisando que no tiene ninguna tarea
        else: #Si sí tiene tareas, entonces va a else
            print(f"Tareas de {self.nombre}:") #Muestra en pantalla un título con el nombre del estudiante
            for tarea in self.tareas: #Recorre una por una todas las tareas que el estudiante tiene en su lista
                estado = "Aprobada" if tarea.aprobado else ("Entregada" if tarea.entrega else "Pendiente ") #Esta línea decide qué texto mostrar según el estado de la tarea:
                #Si está aprobada muestra: Aprobada
                #Si está entregada pero no aprobada muestra: Entregada
                #Si todavía no fue entregada muestra: Pendiente
                print(f"{tarea.descripcion}: {estado}") #Muestra en pantalla el nombre de la tarea y el estado actual si es pendiente, entregada o aprobada
 



def canjearBeneficio(self, beneficio, profesor): #define el metodo canjear beneficios para canjear beneficios por coins 
  
    if self.coins >= beneficio.costo: #esto revisa si el estudiamnte (self) tiene suficientes monedas. para canjear beneficios. Te dice que SI el estudiante tiene la MISMA cantidad de monedas o MÁS  de las que cuesta el beneficio, entra al if
    
        self.coins -= beneficio.costo  #acá llegamos solo si cumple la condición del if, esta línea le resta al estudiante las monedas que gastó. Self.coins -= beneficio.costo es lo mismo que= self.coins = self.coins - beneficio.costo.  Osea se descuentan las monedas.  
        
        print(f"{self.nombre} canjeó el beneficio '{beneficio.nombre}'") #esto muestra en pantalla dice que el nombre del estudiante y qué beneficio canjeó  "{beneficio.nombre}" se pone  el nombre  del beneficio

        self.beneficios_canjeados.append(beneficio)  #esto cd que se hace un canje con los coins guarda el beneficio en la lista del estudiante con el metodo append 

        #se le manda un email automatico al profesor
        profesor.enviarMail(  #se llama al método enviarMail del profesor (no me funciono)
            destinatario=profesor.email,  #destinatario quién recibe el email (el correo del profe)
            asunto="beneficio canjeado",   #asunto → el título del mail
            mensaje=f"El estudiante {self.nombre} canjeó '{beneficio.nombre}'." #MLo que dice el correo,indicando qel nomnbre del estudiante  quecanjeó qué beneficio. Esto sirve para avisarle al profe cada vez que un alumno usa monedas
        )

    else: #esto se ejecuta solo cuando no se cumple el IF de arribaa
        print(" No tenés suficientes monedas para este beneficio.") #muestra en pantalla que no tenes suficientes monedas para canjear x beneficio



