#Exemplo — Calculadora 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:  Exercícios que juntam tudo: cálculos, várias decisões, operadores lógicos e se aninhado. Planeje no papel ntes de abrir o Portugol Studio. 
n1 = float(input("Digite o primeiro número: "))# ta falando digitar o primeiro número
n2 = float(input("Digite o segundo número: "))# ta falando digitar o segundo número
op = input("Digite a operação (+, -, *, /): ")# ta falando digitar a operação

if op == "+":# ta falando que se a conta for de mais vai aparecer essa mensagem
    resultado = n1 + n2
    print(f"Resultado: {resultado}")
elif op == "-":# ta falando que se a conta for de menos vai aparecer essa mensagem
    resultado = n1 - n2
    print(f"Resultado: {resultado}")
elif op == "*":# ta falando que se a conta for de multiplicação vai aparecer essa mensagem
    resultado = n1 * n2
    print(f"Resultado: {resultado}")
elif op == "/" and n2 == 0:# ta falando que se a conta for de divisão e o segundo número for zero vai aparecer essa mensagem
     print("Erro: divisão por zero")
elif op == "/": # ta falando que se a conta for de divisão vai aparecer essa mensagem
    resultado = n1 / n2
    print(f"Resultado: {resultado}")
else:# ta falando que se a conta for de outro operador vai aparecer essa mensagem
    print("Operador inválido")