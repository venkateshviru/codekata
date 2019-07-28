from itertools import permutations
res = []
a = input()
n = list(a)
l = [''.join(w) for w in permutations(n)]
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(len(l)):
    if l[i]>int(a):
        res.append(l[i])
if(len(res)!=0):
    print(min(res))
else:
    print('impossible')
