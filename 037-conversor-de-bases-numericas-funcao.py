#Conversão em binário, octal e hexadecimal através de função - fucionando

def conversao(num, pos):
    if pos == 1:
        return print(f'O número digitado em INÁIO é: {bin(num)[2:]}')
    elif pos == 2:
        return print(f'O Número digitado em OCTAL é: {oct(num)[2:]}')
    elif pos == 3:
        return print(f'O Número digitado em HEXADECIMAL é: {hex(num)[2:]}')
    else:
        print(f'Você digitou a opção {pos} e está errada.')
        return num

numero = int(input('Digite um número inteiro: '))
print('''Escolha a opção digitando um número para a conversão:
    1 - BINÁRIO
    2 - OCTAL
    3 - HEXADECIMAL''')
opcao = int(input('Escolha a sua opção: '))
conversao(numero, opcao)
print(f'Fim do programa')

