#Exemplo — Desconto progressivo 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: LLeia o valor de uma compra e aplique o desconto da faixa correspondente. Mostre o valor do desconto e o valor final. 
if pa > 20:# ta falando que  se o lim for menor que 20  vai aparecer essa mensagem
    print(f"{pa:.2f} % - Sem infração ")
elif  pa <= 20:# ta falando que  se o lim  for até  o 20  vai aparecer essa mensagem
    print(f" {pa:.2f} % acima do limite- Infração média ")
elif   pa > 20 and pa <= 50:# ta falando que  se o lim está entre 20 e 50 vai aparecer essa mensagem
    print(f" {pa:.2f} % acima do limite- Infração grave ")
else:# ta falando que  se o lim é maior que 50 vai aparecer essa mensagem
    print(f"{pa:.2f} % acima do limite- Infração gravíssima ")