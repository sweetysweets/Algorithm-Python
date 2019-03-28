"""
补全10-1 的式子，判断结果是否是2019

"""
A = [10,9,8,7,6,5,4,3,2,1]
def possible_values(A,start,end):
    result = []
    if start == end -1 :
        result.append((A[start],str(A[start])))
        return result

    for i in range(start+1,end):
        tmp1 = possible_values(A,start,i)
        tmp2 = possible_values(A,i,end)

        for a in tmp1:
            for b in tmp2:
                result.append((a[0]+b[0],'('+a[1]+'+'+b[1]+')'))
                result.append((a[0]-b[0],'('+a[1]+'-'+b[1]+')'))
                result.append((a[0]*b[0],'('+a[1]+'*'+b[1]+')'))
                if b[0]!=0:
                    result.append((a[0] // b[0], '('+a[1]+'/'+b[1]+')'))
        return result

if __name__ == '__main__':
    result = possible_values(A,0,10)
    for (a,b) in result:
        print(a,b)
        if a == 2019:
            print(b)