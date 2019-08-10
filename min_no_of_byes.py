n = int(input())
sqrt = []
res = []
for i in range(1,n+1):
    sqrt.append(2**i)
for i in range(len(sqrt)):
    sqrt[i] = n - sqrt[i]
    if sqrt[i] >= 0:
        res.append(sqrt[i])
print(min(res))
