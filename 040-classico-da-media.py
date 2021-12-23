#Calculando a média de um aluno porém tratando se digitar nota errada. verificar se o usuário digitar
#uma nota errada, o programa finaliza.
nota1 = float(input('Digite a primeira nota: '))
if nota1 > 10 or nota1 < 0:
    print(f'Nota inválida')

nota2 = float(input('Digite a segunda nota: '))
if nota2 > 10 or nota2 < 0:
    print(f'Nota inválida!')

media = (nota1 + nota2) / 2
print(f'Nota 1 foi {nota1:.1f} e nota 2 foi {nota2:.1f}, a sua média é de {media:.1f}')
if 7.0 >= media >= 5.0:
    print(f'Você está em RECUPERAÇÃO.')
elif media >= 7.0:
    print(f'Você está APROVADO!')
elif media < 5.0:
    print(f'Você está REPROVADO!')

