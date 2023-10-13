numer = [1,2,3,2,44,5,6]
#ORDENA la lista
# numer.sort()
# print(numer)
#ORDEN INVERSA 'reverse' 
numer2=sorted(numer,reverse=True)
print(numer2)

# clientes = [[3,"Chanchito"],
#             [1,"Felipe"],
#             [5,"Pulga"]
# ]
# clientes.sort()
# print(clientes)

clientes = [["Chanchito",3],
            ["Felipe",1],
            ["Pulga",5]
]
# def ordena(elemento):
#     return elemento[1]

# clientes.sort(key=ordena,reverse=True)
# print(clientes)

# mejor forma de resolver con funcion lambda
clientes.sort(key=lambda el: el[1],reverse=True)# to  invertir add "reverse=True"
print(clientes)