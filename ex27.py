#Exemplo — Número no intervalo 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia um número inteiro e informe se ele está entre 1 e 100, incluindo o 1 e o 100. 
numero = int(input("Digite um número inteiro: "))# ta falando para digitar um numero inteiro

if  numero >= 1 and numero <= 100:# tafalando que se o numero estiver entre 1 e 100 vai aparecer essa mensagem
    print(f"Dentro do intervalo ")
else:# tafalando que se o numero não estiver entre 1 e 100 vai aparecer essa mensagem
    print(f"Fora do intervalo ")