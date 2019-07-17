n,q = map(int,input().split())
l = []
l1 = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(q):
    a,b = map(int,input().split())
    res = []
    for i in range(a-1,b):
        s = l[i]
        res.append(s)
    res.sort()
    print(res[0])
