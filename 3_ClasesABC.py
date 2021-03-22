"""
Crear tres clases ClaseA, ClaseB, ClaseC que ClaseB herede de ClaseA y ClaseC herede de ClaseB.
Definir un constructor a cada clase que muestre un mensaje. Luego definir un objeto de la clase ClaseC.
"""

class ClaseA:
    def __init__(self):
        print('Hola, te saludo desde la Clase A')
        
class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        print('Hola, te saludo desde la Clase B')
        
class ClaseC(ClaseB):
    def __init__(self):
        super().__init__()
        print('Hola, te saludo desde la Clase C')
        

Obj = ClaseC()

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233