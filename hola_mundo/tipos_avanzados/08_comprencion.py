clientes = [["Chanchito",3],
            ["Felipe",1],
            ["Pulga",5]
]
# nombres = []
# for clientes in clientes:
#     nombres.append(clientes[0])
# print(nombres)

nombres=[clientes[1] for clientes in clientes]
print(nombres)