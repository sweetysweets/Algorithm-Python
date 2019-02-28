


if __name__ == '__main__':
    n = 10 ** 5
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    temp = []

    for i in range(2, n + 1):
        if prime[i]:
            temp.append(i)

    t = int(input())
    for _ in range(t):
        m = int(input())
        cnt = 0
        i = 0
        while i < len(temp):
            j = i + 1
            if pow(temp[i] * temp[j], 2) > m:
                break
            while j < len(temp):
                if pow(temp[i] * temp[j], 2) > m:
                    break
                j += 1
                cnt += 1
            i += 1

        i = 0
        while temp[i] < 28:
            if pow(temp[i], 8) > m:
                break
            cnt += 1
            i += 1
        print(cnt)
