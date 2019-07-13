n = []
n = input().split()
k = n[1]
k = int(k)
arr = []
arr = input().split()
res = []
for i in range(0,k):
    a = arr[i]
    res.append(a)
a = 0
for i in range(len(res)):
    res[i] = int(res[i])
    a += res[i]
print(a)
