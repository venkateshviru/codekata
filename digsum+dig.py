def digit_sum(n):
    sum = 0;
    rem = 0;
    while(n):
        rem = n % 10;
        sum = sum + rem;
        n = int(n / 10);
    return sum;
a = int(input())
count = 0
res = []
for i in range(a + 1):
    if (i + digit_sum(i) == a):
        count +=1
        res.append(i)
print(count)
print(*res)
