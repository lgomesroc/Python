dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quanos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('Total é de R$ {:.2f}'.format(pago))