num = [2, 5, 9]
num.append(7)
num.insert(2, 2)
# num.remove(4)

for c, v in enumerate(num):
    print(v, end = '')
    print(', pos: ', c)