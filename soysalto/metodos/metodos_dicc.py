diccionario = {
    "name" : "TheBR",
    "lastname" : "Company",
    "luagar":"EEUU"
}

valor_de_k = diccionario.get("k")#get evitar el error y sigue corriendo el codigo

#eliminados un elementos del diccionario
diccionario.pop("name")
print(diccionario)

#obteniendo un dict_items interable
diccionario_iterable = diccionario.items() 


#elimina todos los item de diccionario
# diccionario.clear()



