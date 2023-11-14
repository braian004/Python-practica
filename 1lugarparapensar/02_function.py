def suma (a,b):
    result=a+b
    print(result)
    return result

def operaciones(a,b):
    suma = a+b
    multiplicacion = a*b
    resta= a+b
    return suma,multiplicacion,resta
resultado = suma(5,6)
print(resultado)