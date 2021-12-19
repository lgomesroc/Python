# Python
Aqui estarão os códigos de exercícios e projetos

#Troca base de conversão de decimal para binário, octal e hexadecimal calculando mais de uam vez.

while True:
    num = int(input('Digite um número inteiro: '))
    print('''Escolha a opção digitando um número para a conversão:
    [1] - BINÁRIO
    [2] - OCTAL
    [3] - HEXADECIMAL''')
    pos = int(input('Escolha a sua opção: '))

    if pos == 1:
        print(f'{num} convertido em binário é: {bin(num)[2:]}')
        op = str(input("Deseja continuar [S/N]: "))
        if op == 'Nn':
            print(f'Saindo do programa!')
            break
        else:
            print('Opção inválida! Tente de novo.')

    elif pos == 2:
        print(f'{num} convertido em octal é: {oct(num)[2:]}')
        op = str(input("Deseja continuar [S/N]: "))
        if op == 'Nn':
            print(f'Saindo do programa!')
            break
        else:
            print('Opção inválida! Tente de novo.')

    elif pos == 3:
        print(f'{num} convertido em hexadecimal é: {hex(num)[2:]}')
        op = str(input("Deseja continuar [S/N]: "))
        if op == 'Nn':
            print(f'Saindo do programa!')
            break
        else:
            print('Opção inválida! Tente de novo.')

    else:
        print(f'Opção inválida. Tente novamente!')
        op = str(input("Deseja continuar [S/N]: "))
        if op == 'Nn':
            print(f'Saindo do programa!')
            break
        else:
            print('Opção inválida! Tente de novo.')

print(f'Aqui termina o programa. Obrigado por utilizar.')
