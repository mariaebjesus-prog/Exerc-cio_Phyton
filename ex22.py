#Exemplo — Termômetro da Serra 
#Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia a temperatura do dia em °C (pode ter casas decimais) e mostre a mensagem conforme a tabela.                            
temperatura = float(input("Digite a temperatura em °C: "))

if  temperatura < 0:#ta falando que se for menor que 0 vai aparecer essa mensagem
    print("Abaixo de zero — risco de geada! ")
elif temperatura < 10 :  #ta falando que se for menor que 10 vai aparecer essa mensagem
     print("Muito frio — capriche no agasalho ")
elif  temperatura < 18:#ta falando que se for menor que 18 vai aparecer essa mensagem
    print("Frio ")
elif  temperatura < 25:#ta falando que se for menor que 25 vai aparecer essa mensagem
    print("Agradável ")
else:#ta falando que se for acima de 25 vai aparecer essa mensagem
    print("Calor")    