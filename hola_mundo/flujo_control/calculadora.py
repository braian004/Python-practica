welcom = "bienvenidos a la calculadora"
salir = 'para salir escriva salir'
print(welcom)
print(salir)
    
exit = ""
while exit != "exit":
    try:
        numero = float(input("ingresa un numero:"))
    except ValueError:
        print("escrive un numero no una letra pendejo")
        # break repetir de nuevo
        continue #continua de nuevo hasta que cumpla  
    try:
        operacion = input("las operaciones son suma,multi,div y resta:")
    except ValueError :
        print("escrive suma,resta y lo que sigre ")
        continue
    try:
        numero2 = float(input("ingrsa numero siguiente:"))
    except ValueError:
        print("escrive un numero no una letra pendejoooooooo")
        continue

    n1 = numero + numero2
    n2 = numero * numero2
    n3 = numero / numero2
    n4 = numero - numero2
    if operacion == "suma":
        print(n1)
    elif operacion == "multi":
        print(n2)
    elif operacion == "div":
        print(n3)        
    elif operacion == "resta":
        print(n4)
    print(exit)  


# welcome = "Bienvenidos a la calculadora"
# salir = 'Para salir, escriba "exit"'
# print(welcome)
# print(salir)

# exit_command = ""
# while exit_command != "exit":
#     try:
#         numero = float(input("Ingresa un número:"))
#     except ValueError:
#         print("Escribe un número válido.")
#         continue

#     operacion = input("Las operaciones son suma, multi, div y resta:")
    
#     if operacion not in ["suma", "multi", "div", "resta"]:
#         print("Operación no válida.")
#         continue
    
#     try:
#         numero2 = float(input("Ingresa el siguiente número:"))
#     except ValueError:
#         print("Escribe un número válido.")
#         continue

#     if operacion == "suma":
#         resultado = numero + numero2
#     elif operacion == "multi":
#         resultado = numero * numero2
#     elif operacion == "div":
#         if numero2 == 0:
#             print("No puedes dividir por cero.")
#             continue
#         resultado = numero / numero2
#     elif operacion == "resta":
#         resultado = numero - numero2

#     print("Resultado:", resultado)
    
#     exit_command = input('Escribe "exit" para salir o presiona Enter para continuar.')

# print("Calculadora cerrada. Gracias por usarla!")
