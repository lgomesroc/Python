#Saber se pode criar um triângulo e classificar em equilátero, isósceles e escaleno ou ainda que
#não dá para criar um triângulo
r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os lados PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print(f'EQUILÁTERO!')
    elif r1 != r2 != r3 and r1 != r3:
        print(f'ESCALENO!')
    else:
        print(f'ISÓSCELES!')
else:
    print(f'Os lados digitados NÃO PODEM FORMAR um triângulo.')

