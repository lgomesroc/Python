salario = float(input('Digite seu salário: R$ '))
salaux = salario
if salario <= 1250.00:
    salario = salario + (salario * 0.15)
    perc = 15
else:
    salario = salario + (salario * 0.10)
    perc = 10
print("O salário de R${:.2f} foi reajustado para R${:.2f} com {}% de aumento.".format(salaux,salario,perc))