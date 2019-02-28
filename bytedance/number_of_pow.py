# 给你一个有序整数数组，数组中的数可以是正数、负数、零，
# 请实现一个函数，这个函数返回一个整数：返回这个数组所有数的平方值中有多少种不同的取值。举例：
# nums = {-1,1,1,1},
# 那么你应该返回的是：1。因为这个数组所有数的平方取值都是1，只有一种取值
# nums = {-1,0,1,2,3}
# 你应该返回4，因为nums数组所有元素的平方值一共4种取值：1,0,4,9
#


# 第一种也是最为直接、简单的思路：把nums数组中所有数的绝对值，全部计算完之后再统计有多少种不同的取值。
def num_of_powers(nums):
    my_set = set()
    for i in nums:
        my_set.add(abs(i))
    return len(my_set)

if __name__ == '__main__':
    print(num_of_powers([-1,0,1,2,3]))
##优化思路：：  看条件，有说有序

def num_of_powers_v2(nums):
    i = 0
    j = len(nums) - 1
    count = 0
    while i <= j:
        num_i = abs(nums[i])
        num_j = abs(nums[j])
        if num_i == num_j:
            count += 1
            while i<=j and abs(nums[i]) == num_i:
                i += 1
            while i<=j and abs(nums[j]) == num_j:
                j -= 1
        elif num_i < num_j:    # -5 6
            count += 1
            while i <= j and abs(nums[j]) == num_j:
                j -= 1
        else:
            count += 1
            while i <= j and abs(nums[i]) == num_i:
                i += 1
