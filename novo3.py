#estrutura de repetição: while = enquanto
soma = 0
i = 0
while i < 5:
    idade = int(input('Digite sua idade: '))
    soma = soma + idade
    i = i+ 1

print('Soma de idade foi ', soma)
media = soma / 5
print('A média de idade foi ', media)