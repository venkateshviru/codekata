n = int(input())
binary = [1,2,4,8,16,32]
b = 0
for i in range(n):
    b += binary[i]
bi = []
for i in range(1,b+1):
    bi.append(str(bin(i).replace('0b','')))
for i in range(len(bi)):
    a = n - len(list(bi[i]))
    if a != 0:
        bi[i] = (a*'0') + bi[i]
for i in bi:
    print(i)
