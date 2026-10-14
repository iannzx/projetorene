sim = 0
nao = 0
outro = 0
resp = ''
while resp != "fim":
    resp= input('Vc está gostando de programção')
    if resp == 'sim':
     sim += 1

    elif resp == 'nao':
     nao += 1
    else:
     outro += 1

if sim > nao:
    print('A maioria da sala está gostando de programação?', sim)
elif nao > sim:
  print('Deu ruim')