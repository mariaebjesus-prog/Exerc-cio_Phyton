#Exemplo — Login com usuário e senha 
# Aluno: Maria Eduarda Branco Gracia de Jesus
# Objetivo: O usuário cadastrado é aluno e a senha é 1234. Leia o usuário e a senha (os dois como texto) e mostre: • Usuário não encontrado, se o usuário estiver errado; • Senha incorreta, se o usuário estiver certo mas a senha estiver errada; • Login realizado com sucesso!, se os dois estiverem certos.  

user = input("Digite o usuário: ")# ta falando para digitar o usuário
senha = input("Digite a senha: ")# ta falando para digitar a senha

if user != "aluno":# ta falando que o usuário é "aluno"  estiver errado vai aparecer essa mensagem
    print("Usuário não encontrado")
elif senha != "1234":# ta falando que a senha é "1234" estiver errada vai aparecer essa mensagem
    print("Senha incorreta.")
else:# ta falando que o usuário é "aluno" estiver certo e a senha estiver certa vai aparecer essa mensagem
    print("Login realizado com sucesso!")