
print('-=' * 20)
print('Analisando criação de triângulo')
print('-=' *20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Com esse valores, DÁ para criar um triângulo.')
else:
    print('Com esses valores, NÃO DÁ para criar um triângulo.')

