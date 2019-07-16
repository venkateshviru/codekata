n = int(input())
l = []
l = input().split()
l1 = []
l1 = list(l[0])
l2 = []
vowel = ["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(l1)):
    if l1[i] not in vowel:
        l2.append(l1[i])
l2.reverse()
print(*l2, sep="")
