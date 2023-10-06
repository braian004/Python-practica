thislist = ["apple", "banana", "cherry"]
lista =list(("hl",2,3,True))#usando contructor
lista2 = [3,"lista",True,2] 
#devuelve la cantidad de elementos de una lista 
cantidad_elementos = len(lista)

#AGREGAR agrega un elemento en el ultimo index a la lista
lista.append("as")

#AGREGAR un elemento a la lista en un indice especifico 
lista2.insert(0,"Tom")
# CAHNGE the second item
thislist[1] = "blackcurrant"

# AGREGA VARIOS item in the list
lista.extend([False,2030])

#DELETE item the list por su index
lista.pop(-1)#eliminar el ultimo  elemento

#DELETE por su valor
lista.remove("hl")

#eliminar todos los elementos de la lista
# lista.clear

#SORT ordena la lista de forma ascendente a descendente
lista.sort

#invirtiendo los elementos de la lista
lista.reverse()

print (dir(lista))#ver lo que se puede aser con lista