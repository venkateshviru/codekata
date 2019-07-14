l = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
l1 = []
l2 = []
l1 = input().split()
l2 = input().split()
for i in range(len(l1)):
    l1[i] = int(l1[i])
for i in range(len(l2)):
    l2[i] = int(l2[i])
count = 0
if(all(x in l1 for x in l2)):
    count = 1
if(count):
    print("YES")
else:
    print("NO")
