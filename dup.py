def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    if(len(repeated)==0):
        print("unique")
    else:
        for i in range (0,len(repeated)):
            print(repeated[i])
n=int(input())
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
l.sort()
Repeat(l)





