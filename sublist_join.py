k = int(input())
l = []
l1 = []
l2 = []
for i in range(k):
    l = input().split()
    l1.append(l)
res = []
for i in l1:
    res += i
for i in range(len(res)):
    res[i] = int(res[i])
res.sort()
print(res)
