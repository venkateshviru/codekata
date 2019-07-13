n = int(input())
l1 = []
l2 = []
l1 = input().split()
x = len(l1)
for i in range(0,x):
    l1[i] = int(l1[i])
    if(l1[i]==i):
        l2.append(i)
if(len(l2)==0):
    print("-1")
else:
    print(*l2, sep=" ")
