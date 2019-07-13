n = int(input())
l1 = []
l2 = []
l1 = input().split()
x = len(l1)
for i in range(x):
    k = i+1
    for j in range(k,x):
        if l1[i]==l1[j] and l1[i] not in l2:
            l2.append(l1[i])
if(len(l2)==0):
    print("unique")
else:
    print(l2[0])
