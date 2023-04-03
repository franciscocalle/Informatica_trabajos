#!/usr/bin/env python3
import os

file1 = "hola.txt"
file2 = "chau.txt"

os.rename(file1, "temporal")
os.rename(file2, file1)
os.rename("temporal", file2)

# como hacer para  acepte por consola cuales son los archivos q hay q swappear
#usar os.path.exists(path), ver como se usa esto para mejorar el script, lo hago abajo

import sys
file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

with open(file_path1) as f1:
    content_file1 = f1.readlines()
with open (file_path2) as f2:
    content_file2 = f2.readlines()

with open (file_path1, "w") as f1:
    f1.writelines(content_file2)
with open (file_path2, "w") as f2:
    f2.writelines(content_file1)
    

#2
texto_leido = open("un_archivo.txt", "r").read()

texto_para_escribir = texto_leido [0:6]

with open("nuevo_archivo.txt","a") as mi_arch:
    mi_arch.write(texto_para_escribir)