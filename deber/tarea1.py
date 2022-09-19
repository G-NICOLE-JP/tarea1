# Realizar una aplicación en Python que permita registrar estudiantes y notas:
#------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------PYTHON-------------------------------------------------------------



listaAlumnos = []
class Alumnos(object):
    def _init_(self, cedula, nombre, apellido, edad, n1, n2, n3):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.notaFinal = (n1 + n2 + n3) / 3
        self.historial = []



    def entregarDatos(self):
        print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.cedula, self.nombre, self.apellido, self.notaFinal))
    def editarNotas(self, n1, n2, n3):
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.notaFinal = (n1 + n2 + n3) / 3
        print("Registro Exitoso!...")
        exit()

    def incluirEvento(self, n1, n2, n3):
        return ("modificacion: Nota_1: {} Nota_2: {} Nota_3: {}".format(n1, n2, n3))
    def entregaHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))




#OPCION NUMERO 1--------------------------------------------------------------------------------------------------------
def registrarAlumnos():
    print("Registro de Alumnos\n")
    cedula = int(input("Ingrese el numero de cedula: "))
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    n1 = float(input("Ingrese la nota 1: "))
    n2 = float(input("Ingrese la nota 2: "))
    n3 = float(input("Ingrese la nota 3: "))
    objAlumno = Alumnos(cedula, nombre, apellido, edad, n1, n2, n3)
    listaAlumnos.append(objAlumno)




#OPCION NUMERO 2--------------------------------------------------------------------------------------------------------
def listadoAlumnos():
    print("Listado de Alumnos\n")
    for objAlumno in listaAlumnos:
        objAlumno.entregarDatos()





#OPCION NUMERO 3--------------------------------------------------------------------------------------------------------
def buscarAlumnos():
    print("Buscar Alumnos\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaAlumnos:
        if cedula == objAlumno.cedula:
            objAlumno.entregarDatos()




#OPCION NUMERO 4--------------------------------------------------------------------------------------------------------
def modificarCalificaciones():
    print("Modificar Calificaciones\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objAlumno in listaAlumnos:
        if cedula == objAlumno.cedula:
            n1 = float(input("Ingrese nota 1: "))
            n2 = float(input("Ingrese nota 2: "))
            n3 = float(input("Ingrese nota 3: "))
            objAlumno.editarNotas(n1, n2, n3)
            objAlumno.entregarDatos()
            recepcionMensaje = objAlumno.incluirEvento(n1, n2, n3)
            objAlumno.historial.append(recepcionMensaje)




#OPCION NUMERO 5--------------------------------------------------------------------------------------------------------
def consultarHistorial():
    print("Consulta de Historial\n")
    cedula = int(input("Ingrese el numero de cedula a consultar: "))
    for objAlumno in listaAlumnos:
        if cedula == objAlumno.cedula:
            for recepcionMensaje in objAlumno.historial:
                print("Evento: {}".format(recepcionMensaje))




#OPCION NUMERO 6 SALIR--------------------------------------------------------------------------------------------------
def salir():
    print("Salida inmediata...!")
    exit()




#MENU PRINCIPAL --------------------------------------------------------------------------------------------------------
def main():
    while True:
        print("\n")
        print("|*******************************************************************************************************************|")
        print("|*|                           _____BIENVENIDOS A REGISTRO DE ESTUDIANTE____      |*|")
        print("|*|                              _-_-_-_-_-_-_-MENU PRINCIPAL_-_-_-_-_-_-_       |*|")
        print("|*******************************************************************************************************************|")
        print("")
        print("Elija una de las siguientes opciones:");
        print("1.- Registrar Alumno")
        print("2.- Mostrar Alumno")
        print("3.- Buscar Alumno")
        print("4.- Modificar calificaciones")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))


        if opcion == 1:
            registrarAlumnos()
        elif opcion == 2:
            listadoAlumnos()
        elif opcion == 3:
            buscarAlumnos()
        elif opcion == 4:
            modificarCalificaciones()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            salir()

if __name__ == '__main__':
    main();