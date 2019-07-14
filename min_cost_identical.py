l = []
l1 = []
l2 = []
l3 = []
l = input().split()
l1 = list(l[0])
l2 = list(l[1])
n1 = len(l1)
n2 = len(l2)
n = n2 - n1
for i in range(n1):
    if(l1[i]!=l2[i]):
        l3.append(l2[i])
res = len(l3)+n
print(res)
