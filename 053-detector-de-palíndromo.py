frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso, end=' ')
if junto == inverso:
    print(f'É palíndromo!')
else:
    print(f'Não é palíndromo!')