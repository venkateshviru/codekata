def prefix(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    result = ""
    j = 0
    i = 0
    while(i <= n1 - 1 and j <= n2 - 1):
        if (str1[i] != str2[j]):
            break
        result += (str1[i])
        i += 1
        j += 1
    return (result)
def main(arr, n):
    arr.sort(reverse = False)
    print(prefix(arr[0], arr[n - 1]))
if __name__ == '__main__':
    a = int(input())
    arr = []
    for i in range(0,a):
        s = input()
        arr.append(s)
    n = len(arr)
    main(arr, n)
