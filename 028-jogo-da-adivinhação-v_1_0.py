from random import randint
from time import sleep ## importar o nétodo sleep da classe time

comp = randint(0, 5) #a variável comp sorteará um número e irá guardar
print('-=-' * 25)
print('Pensando num número entre 0 e 5. Quero ver adivinhar... KKKK')
print('-=-' * 25)
jog = int(input('Em que número pensei? ')) #Jogador tentando adivinhar
print('PROCESSANDO... AGUARDE!')
sleep(5) #Vai travar durante segundos.
if comp == jog:
    print('Ae você adivinhou. Parabéns!!! O número é {}'.format(comp))
else:
    print('KKKK Eu ganhei!!! O Número é esse: {}'.format(comp))