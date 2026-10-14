nota = float(input('Digite a nota: '))
freq = float(input('Digite a frequência: '))

if (nota >= 7 and freq >= 75) or (nota >= 6 and freq == 100):
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')