num = []
for i in range(14, 56):
    num.append(i)

    print(num)

# exceto no numero 25, sobreescreva os demais pela letra 'a'

for i in range(len(num)):
    if num[i] == 25:
        continue
    num[i] = 'a'