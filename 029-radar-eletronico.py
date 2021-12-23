velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO. Excesso de velocidade e ultrapassou o limite que é de 80km/h')
    print('A multa a ser paga é de R${:.2f}'.format((velocidade - 80) * 7))
print('Tenha um bom dia! Cuidado ao dirigir hein?')