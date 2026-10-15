#Exemplo — Aprovado ou reprovado
#Aluno: Maria Eduarda Branco Gracia de Jesus
#Objetivo: Leia duas notas de um aluno e calcule a média. Mostre a média e a mensagem Aprovado se ela for maior ou igual a 7.0, ou Reprovado caso contrário.

n1 = float(input("Digite sua primeira nota: "))#ta falando para digitar a primeira nota
n2 = float(input("Digite sua segunda nota: "))#ta falando para digitar a segunda nota
media = (n1 + n2) / 2

print(f"A média do aluno é: {media}")#ta mostrando como faz a conta

if media >= 7.0:#ta falando que se a media for igual ou acima de 7 esta aprovado se não esta reprovado
    print(f"Média: {media} — Aprovado")#resltado final
else:
    print(f"Média: {media} — Reprovado")#resultado final    