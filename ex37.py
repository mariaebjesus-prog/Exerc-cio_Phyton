#Exemplo — Três números em ordem crescente 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: Leia três números diferentes e mostre-os em ordem crescente. Não use listas nem funções prontas de ordenação: resolva apenas com se / senao se / senao.

n1 = int(input("Digite o primeiro número: "))# ta falando para digitar o primeiro número
n2 = int(input("Digite o segundo número: "))# ta falando para digitar o segundo número
n3 = int(input("Digite o terceiro número: "))# ta falando para digitar o terceiro número

# ta mostrando as variasoes pe pode dar do n1 , n2 e n3
if n1 <= n2 and n2 <= n3 :
    print(f"Ordem: {n1} {n2} {n3}")
elif n1 <= n3 and n3 <= n2 :
    print(f"Ordem: {n1} {n3} {n2}")
elif n2 <= n1 and n1 <= n3 :
    print(f"Ordem: {n2} {n1}{n3}")
elif n2 <= n3 and n3 <= n1 :
    print(f"Ordem: {n2} {n3} {n1}")
elif n3 <= n1 and n1 <= n2 :
    print(f"Ordem: {n3} {n1} {n2}")
else:
    print(f"Ordem: {n3} {n2} {n1}")
