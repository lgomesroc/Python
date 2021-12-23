numero = int(input('Digite um número: '))
numdiv = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[34m', end=' ')
        numdiv += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
if numdiv == 2:
    print(f'\n\033[mO número {numero} é divisível por {numdiv} números. É número primo.')
else:
    print(f'\n\033[mO número {numero} é divisível por {numdiv} números. Não é número primo.')
