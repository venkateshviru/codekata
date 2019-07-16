l = []
l = input().split()
day = ["monday","tuesday","wednesday","thursday","friday"]
for i in range(len(l)):
    if l[i] in day:
        print("no")
    else:
        print("yes")
