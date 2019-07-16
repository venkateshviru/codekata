l = []
l = input().split()
day = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
for i in range(len(l)):
    if l[i] in day:
        print("no")
    else:
        print("yes")
