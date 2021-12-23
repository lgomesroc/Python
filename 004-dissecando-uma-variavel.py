n = (input('Digite um valor: '))
print(type(n)) #Diz o tipo de primitivo e lembrando que o padrão é string

# n= bool(input('Digite um valor agora: ')) #Aqui mostrará verdadeiro (True) porque foi digitado um valor. Para dar falso (False só apertar enter
#print(n)

print('É número? {}'.format(n.isnumeric())) #o método ísnumeric vai verificar se é possível converter esse valor em um número
print('É letra? {}'.format(n.isalpha()))  # aqui o método is é alfabético, ou seja, só letras. O método is só irá executar se o tipo primitivo or str (string)
print('É alfanúmero? {}'.format(n.isalnum()))  # aqui o método is é alfanuméico, ou seja, letras e números juntos. Outros tipos de string dá F no resultado
print('Éstá tudo em naiúscula? {}'.format(n.isupper()))  # método que verificará se o que digitou está tudo em letras maiúsculas
print('Está tudo em minúscula? {}'.format(n.islower())) # método que veriica se o que digitou está tudo em letras minúsculas
print('Está capializada? {}'.format(n.istitle())) # O Python chama de capitalizada quando tem letras em maiúsculas e minúsculas juntas
print('Pode ser impresso? {}'.format(n.isprintable()))  # se o que digitou pode ser impresso
print('É espaço? {}'.format(n.isspace()))  # se o que digitou é espaço
