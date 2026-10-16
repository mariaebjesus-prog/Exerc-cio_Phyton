#Exemplo — Equação do 2º grau 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo:Leia os coeficientes a, b e c de uma equação ax² + bx + c = 0 e resolva 
n1 = int(input("Digite o coeficiente a: "))# ta falando para digitar o coeficiente a
n2 = int(input("Digite o coeficiente b: "))# ta falando para digitar o coeficiente b
n3 = int(input("Digite o coeficiente c: "))# ta falando para digitar o coeficiente c

Δ = n2**2 - 4 * n1 * n3# ta calculando o delta

if n1 == 0:# ta falando que se o n1 for zero vai aparecer a mensagem
    print("Não é uma equação do 2º grau")
elif Δ < 0:# ta falando que se o delta for menor que zero vai aparecer a mensagem
    print(" Não existem raízes reais")
elif Δ == 0:# ta falando que se o delta for igual a zero vaifazer a conta e vai  aparecer a mensagem 
    x = -n2 / (2 * n1)
    print(f"Uma raiz: x = {x}")
else :# ta falando que se o delta for maior que zero vai fazer as duas conta e vai aparecer a mensagem
    x1 = (-n2 + Δ**0.5) / (2 * n1)
    x2 = (-n2 - Δ**0.5) / (2 * n1)
    print(f" x1 = {x1} e x2 = {x2}")