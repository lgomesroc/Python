distancia = float(input('Qual é a disstância da sua viagem? '))
print('Uau que distância boa! {}Km'.format(distancia))
if distancia >= 200:
    preco = distancia *0.50
else:
    preco = distancia *0.45
print('O preço da passagem será de R${:.2f}'.format(preco))