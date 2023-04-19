#ej 1
import re 

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]',string))

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

#ej 8
import re
def extraer_numero(string):
    resultado = re.split("\D+", string)
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

def get:substr(string)
return re.findall("[@|&](.*?)[@|&]")

#ej 11
import re

def dos_P(lista)
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())
    
lista 

#con el \W le indicas lo del espacio porque es un caracter no alfanumerico, lo podes hacer tambien con \S
