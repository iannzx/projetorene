#operadores logistico (AND)
curso_on = input('Fez curso online? ')
psico = input('Passou no psicotecnico? ')
tox = input('O exame apontou algo ilicito? ')
pratica = input('Passou na pratica? ')

if curso_on == 'sim' and psico == 'sim' and tox == 'não' and pratica == 'sim':
    print('Aprovado!')
else:
    print('Você foi reprovado!')