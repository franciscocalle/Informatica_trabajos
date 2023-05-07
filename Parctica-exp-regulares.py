#ej 1
import re 

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]',string))  #yo le pondria un + afuera de los [] y sacaria el '.'

#ej 2
import re 

def caracteres_permitidos(string):
    return not bool(re.search('[^a-zA-Z0-9.]',string))

#ej 3a
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
#cuando pone he*, solo se ve si la e esta 0 o mas veces, la h no
#3b
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
                          
#3c
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
# en este caso si pones "heee", te va a dar que si lo encontro porque no aclaramos que despues del patron no haya nada, para q de negativo en ese caso habria que pone "he?^e"

#3d
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
#ej 4
import re 

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "patron encontrado"
    else:
        return "patron no encontrado"
print(palabras_unidas("hola_hola"))

#ej 5
import re

def starts_with_number(string, number):
    pattern = "^" + str(number) + "\d*"
    return bool(re.match(pattern, string))

# Ejemplo de uso
string = "123abc"
number = 1
if starts_with_number(string, number):
    print("El string comienza con el número", number)
else:
    print("El string no comienza con el número", number)

#ej6


#ej 7

def func7(string):
    return re.match('^[a-zA-Z0-9\s]+$', string)
string = "Este string es valido"           #tener cuidado con los acentos, sino no te da
print(func7(string))

#ej 8
import re
def extraer_numero(string):
    resultado = re.split("\d+", string)
    for elemento in resultado:
        print(elemento)

#ej 9
import re

def entre_guiones(string):
    return re.findall(r"-(.*?)-", string)

string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))

#ej 10
import re

def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]")

 
#EJERCICIO 10
string10= "hola @ como estas & bien"
def get_substr(string):
    patron = "[@|&] (.*?) [@|&]"
    return re.findall(patron,string10)

print(get_substr(string10))

#ej 11
import re

def dos_P(lista_strings):
    for elemento in lista_strings:
        resultado = re.match("(P\w*)\s+\w+\s+(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())
print(dos_P(lista_strings))
    
lista_strings = ["Práctica o  Python", "Práctica C++", "Práctica Fortran"] 

#ej 12
import re

texto = "Este_es un: ejemplo con espacios y:guiones_bajos"

nuevo_texto = re.sub("[ _:]+", "|", texto)

print(nuevo_texto)

#ej 13
import re

texto = "Este_es un: ejemplo con espacios y:guiones_bajos"

nuevo_texto = re.sub("[^a-zA-Z0-9]*[^a-zA-Z0-9]([^a-zA-Z0-9]*)", "__", texto, count = 2)

print(nuevo_texto)

#ej 14
texto = "Este_es un: ejemplo con espacios y:guiones_bajos"

nuevo_texto = re.sub("[\s\t]", ";", texto)

print(nuevo_texto)

#ej15
import re 
def mail_correcto(string):
    return bool(re.search('^?\W+[.-_]?\W*@[a-z]+[.][a-z]+[.]?[a-z]?$' ,string))
print(mail_correcto('salva-burgos@gmail.com'))
           

#con el \W le indicas lo del espacio porque es un caracter no alfanumerico, lo podes hacer tambien con \S
