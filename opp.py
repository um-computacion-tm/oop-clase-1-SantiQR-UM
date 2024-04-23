#Creamos la clase/modelo:
class Profesor:

    #   Creamos el constructor con el método __init__, self es trabajar consigo mismo, 
    # y los otros son los parámetros que van a recibir.
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email
    
    def dame_tu_nombre(self):
        return self.__nombre__
    
class Alumno:

    def __init__(self, el_nombre):
        self.__nombre__ = el_nombre
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def falta(self):
        self.__inasistencias__ += 1

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"
    
    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta
    
    def es_vegano(self):
        self.__dieta__ = "Vegano"

    def mentoria(self, profesor):
        self.__mentor__ = profesor


#Ahora los objetos:
profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

alumno_juan = Alumno("Juancito")
alumno_maria = Alumno("Maria")


#Código extra:
# profesores = [profe_elio, profe_gabi]

# for profe in profesores:
#     print(profe.__nombre__ + " " + profe.__email__)

#Código:
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.__inasistencias__)
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.__inasistencias__)
print(alumno_juan.esta_libre())

alumno_maria.elegir_dieta_especial("Vegetariana")
print(alumno_maria.__dieta__)
alumno_juan.es_vegano()
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)
alumno_maria.mentoria(profe_gabi)
print(alumno_juan.__mentor__.__nombre__, alumno_maria.__mentor__.__nombre__)


#ipdb for fun:
#import ipdb; ipdb.set_trace()

