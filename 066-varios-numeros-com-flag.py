soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'A soma dos valores foi de {soma} e a quantidade de números digitados são {cont}.')