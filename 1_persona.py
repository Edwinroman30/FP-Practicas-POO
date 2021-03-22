#1)Crear una clase Persona que tenga como atributos el "cedula,# nombre, apellido y la edad 
# (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad una 
# funcion para mostrar ó imprimir. 

# Crear una segunda clase Profesor que herede de la clase Persona.
# Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. 
# Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. También crear 
# un objeto de la clase Profesor y llamar a sus funciones y propiedades.


class Persona:
    
    def __init__(self,p_cedula,p_nombre,p_edad):
        self.__cedula = p_cedula
        self.__nombre = p_nombre
        self.__edad= p_edad
     
    @property
    def Cedula(self):
         return self.__cedula

    @property
    def Nombre(self):
        return self.__nombre
    
    @property
    def Edad(self):
        return self.__edad 
        
    def Show_inf(self):
        print('Usted {1}, de cedula {0} tiene {2} años de edad.'.format(self.__cedula,self.__nombre,self.__edad))
        
 

Miguel = Persona('402-4448881-4','Miguel Gomez',38)
"""
print(Miguel.Cedula)
print(Miguel.Nombre)
print(Miguel.Edad)
"""
Miguel.Show_inf()


class Profesor(Persona):
    
    def __init__(self,_cedula,p_nombre,p_edad,p_sueldo):
        super().__init__(_cedula,p_nombre,p_edad)
        self.__sueldo = p_sueldo
    
    @property
    def Sueldo(self):
        return self.__sueldo
  
    
    def Show_inf(self):
        super().Show_inf()
        print('Su sueldo es de: ',self.__sueldo)
          
Benito = Profesor('402-4448388-5','Benito Rosarios',40,48000)

"""
print(Benito.Nombre)
print(Benito.Edad)
print(Benito.Cedula)
"""
Benito.Show_inf()

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233        