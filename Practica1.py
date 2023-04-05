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
