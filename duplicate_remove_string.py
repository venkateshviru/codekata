l = input()
l1 = []
l2 = []
l1 = list(l)
for i in l1:
    if i not in l2:
        l2.append(i)
print(*l2, sep="")
