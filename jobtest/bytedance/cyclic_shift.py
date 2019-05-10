"""

https://blog.csdn.net/whiterbear/article/details/44521195


"""

"""
排序数组循环移位后查找
题目：
请完成以下算法，给定一个循环有序的数组，在这个数组中找到指定元素，找到的话返回下标，没有找到返回-1。
该数据的特点是它是一个单调递增的数组向右循环移位形成的。
举例说明，原数组是[4, 8, 13, 20, 23, 34, 41, 52]经过向右循环移位后形成的数组可能是[23, 34, 41, 52, 4, 8, 13, 20]，也可能是[4, 8, 13, 20, 23, 34, 41, 52]

第一行输入数组的长度
第二行是数组的元素，用空格隔开
第三行是想要查找的元素
样例输入
7
1 3 5 6 8 10 20
19
样例输出
-1


"""


def my_look_up(list, size, target):
    left = 0
    right = size - 1
    while not left > right:
        mid = int((left + right) / 2)
        if list[mid] == target:
            return mid
        elif list[left] == target:
            return left
        elif list[right] == target:
            return right
        else:
            if list[left] <= list[mid]:  ### 有序，一定有一个区间是有序的
                if list[left] < target < list[mid]:
                    left += 1
                    right = mid - 1
                else:
                    left = mid + 1
                    right -= 1
            else:
                # if list[left] < target or list[mid] > target:
                if list[mid] < target < list[right]:
                    left = mid + 1
                    right -= 1
                else:
                    left += 1
                    right = mid - 1

    return -1
