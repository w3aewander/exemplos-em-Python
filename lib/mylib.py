
def somar(x,y):
    return x+y

def subtrair(x,y):
    return x-y

def dividir(x,y):
    if x == 0 or y == 0:
        return 0
    return x / y

def multiplicar(x,y):
    return x * y

def isPar(n):
    if n % 2 == 0:
        return true
    return false

def celsiusToFarenheit(celsius):
    return  ( 9 * celsius + 160 ) /5 

def farenheitToCelsius(farenheit):
    return  ( 5 * ( farenheit - 32   ) ) / 9 

def imc(peso,altura):
    return peso / ( altura**2 )

def classificacaoIMC( indice  ):
    r = ""
    if indice < 18.5:
        r="Magreza mórbida"
    elif indice > 18.5 and indice <= 24.9:
        r="Normal"
    elif indice >= 25 and indice <= 29.9:
        r="Sobrepeso"
    elif indice >= 30 and indice <= 39.9:
        r="Obeso"
    else:
        r="Obesidade grave"

    return r

