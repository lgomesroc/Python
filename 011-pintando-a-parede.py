altura=float(input('Digite o valor da altura da parede: '))
largura=float(input('Digie o valor da largura da parede: '))
area=(altura*largura)
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e a sua área é de {:.2f}m²'.format(altura,largura,area))
tinta= area/2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))