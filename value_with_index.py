n = int(input())
l = []
l1 = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(len(l)):
    if(l[i]%2==0):
        if(i%2!=0):
            l1.append(l[i])
    else:
        if(i%2==0):
            l1.append(l[i])
print(*l1, sep=" ")
