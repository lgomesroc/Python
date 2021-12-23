from random import choice
nome1 = str(input('Digite um nome de aluno qualquer: '))
nome2 = str(input('Digite um nome de aluno qualquer: '))
nome3 = str(input('Digite um nome de aluno qualquer: '))
nome4 = str(input('Digite um nome de aluno qualquer: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista) #Escolhe um valor
print('O nome escolhido pelo professor é: {}'.format(escolhido))
