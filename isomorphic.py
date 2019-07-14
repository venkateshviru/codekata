maxi = 256
def main(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False
    marked = [False] * maxi
    map = [-1] * maxi
    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True
s = input()
s1 = input()
res = []
if(main(s,s1)==True):
    print("yes")
else:
    print("no")
