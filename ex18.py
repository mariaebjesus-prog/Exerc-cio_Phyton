#Exemplo — Maior ou iguais
 #Aluno: Maria Eduarda Branco Gracia de Jesus
 #Objetivo: Leia dois números e mostre qual é o maior. Se forem iguais, mostre Os números são iguais.
n1 = float(input("Digite o primeiro número: "))#ta falando para digitar o primeiro numero
n2 = float(input("Digite o segundo número: "))#ta falando para digitar o segundo numero

if n1 > n2:#ta falando que se o n1 for maior vai apareser isso
    print(f"O maior número é: {n1}")
elif n2 > n1:#ta falando que se o n2 for maior vai apareser isso
    print(f"O maior número é: {n2}")
else:#ta falando que se os numeros forem iguais vai apareser isso
    print("Os números são iguais.")