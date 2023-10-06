#Programa unatabla de multiplicar de cuaker numero entero del 0 al 12
# def tablaMultiplicar(num1,num2):
#     multiplicar = str(num1)+"x"+str(num2)+"="+str(num1*num2)
#     i = str(input("write the number the 1 al 12"))
#     for multiplicar in range(13):
        

#         return multiplicar
# resultado =tablaMultiplicar(3,4)
# print(resultado)

def tablaMultiplicar(num):
    for i in range(1, 13):
        resultado = num * i
        print(str(num) + " x " + str(i) + " = " + str(resultado))
num = int(input("Escribe un número del 1 al 12: "))
tablaMultiplicar(num)
# num = int(input("Escribe un número del 1 al 12: "))
# for i in range(1, 13):
#     resultado = num * i
#     print(str(num) + " x " + str(i) + " = " + str(resultado))



# while comando != "salir":
#     comando = input("$")
#     for i in range(1, 13):
#         resultado = comando * i
#         print(str(comando) + " x " + str(i) + " = " + str(resultado))
  