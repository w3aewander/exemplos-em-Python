"""
Esta função verifica se um determinadao ip
é verdadeiro ou falso com base no número de octetos
informados. Se o número de octetos for diferente de 4
ou um dos octetos maior que 255 o ip é falso caso contrário
o ip é verdadeiro

@author Wanderlei Silva do Carmo <wander.silva@gmail.com>
@version 1.0

"""

def ip_valido(IP):

    #divide a string contendo o ip em octetos
    octetos =  IP.split(".")
    
    #Verifica se o número de octetos é diferente de 4
    if  len(octetos) !=  4:
        return False

    #cria uma lista para adicionar cada um dos octetos      
    ip = []                  

    #Itera na lista de octetos e adiciona cada octeto encontrado
    #na lista "ip"    
    for octeto in octetos:
        octeto = (int) (octeto)
        ip.append( octeto )

    #Altera a lista "ip" substituindo cada elemento pelo resultado das comparações
    #de cada octeto. Se o octeto for maior que 255 então o-substitui por false
    ip = [ f > 255 for f in ip ]

    #Verifica se algum é maior que 255
    #Se encontrar algum então o resultado será True senão será False
    #Se não houver um valor True então o ip informado é válido.
    return ( True not in ip )


#Apenas para testar a função...
lista_ips = ["192.168.1.1", "192.168.345.3", "1.2.3" ]

for f in lista_ips:
    print ( "IP %s é %s" % (f, ip_valido(f) ) )


#Fim
