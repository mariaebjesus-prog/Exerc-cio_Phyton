
 #Exemplo — O maior de dois
 #Aluno: Maria Eduarda Branco Gracia de Jesus
 #Objetivo: Leia dois números diferentes e mostre qual deles é o maior

n1 = float(input("Digite sua primeira numero: "))# ta falando para digitar a primeira numero
n2 = float(input("Digite sua segunda numero: "))# ta falando para digitar a segunda numero

maior = n1 #ta falando que se o n1 for menor que o n2 o ele vai ser o valor maior se não vai ser o n1
if n2 > maior:
    maior = n2  
print(f"O maior número é: {maior}")#resultado final