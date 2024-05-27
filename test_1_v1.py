# Так как входные данные не указанны, я возьму определнные последовательности целых чисел
a = [1, 2, 3, 4, 5, 600]
b = [1, 4, 6, 8, 11, 12, 15]
res = []
x, y = None, None

while a and b:
    if a and x == None:
        x = a.pop()
    if b and y == None:
        y = b.pop()

    if x >= y:
        res.append(x)
        x = None
    else:
        res.append(y)
        y = None
if a:
    for i in a[::-1]:
        res.append(i)
if b:
    for i in b[::-1]:
        res.append(i)
print(res)


