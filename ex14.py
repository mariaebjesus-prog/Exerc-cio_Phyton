#Exemplo — Radar de velocidade
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Numa via com limite de 80 km/h, leia a velocidade de um carro. Se ele passou do limite, mostre quantos km/h acima ele estava. Senão, mostre Velocidade dentro do limite. Boa viagem!
vel = float(input("Digite a velocidade do carro (km/h): "))# ta falando para digitar a velocidade
  
excesso = vel - 80#ta mostrando como faz a conta para saber se passou do limite ou não

if vel > 80:# ta falando que se a velocidade for maior que o limite vai dar essa resposta
    print(f"Multado! Você passou {excesso} km/h  do limite.")
else:# se nao for maior que o limite vai dar essa resposta
    print("Velocidade dentro do limite. Boa viagem!")