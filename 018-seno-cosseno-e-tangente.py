from math import cos, sin, tan, radians
angulo = float(input('Digite um valor de um ângulo: '))
rad = radians(angulo)
print('O seno do ângulo {} é: {:.2f}'.format(angulo,sin(rad)))
print('O cosseno do ângulo {} é: {:.2f}'.format(angulo,cos(rad)))
print('A tangente do ângulo {} é: {:.2f}'.format(angulo,tan(rad)))