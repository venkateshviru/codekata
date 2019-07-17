n,k = map(int,input().split())
l = []
l = input().split()
x = len(l)
for i in range(x):
    l[i] = int(l[i])
count = 0
for i in range(x):
    n = i+1
    for j in range(n,x):
        if l[i]+l[j] == k:
            count += 1
if(count>=1):
    print("yes")
else:
    print("no")
