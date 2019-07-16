l = []
l = input().split()
l1 = []
l1 = list(l[0])
for i in range(len(l1)):
    l1[i] = int(l1[i])
res = 0
for i in range(len(l1)):
    res += l1[i]**2
print(res)
