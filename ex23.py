#Exemplo — Cardápio da cantina 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Mostre o cardápio abaixo na tela, leia o código do produto e a quantidade, e mostre o total a pagar. Se o código não existir, mostre Código inválido.               
print("       Cardápio:")      
print("1 - Pão de queijo - R$ 4.50")
print("2 -    Coxinha  -   R$ 6.00 ")
print("3 -    Pastel   -   R$ 7.00 ")
print("4 - Suco    -   R$ 5.00 ")
print("5 - Café - R$ 3.00 ")
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

soma = 0 # ta fazendo isso para nao ter erro
# par demonstras o valor que cada soma 
if codigo == 1:
    soma = 4.50 * quantidade
elif codigo == 2:
    soma = 6.00 * quantidade
elif codigo == 3:
    soma = 7.00 * quantidade
elif codigo == 4:
    soma = 5.00 * quantidade
elif codigo == 5:
    soma = 3.00 * quantidade
else:
    print("Código inválido.")

print("O total a pagar é: R$ " + str(soma))# resultado final
