if __name__ == '__main__':

    t = int(input())
    for q in range(t):
        s = str(input())
        res = ""
        arr = [0]*26
        for i in range(len(s)):

            arr[ord(s[i])-ord('A')] = 1
        for i in range(1, 26):
            for j in range(25,-1,-1):
                if arr[j] != 0:
                    ss = chr(ord('A')+j)
                    for k in range(j-i,-1,-i):
                        if arr[k] != 0:
                            ss+=chr(ord('A')+k)
                        else:
                            break
                    if len(ss) > len(res):
                        res = ss
        print(res)