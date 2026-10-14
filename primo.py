for num in range (3, 100001):

    qntd = 0
for i in range (2,num):
    if num % i == 0:
        qntd = qntd +1

    if qntd == 0:
        print(num)