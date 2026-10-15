#Exemplo — Calculadora de IMC 
 #Aluno: Maria Eduarda Branco Gracia de Jesus
 #Objetivo: Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC = peso ÷ (altura × altura) e mostre a classificação. 
kg = float(input("Digite seu peso (kg): "))# ta falando para digitar o seu pesso 
m = float(input("Digite sua altura (m): "))#ta falando para digitar a sua altura

imc = kg / (m * m)# ta mostrando como fas a conta para saber o imc

if imc < 18.5:# ta falando que  se o imc é menor que 18.5  vai aparecer essa mensagem
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif 18.5 <= imc < 25:# ta falando que  se o imc está entre 18.5 e 25 vai aparecer essa mensagem
    print(f"IMC: {imc:.2f} - Peso normal")
elif 25 <= imc < 30:# ta falando que  se o imc está entre 25 e 30 vai aparecer essa mensagem
    print(f"IMC: {imc:.2f} - Sobrepeso")
else:# ta falando que  se o imc é maior ou igual a 30 vai aparecer essa mensagem
    print(f"IMC: {imc:.2f} - Obesidade")