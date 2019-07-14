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
s = []
s = input().split()
s1 = s[0]
s2 = s[1]
if(main(s1,s2)==True):
    print("yes")
else:
    print("no")
