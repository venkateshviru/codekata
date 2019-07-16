l = []
l = input().split()
l1 = []
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(1,(len(l)-1)):
    if l[i]>l[i+1]:
        s = l[i]
        l1.append(s)
l1.append(l[-1])
print(*l1, sep=" ")
l.sort()
print(l[-1])
