
def get_MinDvalue(a,b):
    # combinations是一个生成器（迭代器），每次从a+b中取出n个数返回一个列表，并且会列举出所有种情况
    # 这个列表的和与sum(a+b)/2差值的绝对值的最小值就是题目要求的最小差值
    return min(combinations(a+b, len(a+b)/2), key=lambda x:abs(sum(x)-sum(a+b)/2))

def combinations(numbers, length, num=0, begin=0):
# nums用于表示当前以及取出了多个数字了
# begin用来表示迭代中for循环的起点序列
    for i in range(begin,len(numbers)):
        if num == length-1:
            yield [numbers[i]]
        for result in combinations(numbers, length, num+1, begin=i++1):
            yield [numbers[i]] + result
