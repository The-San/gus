a = int(input('Введите число:'))
b = format(a, 'b')
c = str(b)
z = 0
for x in c:
    if x == '0':
        z +=1
print(z)
