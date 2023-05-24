import Forca
import Sorteio


print('****************************************')
print('******Bem vindo, escolha seu jogo******')
print('****************************************')

print('(1) Sorteio (2) Forca ')

jogo = int(input('Qual jogo deseja jogar: '))
if(jogo == 1):
    print('\nJogando Sorteio')
    Sorteio.jogar()
elif(jogo == 2):
    print('\nJogando Forca') #jogo ainda será elaborado
    Forca.jogar()