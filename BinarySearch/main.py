def binarySearch(l, target, low=None, high=None):
    temp = sort(l)
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binarySearch(l, target, low, midpoint - 1)
    else:
        return binarySearch(l, target, midpoint + 1, high)


def sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l


if __name__ == '__main__':
    l = [1, 10, 6, 88, 9, 12, 455, 33]
    target= 10
    print("Sorted list is {}".format(sort(l)))
    print(" Binary: {} is at {}".format(target,binarySearch(l, target)))
   # print (" Naive search")
