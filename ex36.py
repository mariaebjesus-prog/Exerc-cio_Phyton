#Exemplo — Pedra, papel e tesoura 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Dois jogadores digitam suas jogadas: pedra, papel ou tesoura. Mostre quem venceu ou se deu empate.Regras: pedra vence tesoura, tesoura vence papel e papel vence pedra. Se algum jogador digitar uma opção que não existe, mostre Jogada inválida.  
j1 = input("Jogador 1, digite sua jogada (pedra, papel ou tesoura): ") # ta falndo para o j1 digitatar sua jogada
j2 = input("Jogador 2, digite sua jogada (pedra, papel ou tesoura): ") # ta falndo para o j2 digitatar sua jogada

if j1 == j2:# ta falando que se j1 for igual a j2 vai dar empate 
    print("Empate !")
# ta mostrando as jogadas da pedra 
elif (j1 == "pedra" and j2 == "tesoura"):
    print("Jogador 1 venceu!")
elif (j1 == "pedra" and j2 == "papel"):
    print("Jogador 2 venceu!")

 # ta mostrando as jogadas da tesoura
elif (j1 == "tesoura" and j2 == "pedra"):
    print("Jogador 2 venceu!")
elif (j1 == "tesoura" and j2 == "papel"):
    print("Jogador 1 venceu!")

 # ta mostrando as jogadas do papel
elif (j1 == "papel" and j2 == "tesoura"):
    print("Jogador 2 venceu!")
elif (j1 == "papel" and j2 == "pedra"):
    print("Jogador 1 venceu!")

else:# ta falando que se nenhuma das condições anteriores for verdadeira, a jogada é inválida
    print("Jogada inválida")