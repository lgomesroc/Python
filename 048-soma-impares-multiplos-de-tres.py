soma = cont = 0
for num in range(1,501,2):
    if num %3 == 0:
        soma += num
        cont +=1
print(f'A soma de todos os {cont} valores solicitados é de : {soma}', end='')
