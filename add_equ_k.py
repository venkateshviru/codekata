a,b = map(int,input().split())
l = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
count=0
for i in range(len(l)):
    k = i+1
    for j in range(k,len(l)):
        if l[i]+l[j] == b:
            count+=1
if(count>=1):
    print("YES")
else:
    print("NO")

