def main():
    n = []
    n = input().split()
    l = n[0]
    k = n[1]
    l = int(l)
    k = int(k)
    res = []
    for i in range(l,k + 1):
        if i > 1:
             for j in range(2,i):
                 if ((i % j) == 0):
                     break
             else:
                 res.append(i)
    print(*res, sep=" ")

if __name__ == '__main__':
    main()
