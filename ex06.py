# Exemplo — Compra na cantina
# Aluno: Maria Eduarda Branco garcia de jesus
# Objetivo: Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e o troco. Considere que o valor pago é sempre suficiente.
pr = float(input("Digite o preço do lanche: "))# ta falando para digitar o preço do lanche
quan = int(input("Digite a quantidade comprada: "))# ta falando para digitar a quantidade comprada
val = float(input("Digite o valor pago pelo cliente: "))# ta falando para digitar o valor pago pelo cliente

total = pr * quan# ta mostrando como faz a conta para saber o total da compra
troco = val - total# ta mostrando como faz a conta para saber o troco
# resultado final
print(f"O total da compra é: R$ {total}")
print(f"O troco é: R$ {troco}")