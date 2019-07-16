l = []
l = input().split()
l1 = [list(l[0])]
l2 = [list(l[1])]
k = int(l[2])
res = []
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        res.append(l2[i])
if len(res)==k:
    print("yes")
else:
    print("no")
