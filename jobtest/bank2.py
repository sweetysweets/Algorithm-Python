
def getTotal(n,w,ai):
    global result
    man = ai[n-1]
    tmp = [i for i in range(man+1)]
    binary(tmp,0,man,w,ai)
    return result

result = 0

w = 0
ai = []
def binary(list,begin,end):
    global result,w,ai
    if begin == end:
        man = list[begin-1]
        female = man/2
        tmp = (man + female) * n
        if tmp <= w:
            if result < tmp:
                result = tmp
    if begin < end:
        mid = (begin + end) // 2
        man = list[mid]
        female = list[mid] / 2
        if ai[n] >= female:
            tmp = (man + female) * n
            if tmp > w:
                binary(list[0:mid+1],0,mid,w,ai)
            elif tmp<w:
                if result<tmp:
                    result = tmp
                binary(list[mid+1:end+1], 0, end-mid-1,w,ai)




if __name__ == '__main__':
    strs = input().split()
    n = int(strs[0])
    w = int(strs[1])
    strs = input().split()
    ai = [0 for i in range(2*n)]

    for i in range(n*2):
        ai[i] = int(strs[i])
    ai = sorted(ai,reverse=True)
    print("%.6f"%getTotal(n,w,ai))



