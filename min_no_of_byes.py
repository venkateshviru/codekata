def main(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    mid = 0
    if (target >= arr[n - 1]):
        return arr[n - 1]
    while (left < right):
        mid = (left + right)//2
        if (arr[mid] == target):
            return arr[mid]
        if (target < arr[mid]):
            if (mid > 0 and target > arr[mid - 1]):
                return closest(arr[mid - 1], arr[mid], target)
            right = mid
        else:
            if (mid < n - 1 and target < arr[mid + 1]):
                return closest(arr[mid], arr[mid + 1], target)
            left = mid + 1
    return arr[mid]
def closest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1
target = int(input())
arr = []
for i in range(1,20):
    s = 2**i
    arr.append(s)
res = main(arr, target)
final = target - res
print(final)
