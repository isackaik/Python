from datetime import datetime
print(' Programa destinado para homens jovens.')
ano = int(input('Qual o seu ano de nascimento?\n'))
idade = int(datetime.today().strftime('%Y')) - ano

if idade < 18:
    print('Você ainda vai se alistar. Faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Corra para se alistar, já está na hora.')
elif idade > 18:
    print('Você já passou {} anos do prazo de se alistar.'.format(idade-18))
