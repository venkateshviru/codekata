s = []
s = input()
l = list(s)
x = len(l)
i = 0
while(i<x):
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp
    i +=2
print(*l, sep="")
