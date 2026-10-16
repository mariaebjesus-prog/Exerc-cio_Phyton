#Exemplo — Ano bissexto 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia um ano e informe se ele é bissexto. Um ano é bissexto quando é divisível por 4 e não é divisível por 100, ou quando é divisível por 400. 
ano = int(input("Digite um ano: "))# ta falando para digitar um ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:# ta falando que se o ano for divisível por 4 e não for divisível por 100 ou for divisível por 400 vai aparecer essa mensagem
    print("Bissexto.")
else:# ta falando que se o ano não for bissexto vai aparecer essa mensagem
    print("Não é bissexto.")