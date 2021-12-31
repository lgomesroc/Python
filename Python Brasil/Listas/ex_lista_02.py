#Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
listareal = []
for cont in range(1, 11):
    listareal.append(float(input('Digite um valor para a lista: ')))
print(listareal)
listareal.sort(reverse= True)
print(listareal)
