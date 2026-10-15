 #Exemplo — Saque no caixa eletrônico
 #Aluno: Maria Eduarda Branco Gracia de Jesus
 #Objetivo: Leia o saldo da conta e o valor que a pessoa quer sacar. Se houver saldo suficiente, mostre o novo saldo.Senão, mostre Saldo insuficiente.
saldo = float(input("Digite o saldo da conta: R$ "))#ta falando para digitar o saldo da conta
saque = float(input("Digite o valor que deseja sacar: R$ "))#ta falando para digitar o valor que deseja sacar               

novoSaldo = saldo - saque#ta mostrando como faz a conta para saber o seu novo saldo

if saque <= saldo:#a falando que se o saldo for maior que o saque vai apareser essa mensagem
    print(f"Saque realizado. Novo saldo: R$ {novoSaldo:.2f}")#resultado final   
else:#ta falando que se o saldo nao for suficente vai apareser essa mensagem
    print("Saldo insuficiente.")#resultado final