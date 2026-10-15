#Exemplo —  Radar com tipo de infração 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:Leia o limite de velocidade da via e a velocidade medida do carro. Calcule quantos por cento a velocidade passou do limite e classifique conforme a tabela. 
lim = float(input("Digite o limite de velocidade da via (km/h): "))# ta pedindo para ele digitar o limite de velocidade da via 
vel = float(input("Digite a velocidade medida do carro (km/h): "))# ta pedindo para ele digitar a velocidade do carro


pa = (vel - lim) / lim * 100# ta mostrando como fazer o cálculo para descobrir a velocidade


if pa <= lim:# ta falando que  se o lim for menor que 20  vai aparecer essa mensagem
  print(" Sem infração ")
elif  pa <= 20:# ta falando que  se o lim  for até  o 20  vai aparecer essa mensagem
    print(f" {pa:.2f} % acima - Infração média ")
elif  pa <= 50:# ta falando que  se o lim fot  até 50 vai aparecer essa mensagem
    print(f" {pa:.2f} % acima - Infração grave ")
else:# ta falando que  se o lim é maior que 50 vai aparecer essa mensagem
    print(f"{pa:.2f} % acima - Infração gravíssima ")