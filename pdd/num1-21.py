
"""

老师在1-21中选择两个不同的数字，把两数之和告诉小明，把两数之积告诉小刚，
然后问小明：“你知道是哪两个数字了吗？”小明说:"不知道。"
老师同样的问题问小刚，小刚也不知道。然后小明说:“我知道了。”小刚说:“我也知道了。”
问:两个数分别是多少？
"""
sum_dict = {}
mulit_dict = {}

sum_count = {}
mulit_count={}

first_sum = {}
forst_mulit = {}

result = []
result2= []
def init():
    for i in range(1,22):
        for j in range(i+1,22):
            sum_dict[(i,j)] = i+j
            mulit_dict[(i,j)] = i*j
def first():
    for key,value in sum_dict.items():
        count = sum_count.setdefault(value,0)
        sum_count[value] = count+1
    for key,value in mulit_dict.items():
        count = mulit_count.setdefault(value,0)
        mulit_count[value] = count+1
    for key,value in sum_count.items():
        if value!=1:
            first_sum[key] = value
    for key,value in mulit_count.items():
        if value!=1:
            forst_mulit[key] = value


def second():
    # print(first_sum)
    # print(mulit_count)
    for key,value in first_sum.items():
        sum_tmp = [k for k, v in sum_dict.items() if v == key]
        for (a,b) in sum_tmp:
            # print(a,b,end=" ")
            key = a*b
            if mulit_count[key]!=1:
                result.append((a,b))
            else:
                pass

def third():
    print(sum_count)
    for (a,b) in result:
        mulit_tmp = [k for k, v in mulit_dict.items() if v == a*b]
        # print(mulit_tmp)
        for (a,b) in mulit_tmp:
            key = a+b

            if sum_count[key]!=1:
                result2.append((a,b))
            else:
                pass



if __name__ == '__main__':
    init()
    # print(sum_dict)
    # print(mulit_dict)
    first()

    # print(first_sum)
    # print(forst_mulit)

    second()
    third()
    print(result)
    print(result2)