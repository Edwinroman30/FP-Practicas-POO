"""
2 - Crear una clase Contacto. Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion".
También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos. 
También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos. Crear también una
clase llamada ProbarContacto. Esta clase deberá contener sólo la función principal, que creará dos objetos de tipo 
Contacto, les asignará los datos del contacto y les pedirá que saluden.
"""

class Contacto:
    
    def __init__(self,p_nombre,p_apellidos,p_telefono,p_direccion):
        self.__nombre = p_nombre
        self.__apellidos = p_apellidos
        self.__telefono = p_telefono
        self.__direccion = p_direccion
    
    #* GET
    @property
    def Nombre(self):
        return self.__nombre
    @property
    def Apellido(self):
        return self.__apellidos
    @property
    def Telefono(self):
        return self.__telefono
    @property
    def Direccion(self):
        return self.__direccion
        
    #* SET    
    @Nombre.setter
    def Nombre(self,nombre):
        if(nombre == ''):
             pass
        else:
            self.__nombre = nombre       
    
    @Apellido.setter
    def Apellido(self,apellido):
        if(apellido == ''):
            pass
        else:
            self.__apellidos = apellido

    @Telefono.setter
    def Telefeno(self,telefono):
        if(telefono == '' or len(telefono)>12):
            pass
        else:
            self.__telefono = telefono

    @Direccion.setter
    def Direccion(self,direccion):
        if(direccion == '' or len(direccion)>45):
            pass
        else:
           self.__direccion = direccion
    
    def Saludar(self):
        print('Hola, soy {} {} me gusta hacer amigos/as. Por eso toma mi Whatsapp: {} y resido en "{}" por si quieren visitarme.'.format(self.Nombre,self.Apellido,self.Telefeno,self.Direccion))
        
    
"""
p1 = Contacto('Pablo','Martinez','8092334811','Calle e tres brazos')
p1.Nombre = 'Fran'
#print(p1.Nombre)
p1.Saludar()
"""

class ProbarContacto:
    
    def __init__(self):
        self.__contacs = []       
    
    def FuncionPrincipal(self):
        i = 0
        while(i<2):
           self.__contacs.append(Contacto(input('Type your name: '),input('Type your lastname: '),input('Type your phoneNumber: '),input('Type your AD: ')))
           i= i+1
           print('')
            
        for item in self.__contacs:
            item.Saludar()
            
test = ProbarContacto()
test.FuncionPrincipal()

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233