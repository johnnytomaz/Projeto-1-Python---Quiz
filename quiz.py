print('Olá! Seja bem-vindo.')
answer_user = input('Deseja iniciar um quiz? Sim ou não?')
print(answer_user)


if answer_user == 'Sim':
    print('Então vamos começar! O Quiz é sobre a história do Brasil.')
else:
    print('Que pena! Vamos deixar para uma próxima...')
    quit()

score = 0

print('Qual foi o primeiro português a chegar no Brasil? \n (A) Pedro Alváres Cabral \n (B) Camões \n (C) Vasco da Gama \n (D) Pero Vaz de Caminha \n')
answer_1 = input('Resposta:')
if answer_1 == "A":
    print('Correto!')
    score = score + 1
else:
    print('Infelizmente, resposta errada!')

print('Em que ano o Brasil tornou-se independente? \n (A) 1855 \n (B) 1889 \n (C) 1818 \n (D) 1822 \n')
answer_2 = input('Resposta:')
if answer_2 == "D":
    print('Correto!')
    score = score + 1
else:
    print('Infelizmente, resposta errada!')

print('Quem foi o primeiro presidente do Brasil? \n (A) Getúlio Vargas \n (B) Marechal Deodoro \n (C) Juscelino Kubitschek \n (D) Floriano Peixoto    \n')
answer_3 = input('Resposta:')
if answer_3 == "B":
    print('Correto!')
    score = score + 1
else:
    print('Infelizmente, resposta errada!')

print(f'Quiz acabou! Pontuação: {score}/3')