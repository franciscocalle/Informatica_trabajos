#ej tipo parcial de manejo de archivos
#definir un procedimeinto q lea los atchivos txt q esten la carpeta marzo y copie la primera linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
import os, glob
#pasos: 1- movemos a marzo 2- extraemos los .txt 3- leemos las primeras primeras_lineas 4- hacemos carpeta de salida 5- hacer archivo 6- poner lineas en archivo nuevo

def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())
    os.chdir("../../")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open(salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")