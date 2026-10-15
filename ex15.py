 #Exemplo — Desconto na compra
 #Aluno: Maria Eduarda Branco Gracia de Jesus
 #Objetivo:Uma loja dá 10% de desconto em compras a partir de R$ 100,00. Leia o valor da compra e mostre o valor final a pagar.
compra = float(input("Digite o valor da compra: "))#ta falando para digitar o valor da compra 

if compra >= 100:#ta falando que se a compra for maior ou igual a 100 desconta 0.10
    desconto = compra * 0.10
    valorfinal = compra - desconto
    print(f"Valor final a pagar: R$ {valorfinal:.2f}")
else:#ta falando que se for menos que 100 nao desconta nada 
    print(f"Valor final a pagar: R$ {compra:.2f}")#resultado fonal