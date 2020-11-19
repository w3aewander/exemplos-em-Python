# -*- encode: utf8 -*- #

#from lib.mylib import *
from lib.mylib  import imc
from lib.mylib import classificacaoIMC

print("Calculo do IMC:")

print("Qual é o seu peso em Kg?")
peso = float(input())

print("Qual é a sua altura?")
altura = float(input())

resultado = imc(peso,altura)

print("Seu IMC é: ", resultado )

print("Segundo a OMS - Organização Mundia da Saúde, seu peso está classificado como: ", 
       classificacaoIMC(resultado)
       )


