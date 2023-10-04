'''
reglas genrales de la funcion :
1- no se ejcuta la funcion a menos que la llames
2- la puedo llamar la cantidad de veces que kiera
3- primero ahi que definir la funcion y luego llamarla
'''
# FUNCION SIN PARAMETROS
'''
def mifuntion():
    conjunto de intrucciones
'''
def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")
# derechos_humanos()

def derecho_mayorDeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")


# FUNCTIONS WITH PARAMETERS
'''
def miFuntion2(parametro1,parametro2):
    # conjunto de instrucciones
'''

def mayoria_de_edad(nombre,edad):
    if edad >= 18:
        derechos_humanos()
        derecho_mayorDeEdad()
    else:
        derechos_humanos()

mayoria_de_edad("Pepito",12)
mayoria_de_edad("Rosa",2)
mayoria_de_edad("Juan",10)
mayoria_de_edad(edad=5,nombre='Mayoria')

''''
def mifuncion3(parmaetro1,parametro2=valorpordefecto)
'''
def mayoria_de_edad2(edad,nombre="DESCONOCIDO"):
    print(f'Segun la edad de {nombre},sus derechos son:')
    if edad >=18:
        derechos_humanos()
        derecho_mayorDeEdad()
    else:
        derechos_humanos()
mayoria_de_edad2(15,'Pepito')