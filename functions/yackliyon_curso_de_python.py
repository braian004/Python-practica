# def suma_tres(n):
#     print (n+3)
# suma_tres(4)


# def tabla_de_multiplicar(n):
#     for i in range(10):
#         print(f"2 x {i} = {i*n}")
# tabla_de_multiplicar(2)

# n = 56
# def function():
#     print(n)
#     print(m)
# m = 23
# function()

# def dato():
#     n=2
#     print(n)
# dato()

# j = 567
# dato()
# print(j)

# def suma(a,b):
#     return a+b  
# respuesta = suma(4,6)
# print(respuesta)

'''separa una lista '''
'''pares e inpares'''
ejemplo = [3,7,9,5,3,7,3,12]
# def separador(lista):
#     # lista.short # => para qu este ordenado
#     pares = []
#     inpares = []
#     for i in lista:
#         if i % 2 == 0:
#             pares.append(i)
#         else:
#             inpares.append(i)
#     return pares, inpares
# pares,inpares = separador(ejemplo)
# print(pares)
# print(inpares)






def separar_lista(lista):
    # lista.sort()
    pares = []
    inpares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            inpares.append(i)
    return pares,inpares
pares,inpares = separar_lista(ejemplo)
print(pares)
print(inpares)
