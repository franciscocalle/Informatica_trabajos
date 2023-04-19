#!/usr/bin/env python3

#1
def siguiente (numero):
    return numero + 1
print(siguiente(3))

#2
def doble (num):
    return num * 2
print(doble(2))

#3
def doble_anterior (numero):
    return (numero - 1) * 2
print(doble_anterior(5))

#4
def retirar_dinero(saldo, monto):
    return max(saldo - monto, 0)
print(retirar_dinero(98,80))

#5
def dia_de_la_semana_favorito(dia):
    return dia == "Sábado"

#6
def esta_en_rango(longitud_onda):
    return 223.0 <= longitud_onda <= 586.8

#7
def esta_en_rango(longitud_onda):
    return 223.0 <= longitud_onda <= 586.8 and longitud_onda != 314.5

#8
def tiene_descuento(edad):
    return (edad <= 12) or (edad >= 60)



#Ejercicio 9
def funcion_xor(a,b):
    if a == "V" and b == "V" or a == "F" and b == "F":
        return "F"
    else:
        return "V"
print (funcion_xor("V","V"))
print (funcion_xor("V","F"))
print (funcion_xor("F","V"))
print (funcion_xor("F","F"))


#Ejercicio 10
def saludar_persona(nombre, apellido):
    resultado_10 = nombre + " " + apellido
    return "Buenas tardes " + resultado_10
print (saludar_persona("matias","cadena"))


#Ejercicio 11
def largo_de_palabra_si_empieza_con_h (palabra):
    if palabra[0] == "H":
        return len(palabra) 
    else:
        return "la palabra no empieza con H"
print (largo_de_palabra_si_empieza_con_h ("Holis"))
print (largo_de_palabra_si_empieza_con_h ("buenas"))

#Ej 11.2 (otra forma de hacerlo)
def largo_de_palabra_si_empieza_con_h (palabra):
    return len(palabra) if palabra.startswith("H") else False
print (largo_de_palabra_si_empieza_con_h ("Holis"))
print (largo_de_palabra_si_empieza_con_h ("buenas"))


#Ejercicio 12
def empieza_con_buenos(palabra):
    return palabra.startswith ("Buenos") or palabra.startswith ("Buenos")
print(empieza_con_buenos("Buenos días"))
print(empieza_con_buenos("Hola"))


#Ejercicio 13
def es_multiplo(numero_1,numero_2):
    return numero_2 % numero_1 == 0
print (es_multiplo(3,108))


#14
def numero_par_impar_cero (numero1):
    if numero1  == 0:
        return "cero"
    elif numero1 % 2 == 0:
        return "par"
    else: 
        return "impar"
print (numero_par_impar_cero(0))
#15
def contar_letras_a(frase):
    contador = 0
    for letra in frase:
        if letra == 'a' or letra == 'A':
            contador += 1
    return contador
print (contar_letras_a("holaA"))

#16
def meses_subsistir (plata):
    gasto = 60000
    return  plata / gasto 
print(meses_subsistir(120000))
