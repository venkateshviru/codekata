l = []
l = input().split()
l1 = []
a = int(l[0])
b = int(l[1])
for i in range(1,1000000):
    if i%a==0 and i%b==0:
        l1.append(i)
print(l1[0])
