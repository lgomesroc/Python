from random import shuffle
nome1 = str(input('Digite um nome de um aluno qualquer: '))
nome2 = str(input('Digite um nome de um aluno qualquer: '))
nome3 = str(input('Digite um nome de um aluno qualquer: '))
nome4 = str(input('Digite um nome de um alunoqualquer: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista) #método que faz embaralhar uma lista ordenada e a escolha é aleatória
print('A sequencia de nomes dos alunos são: {}'.format(lista))