num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print(f'O primeiro valor é maior. O valor digitado foi: {num1}')
elif num2 > num1:
    print(f'O segundo valor é o maior. O valor digitado foi: {num2}')
elif num1 == num2:
    print(f'Não há valor maior pois os dois são iguais. O valor digitado foi: {num1}')
