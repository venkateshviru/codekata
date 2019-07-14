s = []
s = input().split()
s1 = list(s[0])
s2 = list(s[1])
count=0
x1 = len(s1)
x2 = len(s2)
if(x1!=x2):
    print("no")
else:
    for i in range(x1):
        if(s1[i]!=s2[i]):
            count += 1
    if(count==1):
        print("yes")
    else:
        print("no")
