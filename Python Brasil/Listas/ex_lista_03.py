#Programa que leia 4 notas, mostre as notas e a média na tela
notas = list()
media = soma = 0
for i in range(0, 4):
    notas.append(float(input(f'Digite a {i+1}ª nota: ')))
    soma += notas[i]
print(notas)
media = soma / 4
print(media)