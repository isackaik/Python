r1 = int(input('Primeiro segmento?\n'))
r2 = int(input('Segundo segmento?\n'))
r3 = int(input('Terceiro segmento?\n'))
l = [r1, r2, r3]
if (max(l) < ((r1 + r2 + r3) - max(l)) and max(l) > abs((r1 - r2 - r3) + max(l))):
    print('Pode formar triângulo.')
    if r1 == r2 and r1 == r3:
        print('Esses segmentos formam um triângulo equilátero.')
    elif (r1 == r2 and r1 != r3) or (r2 == r3 and r2 != r1) or (r3 == r1 and r3 != r2):
        print('Esses segmentos formam um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esses segmentos formam um triângulo escanelo.')
else:
    print('Não pode formar triangulo.')