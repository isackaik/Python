num = int(input('Informe um número:\n'))
base = int(input('Escolha a base que deseja convertê-lo.\n1 - binário\n2 - octal\n3 - hexadecimal\n'))
if base == 1:
    conv = bin(num)
    print(conv[2::])
if base == 2:
    conv = oct(num)
    print(conv[2::])
if base == 3:
    conv = hex(num)
    print(conv[2::])


