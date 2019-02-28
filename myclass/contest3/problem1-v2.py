if __name__ == '__main__':

    # flag = 0
    # def perm(n, begin, end):
    #     if begin >= end:
    #         tmp = ''.join(n)
    #         if int(tmp)%17 == 0:
    #             print(tmp)
    #     else:
    #         i = begin
    #         for num in range(begin, end):
    #             n[num], n[i] = n[i], n[num]
    #             perm(n, begin + 1, end)
    #             n[num], n[i] = n[i], n[num]
    #
    #
    # t = input()
    # for _ in range(int(t)):
    #     input_str = input().strip()
    #     n = list(str(input_str))
    #     result = perm(n, 0, len(n))
    #     # print(result if result is not None else 'Not Possible')
    #
    def Swap(n, a, b):
        n[a], n[b] = n[b], n[a]
        return None


    def Reverse(n, begin):
        if len(n) > begin:
            i = begin
            j = len(n) - 1
            while i < j:
                Swap(n, i, j)
                i += 1
                j -= 1
        return n


    def FindMin(n, i):
        j = len(n) - 1
        k = i + 1
        while j > i:
            if n[j] > n[i] and n[j] < n[k]:
                k = j
            j -= 1
        return k


    def FindMax(n, i):
        j = len(n) - 1
        k = i + 1
        while j > i:
            if n[j] < n[i] and n[j] > n[k]:
                k = j
            j -= 1
        return k


    def Permut(n):
        count = 0
        j = len(n) - 1
        if j < 1:
            return None
        else:
            # print(n)

            tmp = ''.join(n)
            if int(tmp)%17 == 0:
                # print(tmp)
                return tmp
            count += 1
            while j >= 1:
                i = j - 1
                if n[i] > n[j]:
                    k = FindMax(n, i)
                    Swap(n, i, k)
                    Reverse(n, j)
                    j = len(n) - 1
                    count += 1
                    # print(n)
                    tmp = ''.join(n)
                    if int(tmp) % 17 == 0:
                        # print(tmp)
                        return tmp
                else:
                    j -= 1
        return None


    t = input()
    for _ in range(int(t)):
        input_str = input().strip()
        n = sorted(list(str(input_str)),reverse=True)
        result = Permut(n)
        print(result if result is not None else 'Not Possible')