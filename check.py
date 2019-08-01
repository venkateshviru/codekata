n,k=map(int,input().split())
l = list(map(int,input().split()))
count=0
size=len(l)
for i in range(size):
    if k == l[i]:
        count += 1
if count!=0:
    print('yes')
else:
    print('no')
