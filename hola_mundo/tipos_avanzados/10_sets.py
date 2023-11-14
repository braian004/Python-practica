#significa grupo o conjunto
primer = {1,2,3,4,5,6,7}#set
# primer.add(12)
# print(primer)
# primer.remove(1)
# print(primer)

segundo = [3,4,5]#list
segundoset = set(segundo)
# print(segundoset)
segundoset.add(8)
print(segundoset)


# print(primer | segundoset)#UNION
# print(primer & segundoset)# INTERSECCION
# print(segundoset-primer)#DIFERENCIA
# print(primer^segundoset)#DIFERENCIA SIMETRICA (elimina los duplicados)



if 33 in segundoset:
    print("thas")
else:
    print("no this")
