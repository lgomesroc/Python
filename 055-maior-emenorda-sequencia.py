#Leia pesos das pessoas e o tratamento de erro é que não existe peso 0, negativo ou maio que 250.
maior = menor = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if peso < 0 or peso > 250:
        print(f'Não existe peso 0, negativo ou maior que 250. Peso inválido!')
        break
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é: {maior}')
print(f'O menor peso é: {menor}')
