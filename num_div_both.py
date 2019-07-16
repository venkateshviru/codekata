l = []
l = input().split()
l1 =[]
n = int(l[0])
k = int(l[1])
for i in range(1,100000):
    if n%i==0 and k%i==0:
        l1.append(i)
print(l1[-1])
