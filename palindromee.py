l = input()
l1 = []
l1 = list(l)
l2 = []
for i in l1:
    l2.append(i)
l2.reverse()
if(l1==l2):
    print("YES")
else:
    print("NO")
