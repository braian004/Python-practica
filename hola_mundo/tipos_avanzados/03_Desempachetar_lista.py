numer = [1,2,2,"e"]
# # # no es bueno FEO!
# first = numer[0]
# Second = numer[1]
# third = numer[2]

first,Second,third,letra = numer
#print(first,Second)
letra, *otros = numer
# print(letra,otros)
numeros = [1,2,3,4,5,6,7,8,9]
primero,ultimo, *otro,ult,ant = numeros
print(ant,primero)