#Exemplo — Desconto progressivo 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: LLeia o valor de uma compra e aplique o desconto da faixa correspondente. Mostre o valor do desconto e o valor final. 
compra = float(input("Digite o valor da compra: "))#ta falando para digitar o valor da compra 

if compra <= 50:#ta falando que se a compra for menor ou igual a 50 nao vai ter  desconto
    print(f"Desconto: R$ 0.00 - Final: R$ {compra:.2f}")
elif compra <= 100: #ta falando que se a compra for menor ou igual a 100 vai ter desconto de 5%
    desconto = compra * 0.05
    valorfinal = compra - desconto
    print(f"Desconto: R$ {desconto:.2f} - Final: R$ {valorfinal}")
elif compra <= 200: #ta falando que se a compra for menor ou igual a 200 vai ter desconto de 10%
    desconto = compra * 0.10
    valorfinal = compra - desconto
    print(f"Desconto: R$ {desconto:.2f} - Final: R$ {valorfinal}")
else:#ta falando que se for maior  que 200 vai ter desconto de 15%
  desconto = compra * 0.15
  valorfinal = compra - desconto
  print(f"Desconto: R$ {desconto:.2f} - Final: R$ {valorfinal}")