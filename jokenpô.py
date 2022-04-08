import random

print('Vamos jogar JOKENPÔ!')
escolhas = ['pedra', 'papel', 'tesoura']
computer = random.choice(escolhas)
continuar = 'sim'
while continuar == 'sim':
    jogador = str(input('Escolha: pedra, papel ou tesoura.\n'))
    if jogador == computer:
        print('O computador escolheu {}.'.format(computer))
        print('Deu empate. Tente novamente.')
    elif jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
        print('Escolha uma opção válida.')
    elif jogador == 'pedra' and computer == 'tesoura':
        print('O computador escolheu {}.'.format(computer))
        print('Você ganhou!')
    elif jogador == 'papel' and computer == 'pedra':
        print('O computador escolheu {}.'.format(computer))
        print('Você ganhou!')
    else:
        print('O computador escolheu {}.'.format(computer))
        print('Você perdeu.')
    continuar = str(input('Quer continuar jogando?\n'))
