#Escolhendo a forma de pagamento e tratando opção inválida como erro
import sys #Aqui deve-se importar o módulo sys para tratar erro de forma simples.
print('LUCIANO LOJAS')
preco = float(input('Preço das compras : R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] Á VISTA DINHEIRO / CHEQUE
[ 2 ] À VISTA NO CARTÃO 
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
opcao = int(input('Qual a sua opção?: '))
if opcao == 1:
    total = preco - (preco *0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
elif opcao == 4:
    total = preco + (preco * 0.2)
    totparc = int(input('Quantas parcelas?: '))
    parcela = total / totparc
    print(f'Sua compra será parcela em {totparc}x de R${parcela:.2f} COM JUROS! ')
else:
    total = preco
    print(f'Forma de pagamento inválida. Tente novamente com as opções amostradas.')
    sys.exit()#Tratamento de erro. Se usuário digitar errado a opção, sai do programa.
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
