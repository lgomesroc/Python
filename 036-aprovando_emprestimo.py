#Empréstimo para financiamento de uma casa comprometendo a renda em 30%
casa = float(input('Digite o valor da casa:R$ '))
sal = float(input('Digite o salário:R$ '))
periodo = int(input('Quantos anos quer pagar?: '))
prestacao = casa / (periodo * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {periodo} anos e saláro de R${sal:.2f}, a prestação será de R${prestacao:.2f}!')
if prestacao <= (sal / 0.3):
    print(f'O empréstimo está abaixo ou igual a 30%. NEGADO!')
else:
    print(f'O empréstimo está acima de 30%. APROVADO! ')