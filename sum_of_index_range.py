n,q = map(int,input().split())
l = []
l1 = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(q):
    a,b = map(int,input().split())
    res = 0
    for i in range(a-1,b):
        res += l[i]
    print(res)
