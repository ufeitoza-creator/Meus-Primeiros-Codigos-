a = input('Digite algo: ')
b = input('Digite algo: ')
print('O tipo primitivo desse valor é ' , type(a))
print('O tipo primitivo desse valor é ' , type (b))
print ('só tem espaços?' , a.isspace())
print('só tem números?' , a.isnumeric())
print('é alphanumérico?' , a.isalnum())
print('é alfabético?' , a.isalpha())
print('Está me maiusculas?' , a.isupper())
print('Está em minusculas?' , a.islower())
print('Está capitalizada? ' , a.istitle())
print('É alfanumerico?' , b.isalnum())

# A parte mais chatinha são os termos utilizados da nomeclatura

#Maiusclas = isupper
# Apenas espaços = isspace
# Apenas números = isnumeric
#Apenas alfabeto = isapha
#Alphanumérico = isalnum
#Minusculas = islower
#Capitalizada= istitle

# sempre se atentar nas primeiras linhas com o "type())"
