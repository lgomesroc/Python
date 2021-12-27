n = int(input('Digite um número: '))
print(f'Calculando o fatorial de {n}! = ')
c = n
f = 1
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-=1
print(f'{f}.')
