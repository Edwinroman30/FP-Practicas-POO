"""
4 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro 
en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

lista1 = ['23',10,22,'Edwin0','15/105',';)']
lista2 = ['Edwin','15/15',';)']


def superposicion(lista1,lista2): 
  
  for list1 in lista1:
        
    for list2 in lista2:
            
        if(list1 == list2):
            return True
        
  return False

print(superposicion(lista1,lista2))

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233