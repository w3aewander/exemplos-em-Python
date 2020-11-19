# -*- encode: utf8 -*- #
from lib.mylib import celsiusToFarenheit
from lib.mylib import farenheitToCelsius

print("Conversão entre temperaturas")

print("1 - Celsius para Farenheit")
print("2 - Farenheit para Celsius")

op = int(input())

if op == 1:
    print("Conversão de Celsius para Farenheit")
    print("Qual a temperatura em Celsius?")
    c = float( input() )
    print(c ,  " graus Celsius equivalem a ", 
                celsiusToFarenheit(c), " graus Farenheit")

elif op == 2:
    print("Convertendo de Farenheit para Celsius")
    print("Qual a temperatura em Farenheit ?")
    f = float( input() )
    print(f, " graus Farenheit equialem a ", 
             farenheitToCelsius(f), " graus Celsius.")

else:
    print("Desculpe, você deve escolher uma das opções disponíveis.")

    