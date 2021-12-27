n = int(input('Digite um número: '))
print(f'Calculando o fatorial {n}! = ')
c = n
f = 1
while c > 0:
    print(f'{c}', end ='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
