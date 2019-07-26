n=int(input())
l=[]
res=[]
l=input().split()
for i in range(len(l)):
	l[i] = int(l[i])
for i in range(len(l)):
	k=i+1
	for j in range(0,k):
		if l[i]==l[j]:
			break
		else:
			 s=l[i]+l[j]
			 res.append(s)
print(max(res))
