#num1 = input('Digite o primeiro valor:')
#num2 = input('Digite o segundo valor:')
#print(num1 + num2)-> aqui vai juntar o num1 e o num2



#num1 = input('Digite o primeiro valor:')
#num2 = input('Digite o segundo valor:')
#print(num1 , num2) -> aqui vai mostrar os dois valores separados


num1 = int (input('Digite o primeiro valor:'))
num2 = int (input('Digite o segundo valor:')) # tipo primitivo deve ser especificado. Por padrão é string
soma = num1 + num2
# print('A soma de',num1, 'e', num2, 'é', soma) -> formato antiga do Python 2
print('A soma de {} e {} é {}'.format(num1, num2, soma))
