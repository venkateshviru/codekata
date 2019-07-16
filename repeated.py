n = int(input())
l1 = []
l1 = input().split()
l2 = []
l3 = []
for i in range(len(l1)):
    k = i+1
    for j in range(k,len(l1)):
        if l1[i] == l1[j] and l1[i] not in l2:
            l2.append(l1[i])
for i in l1:
    if i not in l2:
        l3.append(i)
print(*l3)
