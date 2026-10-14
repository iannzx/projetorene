




so = ['xp', '7','vista','8','10','11']
campo = input('Qual S.O vc quer mudar? ')
ind = -1
for i in range(len(so)):
    if so[i] == campo:
        ind = i

if ind == -1:
    print('O S.O digitado não está presente na lista')
else:
    novo = input('Digite o S.O que vai substituir: ')
    so[ind] = novo
    print(so)