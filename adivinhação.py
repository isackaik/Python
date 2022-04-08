import random
n = random.randint(1, 100)
rodada = 1
pontos = 1000
tentativas_de_acerto = 0
nivel = int(input("Escolha o nível do jogo: 1, 2 ou 3.\n"))
if nivel == 1:
    tentativas_de_acerto = 20
elif nivel == 2:
    tentativas_de_acerto = 10
elif nivel == 3:
    tentativas_de_acerto = 5
for rodada in range(1, tentativas_de_acerto + 1):
    chute = int(input('Rodada {} de {}. Digite um número de 1 a 100: \n'.format(rodada, tentativas_de_acerto)))
    acertou = chute == n
    baixo = chute < n
    alto = chute > n
    if acertou:
        print('Voce acertou.')
        break
    elif baixo:
        print('Tente mais alto.')
        pontos = pontos - (1000/tentativas_de_acerto)
    elif alto:
        print('Tente mais baixo.')
        pontos = pontos - (1000/tentativas_de_acerto)
    print('Sua pontuação atual é: {}.'.format(pontos))
print('Fim de jogo. Sua pontuação final foi: {}.'.format(pontos))
