# Если допустить, что входные данные последовательность целых чисел
a = map(int, input().split())
b = map(int, input().split())
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