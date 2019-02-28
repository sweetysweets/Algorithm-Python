def binaryFind(arr, target, end):
    low = 0
    high = end
    while low <= high:
        mid = int((low + high) / 2)
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
    return low


def doubleEndLIS(arr):
    length = len(arr)
    dp1 = []
    dp2 = []
    lis = []
    for i in range(0, length):
        dp1.append(0)
        dp2.append(0)
        lis.append(0)

    dp1[0] = 1
    lis[0] = arr[0]
    maxlen = 1
    i = 1
    while i < length:
        pos = binaryFind(lis, arr[i], maxlen - 1)
        lis[pos] = arr[i]
        dp1[i] = pos + 1
        if pos >= maxlen:
            maxlen += 1
        i += 1

    for i in range(0, length):
        lis[i] = 0
    lis[0] = arr[length - 1]
    dp2[length - 1] = 1
    maxlen = 1
    i = length - 2
    while i > -1:
        pos = binaryFind(lis, arr[i], maxlen - 1)
        lis[pos] = arr[i]
        dp2[i] = pos + 1
        if pos >= maxlen:
            maxlen += 1
        i -= 1

    mids = []
    rmax = 0
    for i in range(0, length):
        rmax = max(rmax, dp1[i] + dp2[i])
    for i in range(0, length):
        if rmax == dp1[i] + dp2[i]:
            mids.append(i)

    results = []
    for mid in mids:
        lis = []
        curlen = dp1[mid]
        i = mid
        while i >= 0:
            if dp1[i] == curlen:
                lis.insert(0, arr[i])
                curlen -= 1
                if curlen == 0:
                    break
            i -= 1
        curlen = dp2[mid] - 1
        i = mid + 1
        while i < length:
            if dp2[i] == curlen:
                lis.append(arr[i])
                curlen -= 1
                if curlen == 0:
                    break
            i += 1
        results.append(' '.join(str(num) for num in lis))

    return results


def solve(arr):
    return doubleEndLIS(arr)

if __name__ == '__main__':

    arr = input().split()
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    results = solve(arr)
    for result in results:
        print(result)
