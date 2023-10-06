cadenas1 = "Hl Satanas"
cadenas2 = "Bienvenidos Maquinola"

#mayusculas
mayus = cadenas1.upper()

#minusculas
minus = cadenas2.lower()

#primera letra con mayuscula 
primer_letra_con_mayuscula = cadenas1.capitalize()

#busca una cadena en otra cadena ,si no hay coincidencia devuelve -1
busqueda_find = cadenas1.find("l")

#busca una cadena en otra cadena
busqueda_index = cadenas1.index("s")

#sie es numerico devuelve true si no false
es_numerico= cadenas1.isnumeric()

# si es alfa numerico return true si no false
es_alfanumeico = cadenas1.isalpha()

#busca una cadena en otra cadena,devuelve la cantidad de veces que coninsida 
contar_coincidencias = cadenas1.count("a")

# conatrar cuantos cadacteres tiene una cadena
contar_caracteres = len(cadenas1)

#verifica si una cadena COMIENZA con una cadena dada,si es asi devuelve true
empieza_com = cadenas1.startswith("Hl")

#verifica si una cadena TERMINA con una cadena dada,si es asi devuelve true
termina_com = cadenas1.endswith("Hl")
    
#remplaza en valor si es encontrado en la cadena 
remplazar_valor = cadenas1.replace("Hl","hola")

remplace_valor = cadenas2.replace(" ",",")

#separaer cadenas con la cadenas que le demos 
cadena_separada = cadenas1.split(",")

print(empieza_com)
print(cadena_separada[0])

print(cadenas1)