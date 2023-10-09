import math
from random import randint

def raizCuadrada(numero):
    resultado = math.sqrt(numero)
    return print("La raiz cuadrada de",numero,"es",resultado )

def numeroAleatorio(a,b):
    resultado = randint(a,b)
    return print("El numero aleatoria es",resultado)