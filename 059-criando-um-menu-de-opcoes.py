#Menu para realizar operações aritméticas simples
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 10:
    print('''MENU - OPÇÕES
    [ 1 ] SOMAR
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] POTÊNCIA
    [ 6 [ RAIZ QUADRADA
    [ 7 ] MAIOR
    [ 8 ] MENOR
    [ 9 ] NOVOS NÚMEROS
    [ 10 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif opcao == 2:
        subtrai = n1 - n2
        print(f'A subtração entre {n1} - {n2} é {subtrai}.')
    elif opcao == 3:
        multiplica = n1 * n2
        print(f'A multiplicação ente {n1} x {n2} é {multiplica}.')
    elif opcao == 4:
        divide = n1 / n2
        print(f'A divisão entre {n1} : {n2} é {divide:.2f}.')
    elif opcao == 5:
        potencia1 = n1**2
        potencia2 = n2**2
        print(f'A potência de {n1} é {potencia1} e a de {n2} é {potencia2}.')
    elif opcao == 6:
        raizquad1 = n1**0.5
        raizquad2 = n2**0.5
        print(f'A raiz quadrada de {n1} é {raizquad1:.2f} e de {n2} é {raizquad2:.2f}.')
    elif opcao == 7:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 8:
        if n1 < n2:
            menor = n1
        else:
            menor = n2
        print(f'O menor número entre {n1} e {n2} é {menor}')
    elif opcao == 9:
        print('Digite novos valores')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 10:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-' * 15)
print('Fim do programa. Obrigado e volte sempre')