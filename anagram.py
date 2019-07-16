n = int(input())
arr = []
for i in range(0,n):
    a = input()
    arr.append(a)
string = "kabali"
count = 0
for i in range(len(arr)):
    if(sorted(arr[i])==sorted(string)):
        count += 1
print(count)
