n=int(input())
k=int(input())
arr = []
for i in range(0, n):
    x = int(input())
    arr.append(x)
a = 0
for i in range(0, k):
    a += arr[i]
print(a)
