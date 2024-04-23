class Persona:

    # Le pongo un valor por defecto por sí no le mando nada, conviertiéndolos en parámetros opcionales
    def __init__(self, nombre: str = "John", apellido: str = "Doe", du: int = 1234):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du
    
    def __str__(self):
        return(f'''Los datos son: 
    Nombre = {self.__nombre__} 
    Apellido = {self.__apellido__}
    DU = {self.__du__}
    \n''')