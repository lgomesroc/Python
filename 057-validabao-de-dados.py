sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]#tira os espaços(strip) e pega só a primeira
# letra que transforma a minúscula em maiúscula(upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} digitado correto e registrado com sucesso!')