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