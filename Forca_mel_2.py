import random

def jogar():

    mensagem_abertura()
    palavra_secreta =leitura_arquivo()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print('\nAcerte a palavra: ', letras_acertadas)

    errou = False
    acertou = False
    erros = 0

    while (not errou and not acertou):

        tentativa = inicia_tentativa()

        if (tentativa in palavra_secreta):
            marca_tentativa_certa(palavra_secreta, tentativa, letras_acertadas)
        else:
            erros += 1
            print('Ops, voce errou! Faltam {} tentativas.'.format(10-erros))

        errou = erros == 10
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        msg_ganhou()
    else:
        msg_perdeu(palavra_secreta)

    print('Fim de jogo!')


def mensagem_abertura():
    print('****************************************')
    print('***Bem vindo ao joguinho de forca***')
    print('****************************************')

def leitura_arquivo():
    arquivo = open(palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return['_' for letra in palavra]

def inicia_tentativa():
    tentativa = input('\nDigite uma letra: ')
    tentativa = tentativa.strip().upper()
    return tentativa

def marca_tentativa_certa(palavra_secreta, tentativa, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(tentativa == letra):
            letras_acertadas[index] = letra
        index += 1

def msg_ganhou():    
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('VOCE GANHOU')

def msg_perdeu(palavra_secreta):    
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('VC PERDEU!')

jogar()


