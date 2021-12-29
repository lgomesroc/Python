num = int(input('Digite um número [999 saí do programa]: '))
cont = soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: [999 saí do programa]: '))
print(f'Você digitou {cont} termos e a soma dos números são: {soma}.')
