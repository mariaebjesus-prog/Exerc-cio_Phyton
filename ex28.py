#Exemplo — Vogal ou consoante 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia uma letra minúscula e informe se ela é vogal ou consoante. 
letra = input("Digite uma letra minúscula: ")# ta falando para digitar uma letra minúscula

if letra in "aeiou":# ta falando que se a letra estiver emtre  essas vogais"aeiou" vai aparecer essa mensagem
    print(f"Vogal ")
else:# ta falando que se a letra não estiver emtre essas vogais "aeiou" vai aparecer essa mensagem
    print(f"Consoante ")