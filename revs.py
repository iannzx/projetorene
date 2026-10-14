num = int(input('Digite um número: '))
resp = input('o número digitado é par? ')

if num % 2 == 0 and resp == 'sim':
    print('Este número é par e você acertou')

if num % 2 == 1 and resp == 'sim':
    print('Este número é impar e você ERROU!')

if num % 2 == 0 and resp == 'não':
    print('Este número é par e você ERROU!')

if num % 2 == 1 and resp == 'não':
    print('Este número é impar e você acertou!')