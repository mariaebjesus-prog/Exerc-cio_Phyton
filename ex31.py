#Exemplo —  Tipo de triângulo 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia os três lados de um triângulo. Primeiro verifique se eles formam um triângulo: cada lado precisa ser menor que a soma dos outros dois. Se não formarem, mostre Esses lados não formam um triângulo. Se formarem, classifique: equilátero, isósceles ou escaleno.

l1 = int(input("Digite o primeiro lado: "))  # ta falando para digitar o primeiro lado
l2 = int(input("Digite o segundo lado: "))  # ta falando para digitar o segundo lado
l3 = int(input("Digite o terceiro lado: "))  # ta falando para digitar o terceiro lado


if l1 == l2 == l3:# ta falando que os três lados são iguais vai aparecer essa mensagem
    print("Equilátero.")
elif l1 == l2 or l2 == l3 or l1 == l3:# ta falando que dois lados são iguais vai aparecer essa mensagem
    print("Isósceles")
elif l1 != l2 and l2 != l3 and l1 != l3:# ta falando que todos os lados são diferentes vai aparecer essa mensagem
    print("Escaleno")
else:# ta falando que os lados não formar um triângulo vai aparecer essa mensagem
    print("Esses lados não formam um triângulo")