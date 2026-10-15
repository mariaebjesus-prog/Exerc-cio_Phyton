# Exemplo — Divisão segura
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia dois números: o dividendo e o divisor. Se o divisor for zero, mostre Erro: não existe divisão por zero. Caso contrário, mostre o resultado da divisão 

dividendo = float(input("Digite o dividendo: "))#ta falando para digitar o dividendo
divisor = float(input("Digite o divisor: "))#ta falando para digitar o divisor

if divisor == 0:#ta falando que se a divisao for zero vai dar essa resposta
    print("Erro: não existe divisão por zero")#resultado final  
else:
    resultado = dividendo / divisor# ta falando como faz a divisao
    print(f"O resultado da divisão é: {resultado}")#resultado final 