arr = []
arr = input().split()
n = int(arr[0])
k = int(arr[1])
l = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
print(l[-k])
