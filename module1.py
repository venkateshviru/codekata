def main():
    n=int(input())
    l=[]
    l=list(input().split())
    l.sort()
    size = len(l)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if l[i] == l[j] and l[i] not in repeated:
                repeated.append(l[i])
    if(len(repeated)==0):
        print("unique")
    else:
        for i in range (0,len(repeated)):
            print(repeated[i])



if __name__ == '__main__':
    main()
