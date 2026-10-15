# Exemplo — Situação do aluno
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia duas notas, calcule a média e mostre a situação do aluno conforme a tabela.
nota1 = float(input("Digite a primeira nota: "))#ta falando para digitar a primeira nota
nota2 = float(input("Digite a segunda nota: "))#ta falando para digitar a segunda nota
media = (nota1 + nota2) / 2#ta mostrando como faz a conta 

if media >= 7:#ta falando que se a media for maior ou igual a 7 vai aparecer isso
    print("Aluno aprovado.")
elif media >= 5:#ta falando que se a media for maior ou igual a 5 vai aparecer isso
    print("Aluno em recuperação.")
else:#ta falando que se a media for menor que 5 vai aparecer reprovado
    print("Aluno reprovado.")