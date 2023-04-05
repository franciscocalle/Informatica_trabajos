#!/usr/bin/env python3

def tiene_descuento(edad):
    return (edad <= 12) or (edad >= 60)
print(tiene_descuento(22))