soma = cont = 0
for c in range(1,7):
    num = int(input(f'Digite {c}º número: '))
    if num %2 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} números pares digitados é: {num}')
