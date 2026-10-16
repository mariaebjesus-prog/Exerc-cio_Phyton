#Exemplo —  O maior de três 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:  Leia três números diferentes e mostre qual deles é o maior. 
n1 = int(input("Digite sua primeira numero: "))# ta falando para digitar a primeira numero
n2 = int(input("Digite sua segunda numero: "))# ta falando para digitar a segunda numero
n3 = int(input("Digite sua terceira numero: "))# ta falando para digitar a terceira numero

if  n1 > n2 and n1 > n3:# ta  falando que se n1 for maior que n2 e n3 vai aparecer essa mensagem
    print("o maior é: ",n1)
elif  n2 > n1 and n2 > n3:# ta falando que se n2 for maior que n1 e n3 vai aparecer essa mensagem
    print("o maior é: ",n2)
else:# ta falando que se n3 for maior que n1 e n2 vai aparecer essa mensagem
    print("o maior é: ",n3)