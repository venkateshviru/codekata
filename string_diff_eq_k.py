l = []
l1 = []
l2 = []
l3 = []
l = input().split()
l1 = list(l[0])
l2 = list(l[1])
k = int(l[2])
n = len(l1)
for i in range(n):
    if(l1[i]!=l2[i]):
        l3.append(l2[i])
if len(l3)==k:
    print("yes")
else:
    print("no")
