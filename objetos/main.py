from persona import Persona

if __name__ == '__main__':
    persona0 = Persona()
    
    print(persona0)

    persona1 = Persona("Santiago", "Quiroga", 4321)
    
    #Para mostrarlo con función __str__:
    print(persona1)

    # Para mostrarlo con función específica:
    #persona1.mostrar()

    # Para mostrarlo sin la función:
    # print(persona1.__nombre__, persona1.__apellido__, persona1.__du__)

    # Para mostrarlo como diccionario:
    # print(persona0.__dict__)