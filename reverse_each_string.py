l = []
l = input().split()
l1 = []
for i in range(len(l)):
    s = l[i]
    a = s[::-1]
    l1.append(a)
print(*l1, sep=" ")
