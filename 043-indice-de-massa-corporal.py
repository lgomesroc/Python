#CLcular o índice da massa corporal (IMC)
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em m: '))
imc = peso / altura ** 2
print(f'O seu IMC é: {imc:.1f}',end=' ')
if imc < 18.5:
    print(f'Você está ABAIXO do peso nomal!')
elif 18.5 >= imc > 25:
    print(f'Você está no peso IDEAL!')
elif 25 >= imc > 30:
    print(f'Você está em SOBREPESO!')
elif 30 >= imc > 40:
    print(f'Você está em OBESIDADE! Cuidado!')
else:
    print(f'Você está em OBESIDADE MÓRBIDA. Procure o médico!')