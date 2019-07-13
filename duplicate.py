def repeat(x):
    size = len(x)
    repeated = []
    res = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    if(len(repeated)==0):
        print("unique")
    else:
        for i in range (0,len(repeated)):
            res.append(repeated[i])
            print(*res, sep=" ")
n=int(input())
l = []
l = input().split()
l.sort()
repeat(l)
