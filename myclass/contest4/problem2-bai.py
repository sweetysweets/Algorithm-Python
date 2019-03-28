def maxsum(a):
    min=a[0]
    sum=0
    for i in a:
        sum+=i
        if i<min:
            min=i
    if min<0:
        sum=sum-min
    return sum

def maxsub(a):
    max_sum = a[0]
    l=len(a)
    start=0
    sum=0
    for i in range(l):
        if sum < 0:
            sum = a[i]
            start=i
        else:
            sum += i
            sum=maxsum(a[start:i+1])
        if sum > max_sum:
            max_sum =  sum
    return max_sum

k=int(input())
for i in range(0,k):
    arr=[]
    lenth=int(input())
    line=input().split(" ")
    for j in line:
        arr.append(int(j))
    print(maxsub(arr))
