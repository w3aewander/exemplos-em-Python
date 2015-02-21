"""
   
   Exemplo de código usando a metodologia TDD.
   @author Wanderlei Silva do Carmo <wander.silva@gmail.com>
   @version 1.0
   
"""

import unittest
import math

class Calculadora(unittest.TestCase):
            
    def somar(self, x, y ):
        res = x + y
        return res
     
    def multiplicar(self, x, y):
        res = x * y
        return res
    
    def dividir(self, x,y):
        res = x / y
        return res
    
    def subtrair(self, x, y):
        res = x - y
        return res

    def resto(self, x,  y):
        res =  x % y
        return res

    def modulo(self, x, y ):
        if x > y:
            res = x // y
            return res
        return -1

    def ehMaior(self,x, y):
        return x > y
    
    def ehMenor(self, x, y):
        return ( x < y )

    def expo(self, x, y ):
        #return x ** y
        return math.pow(x,y)

    def raizQuadrada(self,x):
        return math.sqrt(x)

    def seno(self, x):
        return math.sin(x)

    def cosseno(self, x):
        return math.cos(x)

    def arredondaPraCima(self,x):
        return math.ceil(x)

    def arredondaPraBaixo(self,x):
        return math.floor(x)

    def deslocaNBitsDireita(self,x, y):
        return x >> y

    def deslocaNBitsEsquerda(self,x,y):
        return x << y
    


#Instanciando a classe.
calculadora = Calculadora()

#Fazendo os testes
calculadora.assertEquals(4, calculadora.somar(2,2), "linha %d Método soma.")
calculadora.assertEquals(6, calculadora.multiplicar(2,3), "Método multiplicação.")
calculadora.assertEquals(4, calculadora.dividir(8,2), "Método divisão.")
calculadora.assertEquals(8, calculadora.subtrair(24, 16), "Médtodo subração.")
calculadora.assertEquals(0, calculadora.resto(8,4), "Método resto deve ser 0." )
calculadora.assertEquals( 3, calculadora.resto(8,5), "Método resto deve retornar 3" )
calculadora.assertLessEqual( 1, calculadora.resto(8.5,3.3 ), "Método resto deve retornar 1" )
calculadora.assertEquals( 1, calculadora.modulo(9,8), "Método módulo da divisão deve retornar 1" )
calculadora.assertTrue( calculadora.ehMaior(9,8) , "Método ehMaior." )
calculadora.assertTrue( calculadora.ehMenor(8,9) , "Método ehMenor." )
calculadora.assertEquals( 16, calculadora.expo(4,2) , "Método expo(4,2) deve retornar 16." )
calculadora.assertEquals( 5 , calculadora.raizQuadrada(25) , "Método raiz quadrada de 25 deve ser 5." )
calculadora.assertEquals( 0.0 , calculadora.seno(0) , "Método seno(0) deve ser 0.0" )
calculadora.assertEquals( 1.0 , calculadora.cosseno(0) , "Método cosseno(0) deve ser 1.0" )
calculadora.assertEquals( 6.0 , calculadora.arredondaPraCima(5.3) , "Método arredondaPraCima(5.3) deve ser 6.0" )
calculadora.assertEquals( 5.0 , calculadora.arredondaPraBaixo(5.3) , "Método arredondaPraCima(5.3) deve ser 5.0" )


print("Todos os testes passaram.")
