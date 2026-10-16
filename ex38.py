#Exemplo — Equação do 2º grau 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:Leia os coeficientes a, b e c de uma equação ax² + bx + c = 0 e resolva 
n1 = int(input("Digite o coeficiente a: "))# ta falando para digitar o coeficiente a
n2 = int(input("Digite o coeficiente b: "))# ta falando para digitar o coeficiente b
n3 = int(input("Digite o coeficiente c: "))# ta falando para digitar o coeficiente c

Δ = n2**2 - 4 * n1 * n3

if n1 == 0:
    print("Não é uma equação do 2º grau")
elif Δ < 0:
    print(" Não existem raízes reais")
elif Δ == 0:
    x = -n2 / (2 * n1)
    print(f"Uma raiz: x = {x}")
else :
    x1 = (-n2 + Δ**0.5) / (2 * n1)
    x2 = (-n2 - Δ**0.5) / (2 * n1)
    print(f" x1 = {x1} e x2 = {x2}")