#Es buena práctica en python tener una función que vaya a 
# correr el programa desde el principio.

#Siempre hay que dejar dos espacios de por medio entre funcion o
#entry point, es buena práctica


def palindromo(palabra):
    #Primero se le quitan los espacios a la palabra ingresada
    palabra = palabra.replace(' ', '')
    #Se convierten todas las letras en minúsculas
    palabra = palabra.lower()
    #Se genera la palabra invertida a partir de la palabra original con
    #el método de slice
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

#El punto de entrada de un archivo de python
if __name__ == '__main__':
    run()