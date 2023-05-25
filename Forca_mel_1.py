def jogar():
    print('****************************************')
    print('***Bem vindo ao joguinho de forca***')
    print('****************************************')

    palavra_secreta = 'chocolate'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    errou = False
    acertou = False
    erros = 0
    acertos = 0

    print('\nAcerte a palavra: ', letras_acertadas)

    while (not errou and not acertou):
        tentativa = input('\nDigite uma letra: ')
        tentativa = tentativa.strip().upper()

        if (tentativa in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(tentativa == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print('Ops, voce errou! Faltam {} tentativas.'.format(12-erros))

        errou = erros == 10
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('VOCE GANHOU')
    else:
        print('VC PERDEU!')

    print('Fim de jogo!')


jogar()


