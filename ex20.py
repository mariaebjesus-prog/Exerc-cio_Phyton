# Exemplo — Dia da semana
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:Leia um número de 1 a 7 e mostre o dia da semana correspondente (1 = Domingo, 2 = Segunda-feira, … 7 = Sábado). Para qualquer outro número, mostre Dia inválido.
dia = int(input("Digite um número de 1 a 7: "))# ta falando para digitar um numeru de 1 a 7 

# ta mostrando o dia da semana correspondente ao numero digitado
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido.")