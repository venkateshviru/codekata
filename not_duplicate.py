n = int(input())
l1 = []
l2 = []
l3 = []
l1 = input().split()
x = len(l1)
for i in range(x):
    k = i+1
    for j in range(k,x):
        if l1[i]==l1[j] and l1[i] not in l2:
            l2.append(l1[i])
for i in range(len(l1)):
    if l1[i] not in l2:
        l3.append(l1[i])
print(*l3, sep=" ")
