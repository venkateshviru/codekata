from itertools import permutations
n = input()
l = list(n)
l1 = ["".join(map(str,i)) for i in permutations(l)]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
for i in range(len(l2)):
    print(l2[i])

