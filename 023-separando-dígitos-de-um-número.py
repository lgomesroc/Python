num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 1 % 10
centena = num //100 % 10
milhar = num // 1000 % 10
print('Verificando o número: ',format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))