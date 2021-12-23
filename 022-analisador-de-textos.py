nome = str(input("Digite um nome: ")).strip()

print("Nome em letras maíusculas: {}".format(nome.upper()))

print("Nome em letras minúsculas: {}".format(nome.lower()))

print("Nome ao todo tem: {} letras".format(len(nome)- nome.count(' ')))

#print("Primeiro nome tem {} letras".format(nome.find(' ')))

nomesepara = nome.split()

print("Primeiro nome {} com {} letras".format(nomesepara[0], len(nomesepara[0])))
