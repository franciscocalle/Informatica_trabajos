#!/usr/bin/env python3

#1a
import re

def entreX_Y(string):
    return re.findall("X(.*?ab.*?)Y", string)

string= "XbaaaYjXababYqXbabbbaaYqXfeY"
print(entreX_Y(string))

#1b
#a- verdadero. pq la funcion deberia tener un parametro (de lo q escribio onomaitpipoh). ademas tiene q estar tod en minuscula y con _. los nombres tienen que ser expresivos, expresar lo que hacen no hay que ponerle funcion_algo
#b- verdadero. pq findall esta mal escrito. si lo corregiamos tiraba un type error
#c 
#d-corregida: def entre_ag_cta_sin_numeros(string):
#                   return re.findall("^ag([^\d]*)cta",string)
#tiene que devolver ['gaaa']

#2
import glob, re
def filtrar(archivo):
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as arch:
        for archivo in lista_txt:
            with open(archivo, "r") as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall("[\w]+[-_\.]*[\w]+@gmail.com", texto)
                for email in lista:
                    arch.write(email + "\n")


#4a
# class Pacman:
#     def __init__(self, vidas, puntos, una_velocidad):
#         self.vidas = 3
#         self.puntos = 0
#         self.velocidad =  una_velocidad

#     def comer_bolitas(self, bolitas):
#         self.puntos += bolitas
#         self.velocidad += bolitas

#     def comer_fantasma_rosa(self):
#         self.puntos += 8
#         self.velocidad += 8 * 0,1

#     def comer_fantasma_verde(self):
#         self.puntos += 6
#         self.velocidad += 6  * 0,1

#     def comer_fantasma_naranja(self):
#         self.puntos += 4
#         self.velocidad += 4  * 0,1

#     def comer_fantasma_rojo(self):
#         self.puntos += 2
#         self.velocidad += 2  * 0,1

#     def toca_fantasma(self):
#         self.vidas -= 1

#     def toca_fantasma_aterrador(self):
#         self.vidas -= 2
    
#     def vida_extra(self):


#     def fin_del_juego(self):
#         if self.vidas == 0:
#             return "fin del juego"

# class Fantasma:
#     def __init__(self, un_color):
#         self.color = un_color

# pacman = Pacman(3 ,4, 2)

# print("vidasinicio", pacman.vidas)
# pacman.toca_fantasma()
# print(pacman.vidas)
# print("puntos inicio", pacman.puntos)
# pacman.comer_fantasma_rosa()
# print("puntos desp rosa", pacman.puntos)
# pacman.toca_fantasma_aterrador()

#Consigna 4

class PacMan:
    def _init_ (self, puntos, vidas, velocidad):
        self.puntos = 0
        self.vidas = 3
        #self.velocidad = velocidad     ponerlo como atributo es opcional

    def comer_bolitas(self, bolitas):
        self.puntos += (bolitas * 2)

    def velocidad(self):
        return (2 + self.puntos) / 100

    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER")          

    # def comer_fantasma(self, fantasma):
    #     if fantasma == "rosa":
    #     self.puntos += 8
    #     elif fantasma == "verde":
    #     self.puntos += 6
    #     elif fantasma == "naranja":
    #     self.puntos += 4
    #     elif fantasma == "rojo":
    #     self.puntos += 2
    #esta es una manera de hacerlo pero no es la mejor, igual va bien

    #otra manera
    def comer_fantasma(self, fantasma, color):
        self.puntos += fantasma.puntos_color(color)
    class Fantasma:
        def __init__(self):
            self.fantasma = {"rosa": 8, "verde": 6, "naranja":4, "rojo":2}

        def puntos_color(self, color):
            return self.fantasmas(color)
        # self.puntos += self.puntos_de_fantasma
        # self.velocidad += 0.01 * self.puntos_de_fantasma    #aumenta 1% de velocidad por los puntos del fantasma que se comió

#b
class PacManMejorado(PacMan):
    def vidaExtra(self):
        if self.puntos  >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")

    def velocidad(self):
        return(3 + self.puntos) / 100
                
#5
#a- falta el git
#b- falta el git
#c- no, push es para subir
#d. si
#e- esta mal, es: git add . ; git commit -m "mensaje" ; git push
#f- esta bien
#g- despues tiene que hacer git pull para actualizarlo(hay que estar en la carpeta adecuada en el repositorio), no hay  que hacer git clone pq sino te lo baja de nuevo y te hace otro archivo.git y es complicado eso
