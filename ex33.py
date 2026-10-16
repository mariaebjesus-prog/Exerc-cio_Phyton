#Exemplo —  Voto obrigatório 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia a idade de uma pessoa e informe a situação dela nas eleições brasileiras.
idade = int(input("Digite a idade: "))#ta falando para digitar a idade

if idade < 16 :# ta falando que a idade é menor que 16 vai aparecer essa mensagem
    print("Não pode votar ")
elif idade >= 16 and idade < 17:# ta falando que a idade é maior ou igual for entre 16 e 17 vai aparecer essa mensagem
    print("Voto facultativo.")
elif idade >= 18 and idade <= 70:# ta falando que a idade for entre  18 e 70 vai aparecer essa mensagem
    print("Voto obrigatório.")
else:# ta falando que a idade é maior que 70 vai aparecer essa mensagem
    print("Voto facultativo ")   
