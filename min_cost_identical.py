l = []
l1 = []
l2 = []
l3 = []
l = input().split()
l1 = list(l[0])
l2 = list(l[1])
n1 = len(l1)
n2 = len(l2)
if(n1>n2):
    high = n1
    low = n2
else:
    high = n2
    low = n1
n = high - low
try:
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    for i in range(len(l2)):
        l2[i] = int(l2[i])
    for i in range(low):
        if(l1[i]!=l2[i]):
            l3.append(l2[i])
    res = len(l3) + n
    print(res)
except ValueError:
    for i in range(low):
        if(l1[i]!=l2[i]):
            l3.append(l2[i])
    res = len(l3) + n
    print(res)
