n=int(input())
a=list(map(int,(input().split())))
for i in range(n):
    l = i+1
    for j in range(l,n):
        for k in range(n):
                if a[i]+a[j]==a[k]:
                    if i<j<k:
                        print(a[i],a[j],a[k])
