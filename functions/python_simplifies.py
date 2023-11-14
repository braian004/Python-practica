# def about_me(name, proffesion, pet):
#     print("hl my name is", name)
#     print("I am a", proffesion)
#     print("and I have a", pet)

# about_me("Mariya","programer","cat")
# about_me("cristiano","data analyst","dog")
# about_me("pepe","geologo","hive")

# import random
# from sty import fg

# def generateRGB():
#     red = random.randint(0,256)
#     green = random.randint(0,256)
#     blue = random.randint(0,256)
#     return red,green,blue


# def generateColour(red,green,blue):
#     return fg(red,green,blue)
# red,green,blue =generateRGB()
# colour = generateColour(red,green,blue)
# print(colour,"dsdsdfsdfsdfsdfsdfsfsd")

# def repeticion(color):
#     comando = ""
#     while comando != "exit":
#         comando = input("$")
#     return color
# red,green,blue =generateRGB()
# c = repeticion(colour)
# print(c)


# comando = ""
# while comando != "salir":
#     comando = input("$")
#     print(comando) 
           

import random
from sty import fg

def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)

def repeticion():
    comando = ""
    while comando != "exit":
        red, green, blue = generateRGB()
        color = generateColour(red, green, blue)
        comando = input(f"{color}PS ")
    return color

if __name__ == "__main__":# I don't understand
    c = repeticion()
    print(c)


