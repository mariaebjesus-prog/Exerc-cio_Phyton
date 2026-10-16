#Exemplo —  Caixa eletrônico: contagem de notas  
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:Um caixa eletrônico tem notas de R$ 100, R$ 50, R$ 20 e R$ 10. Leia o valor do saque (número inteiro) e mostre a menor quantidade de notas para pagá-lo.  

valor = int(input("Digite o valor do saque: "))# ta falando para digitar o valor do saque

if valor <= 0 or valor % 10 != 0:
    print("Valor inválido")

else:
    notas100 = valor // 100
    valor = valor % 100

    notas50 = valor // 50
    valor = valor % 50

    notas20 = valor // 20
    valor = valor % 20

    notas10 = valor // 10
    valor = valor % 10

    print(f" Notas de R$ 100: {notas100}")
    print(f" Notas de R$ 50: {notas50}")
    print(f" Notas de R$ 20: {notas20}")
    print(f" Notas de R$ 10: {notas10}")