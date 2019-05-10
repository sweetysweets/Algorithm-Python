def getResult(inputs, n):
    result = []
    for i in range(n):
        tmp = inputs[i]
        if tmp is None or len(tmp.strip()) == 0:
            continue
        i = 0
        while i<len(tmp):
            tmp_item = tmp[i:i+8]
            for _ in range(8-len(tmp_item)):
                tmp_item+='0'
            result.append(tmp_item)
            i = i+8
    return result



if __name__ == '__main__':
    inputs = input().strip().split()
    n = int(inputs.pop(0))
    res = getResult(inputs,n)
    res.sort()
    print(" ".join(res))
