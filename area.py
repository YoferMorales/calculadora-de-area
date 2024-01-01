# crear un programa por sistama de opcion para saber la area de un triangulo, de un rectangulo y de un cuadrado

print(f'''
opciones para escoger la area de una figura
opcion 1 para saber la area de un triagulo
opcion 2 para saber la area de un rectangulo
opcion 3 para saber la area de un cuadrado''')

area = int(input('¿cual es la opcion que escoges?: '))
if (area == 1):
    print('hallar la area de un triangulo')
    base = float(input('¿cual es la base?: '))
    altura = float(input('¿cual es la altura?: '))
    resultado = (base * altura) / 2
    print(f'la area de un triangulo es de {resultado}') 
elif (area == 2):
     print('hallar la area de un rectangulo')
     largo = float(input('¿cual es el largo?: '))
     ancho = float(input('¿cual es el ancho?: '))
     resultado = largo * ancho
     print(f'la area de un rectangulo es de {resultado}') 
elif (area == 3):
     print('hallar la area de un cuadrado')
     lado_1 = float(input('¿cual es el lado 1?: '))
     lado_2 = float(input('¿cual es el lado 2?: '))
     resultado = lado_1 * lado_2
     print(f'la area de un cuadrado es de {resultado}')
else:
    print('esa opcion no pertenece a ninguna de las opciones ya establecidas')

# falta agragar la funcion round para redondiar el resultado en decimales en dos digitos 
