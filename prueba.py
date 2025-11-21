from beneficios import tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico

estudiante1 = estudiante(
    nombre="Stefi",
    apellido="Lopez",
    edad=22,
    legajo=1234,
    curso="4to A",
    correo="stefi.lopez@gmail.com",
    password="stefi123",
    id=1
)

estudiante2 = estudiante(
    nombre="Melanie",
    apellido="Martinez",
    edad=21,
    legajo=1235,
    curso="4to A",
    correo="melanie.martinez@gmail.com",
    password="melanie21",
    id=2
)

estudiante3 = estudiante(
    nombre="Juan",
    apellido="Pérez",
    edad=20,
    legajo=1236,
    curso="4to B",
    correo="juan.perez@gmail.com",
    password="juan20",
    id=3
)

estudiante4 = estudiante(
    nombre="Lucía",
    apellido="Gómez",
    edad=23,
    legajo=1237,
    curso="4to C",
    correo="lucia.gomez@gmail.com",
    password="lucia23",
    id=4
)

estudiante5 = estudiante(
    nombre="Tomás",
    apellido="Fernández",
    edad=22,
    legajo=1238,
    curso="4to D",
    correo="tomas.fernandez@gmail.com",
    password="tomas22",
    id=5
)




profesor1 = profesor(nombre="Juan", 
                     apellido="Perez", 
                     edad=40, 
                     especialidad="Matematica", 
                     email="programacionnai@gmail.com ", 
                     password="", 
                     id=1)

tarea1= trabajoPractico(consigna="esto es una consigna de Tarea1", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")



for estudiante in profesor1.estudiantes:
    print(estudiante.nombre)

profesor1.asignarTarea(tarea1)


from beneficios import CambiarFecha

beneficio1 = CambiarFecha()

estudiante1.canjearBeneficio(beneficio1, profesor1)

