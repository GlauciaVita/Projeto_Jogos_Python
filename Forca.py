def jogar():
    print('****************************************')
    print('***Bem vindo ao meu joguinho de forca***')
    print('****************************************')

    palavra_secreta = 'caneta'
    errou = False
    acertou = False

    while (not errou and not acertou):

        tentativa = input('Digite uma letra: ').strip()
      
        index = 0
        for letra in palavra_secreta:
            if(tentativa.upper() == letra.upper()):
                print('Acertou a letra {} na posição {}'.format(letra, index))
            index = index + 1
        print('Jogando...')




    print('Fim de jogo!')


jogar()


