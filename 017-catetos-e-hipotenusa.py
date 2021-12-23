'''catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
h = (catop ** 2 + catad ** 2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(h))'''

from math import hypot
catod = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite um valor do caeto adjacente: '))
hip = hypot(catod,catad)
print('A hipotenusa é: {:.2f}'.format(hip))