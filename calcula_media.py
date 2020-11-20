#Calculo da médaa
notas=[]

print("Cálculo da média")
print("Por favor, digite as notas dos quatro bimestres")

for i in range(4):
    print("Entre com a nota do ",
       i +1, " bimestre")
    nota=float(input())
    if  nota >=0 and nota<10:
        notas.append(nota)
    else:
        notas.append(0)
        
media = sum(notas) / len(notas)
resultado = ""

if media < 5:
    resultado = "reprovado"
elif media < 7:
    resultado = "em recuperação"
else:
    resultado = "aprovado"
    
print(" A media foi  ", media, " portando você está ", resultado )
#Fim..
