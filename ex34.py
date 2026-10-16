#Exemplo — Aprovação com frequência 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Para ser aprovado, o aluno precisa de média maior ou igual a 7.0 e frequência de pelo menos 75%. Leia duas notas e a frequência (em %) e mostre: 
n1 = float(input("Digite sua primeira numero: "))# ta falando para digitar a primeira numero
n2 = float(input("Digite sua segunda numero: "))# ta falando para digitar a segunda numero
fq = float(input("Digite sua frequência: "))# ta falando para digitar a frequência

media = (n1 + n2) / 2# ta mostrando como faz a conta para saber a média

if media < 7.0 and fq >= 75.0:# ta falando que a média é menor que 7.0 e a frequência é maior ou igual a 75.0 vai aparecer essa mensagem
    print("Reprovado por nota ")
elif media >= 7.0 and fq < 75.0:# ta falando que a média é maior ou igual a 7.0 e a frequência é menor que 75.0 vai aparecer essa mensagem
    print("Reprovado por falta ")
else:# ta falando que a média for maior ou igual a 7.0 e a frequência é maior ou igual a 75.0 vai aparecer essa mensagem
    print("Aprovado ")
