#construa um algoritmo em py que consiga ler 10 numeros
# informados pelo usuario. O codigo deve ao final informar a
#quantidade de numeros pares e impares
# While

par = 0
impar = 0
cont = 1

while cont <= 10:
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        par +=1

    else:
        impar += 1

    cont += 1

print("Quantidade de números pares:", par)
print("Quantidade de números ímpares:", impar)
