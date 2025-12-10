from beneficios import Tutorias, puntosExtra, cambiarFecha
from usuario import profesor, estudiante
from tareas import trabajoPractico

profesor1 = profesor(nombre="Juan", 
                     apellido="Perez", 
                     edad=40, 
                     especialidad="Matematica", 
                     email="programacionnai@gmail.com ", 
                     password="", 
                     id=1)

estudiante1 = estudiante(
    id=1,
    nombre="Stefi",
    apellido="Lopez",
    password="stefi123",
    correo="stefi.lopez@gmail.com",
    edad=22,
    curso="4to A",
    legajo=1234,
    profesor=profesor1 
)

estudiante2 = estudiante(
    id=2,
    nombre="Melanie",
    apellido="Martinez",
    password="melanie21",
    correo="melanie.martinez@gmail.com",
    edad=21,
    curso="4to A",
    legajo=1235,
    profesor=profesor1
)

estudiante3 = estudiante(
    id=3,
    nombre="Juan",
    apellido="Pérez",
    password="juan20",
    correo="juan.perez@gmail.com",
    edad=20,
    curso="4to B",
    legajo=1236,
    profesor=profesor1
)

estudiante4 = estudiante(
    id=4,
    nombre="Lucía",
    apellido="Gómez",
    password="lucia23",
    correo="lucia.gomez@gmail.com",
    edad=23,
    curso="4to C",
    legajo=1237,
    profesor=profesor1
)

estudiante5 = estudiante(
    id=5,
    nombre="Tomás",
    apellido="Fernández",
    password="tomas22",
    correo="tomas.fernandez@gmail.com",
    edad=22,
    curso="4to D",
    legajo=1238,
    profesor=profesor1
)





tarea1= trabajoPractico(consigna="esto es una consigna de Tarea1", 
                        fechaEntrega="12/10/2025", 
                        criterioEvaluacion="Hacer el trabajo Práctico")



for estudiante in profesor1.estudiantes:
    print(estudiante.nombre)

profesor1.asignarTarea(tarea1)


from beneficios import CambiarFecha

beneficio1 = CambiarFecha()

estudiante1.canjearBeneficio(beneficio1, profesor1)



