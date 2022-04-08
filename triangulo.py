r1 = int(input('Primeiro segmento?\n'))
r2 = int(input('Segundo segmento?\n'))
r3 = int(input('Terceiro segmento?\n'))
l = [r1, r2, r3]
if (max(l) < ((r1 + r2 + r3) - max(l)) and max(l) > abs((r1 - r2 - r3) + max(l))):
    print('Pode formar um triângulo ', end='')
    if r1 == r2 and r1 == r3:
        print('equilátero.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('escanelo.')
    else:
        print('isósceles.')
else:
    print('Esses segmentos não podem formar um triângulo.')