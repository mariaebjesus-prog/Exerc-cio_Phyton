# Exemplo — Minutos em horas
# Aluno: Maria Eduarda Branco garcia de jesus
# Objetivo: Leia uma quantidade de minutos (número inteiro) e mostre quantas horas e quantos minutos ela representa.
m = int(input("Digite a quantidade de minutos: "))# ta falando para digitar a quantidade de minutos

h = m // 60# ta mostrando como faz a conta para saber a horas

minutos_restantes = m % 60# ta mostrando como faz a conta para saber os minutos restantes

print(f"A quantidade de minutos representa: {h} horas(s) e {minutos_restantes} minutos(s)")# resultado final