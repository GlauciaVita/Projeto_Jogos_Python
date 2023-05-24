import random

def jogar():

    print('****************************************')
    print('Bem vindo ao meu joguinho de sorteio')
    print('****************************************')

    total_testes = 0
    teste = 1
    numero_secreto = random.randrange(1, 51)

    print('Qual nivel de dificuldade?')
    print('(1) Facil (2) Medio (3) Dificil ')

    nivel = int(input('Escolha o nivel: '))
    if(nivel == 1):
        total_testes = 15
    elif(nivel == 2):
        total_testes = 10
    elif(nivel == 3):
        total_testes = 5

    while (teste <= total_testes):
        print('\nTeste: ', teste, 'de', total_testes)

        tentativa = int(input('\nDigite seu numero: '))
        print('Voce digitou: ',tentativa)
        if(tentativa < 1 or tentativa > 50):
            print('\n ---ATENCAO: DIGITE UM NUMERO ENTRE 1 E 50---')
            continue

        acertou = tentativa == numero_secreto
        maior = tentativa >numero_secreto
        menor = tentativa< numero_secreto
        if (acertou):
            print('\n-----Acertou-----')
            break
        else:
            if (maior):
                print('Errou, seu chute foi maior do que o numero secreto.')
            elif(menor):
                print('Errou, seu chute foi menor do que o numero secreto.')

        teste = teste +1
   
    print('\nFim de jogo!!!')

jogar()







