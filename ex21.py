# Exemplo — Faixa etária
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia a idade de uma pessoa e mostre a faixa etária conforme a tabela.
idade = int(input("Digite a idade: "))
# ta mostrando como vai dar as respostas de acordo com cada idade 
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")