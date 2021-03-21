"""
5 - Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
Usando funciones.
"""
numEnteros = []

def Rellar_lista():
    try:
        for x in range(10):
            numEnteros.append(int(input('Ingrese un numero: ')))
    except:
        print('Hubo algún error, al ingresar valores.')
        exit()
        
def Separdor(lista_enteros):
    cadena_almacenadora = ''
    
    for x in lista_enteros:
       cadena_almacenadora +='{},'.format(x)
    print(cadena_almacenadora)

Rellar_lista()
Separdor(numEnteros)

