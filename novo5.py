#desenvlva um algoritmo em py que faça a leitura do numero
# dos candidatos (99,88). leia a votaçao para uma turma de 38 alunos
#no final, compute os votos e diga quem ganhou

v99 = 0
v88 = 0
aluno = 1

while aluno <= 7:
    voto = int(input("Voto: "))

    if voto == 99:
        v99 += 1
    elif voto == 88:
        v88 += 1

    aluno += 1

print("99:", v99)
print("88:", v88)

if v99 > v88:
    print("Ganhou o 99")    
elif v88 > v99:
    print("Ganhou o 88")
else:
    print("Empate")