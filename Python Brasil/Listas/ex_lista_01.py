#Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = list()
for num in range(1, 6):
    lista.append(int(input(f'Digite um valor para a lista: ')))
print(lista)