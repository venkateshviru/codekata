arr = []
arr = input().split()
l1 = []
l1 = list(arr)
l2 = []
for i in l1:
    l2.append(i)
l2.reverse()
if(l1==l2):
    print("YES")
else:
    print("NO")
