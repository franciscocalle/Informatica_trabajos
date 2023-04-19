#!/usr/bin/env python3
import os, glob, sys
lista = ["df", "control", "dff"]

#EJERCICIO1
def control_de_lista(lista):
    if "control" in lista:
        lista.remove("control")
        lista.append("revisado")
    return lista

print(control_de_lista(lista))

#2
def eliminar_primer_elemento(lista):
    del lista[0]

#3
def encontrar_posicion(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return None

#4
def mover_elemento(lista1, lista2, elemento):
    # Método 1: Usando el método remove para eliminar el elemento de lista1
    if elemento in lista1:
        lista1.remove(elemento)
        lista2.append(elemento)

    # Método 2: Usando la indexación y la sentencia del para eliminar el elemento de lista1
    if elemento in lista1:
         indice = lista1.index(elemento)
         del lista1[indice]
         lista2.append(elemento)

#5
#EJERCICIO 5
listanumeros = [2,4,7]
def lista_enteros(listanumeros):
     for numero in listanumeros:
          if numero  %2 ==0: 
               index = listanumeros.index(numero)
               listanumeros[index] = True
          else:
               index = listanumeros.index(numero)
               listanumeros[index] = False
         # listanumeros[listanumeros.index(numero)] = (numero % 2 == 0)
     return listanumeros
         
print(lista_enteros(listanumeros))


#EJERCICIO 6: 
string = ("Hola, como estas")
def leer(string):
     dict_result = dict = {}
     for letra in string:
          if letra.isalpha():
               if letra not in dict_result.keys(): 
                    dict_result.update({letra: 1}) 
               else:
                    value = dict_result.get(letra)
                    dict_result.update({letra : value + 1})
     print(dict_result)
     return dict_result
leer(string)

#EJERCICIO 7:
string = ("Hola, como estas")
def leer(string):
     dict_result = dict = {}
     for letra in string:
          if letra.isalpha():
               if letra not in dict_result.keys(): 
                    dict_result.update({letra: 1}) 
               else:
                    value = dict_result.get(letra)
                    dict_result.update({letra : value + 1})
          else:
               dict_result.update({letra: 0})  
     print(dict_result)
     return dict_result
leer(string)

#EJERCICIO 8:
palabra = ["tasat"]
def es_palindromo(palabra):
    if palabra == palabra [::-1]:
     print("Es palindroma")
    else: 
       print ("no es palindroma")

es_palindromo(palabra)