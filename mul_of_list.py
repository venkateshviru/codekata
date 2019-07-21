import numpy
n = int(input())
l = []
arr = []
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
for i in l:
    a = numpy.prod(l)/i
    a = int(a)
    arr.append(a)
print(*arr, sep=" ")

