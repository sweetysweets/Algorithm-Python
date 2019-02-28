"""
链表区间逆序
Description

将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。


Output

输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。


Sample Input 1

8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
Sample Output 1

3 2 1 6 5 4 7 8
d c b a h g f e
"""
from sys import stdin


class ListNode:
    def __init__(self, x, next=None):
        self.next = next
        self.val = x


class Solution:

    # def reverse2(self, head, left, right):
    #     pre = None
    #     start = head
    #     while head != right:
    #         next = head.next
    #         head.next = pre
    #         pre = head
    #         head = next
    #     if left is not None:
    #         left.next = pre
    #     start.next = right

    def reverse(self, head, left, right):  # left保存上一段的最后一个，right保存下一段的第一个
        pre = None                   # 三个指针，pre，head，next 循环指向下一个，每次只调整一个指针
        start = head
        while head != right:
            next = head.next
            head.next = pre
            pre = head
            head = next
        if left is not None:
            left.next = pre
        start.next = right

    def reverseKNode2(self, head, k):
        if head is None or head.next is None or k < 2:
            return head
        pre = None
        cur = head
        count = 0
        while cur is not None:
            count += 1
            next = cur.next
            if count == k:
                start = head if pre is None else pre.next
                head = cur if pre is None else head
                self.reverse(start, pre, next)
                pre = start
                count = 0
            cur = next
        return head

    def print_list_node(self, head):
        while head.next is not None:
            print(head.val, end=' ')
            head = head.next
        print(head.val)


if __name__ == '__main__':
    S = Solution()
    for line in stdin:
        # if not line:
        #     break
        # if line == '\n':
        #     break
        arr_str = line.split()   # 注意别写成stdin.readline了，已经循环过一次了

        list_len = int(arr_str[0])
        head = ListNode(arr_str[1])
        p = head
        for i in range(2, len(arr_str) - 1):
            next = ListNode(arr_str[i])
            p.next = next
            p = p.next
        k = int(arr_str[-1])
        result = S.reverseKNode2(head, k)
        S.print_list_node(result)

    # arr_str = [8, '1', '2', '3', '4', '5', '6', '7', '8', 3]
    # list_len = int(arr_str[0])
    # head = ListNode(arr_str[1])
    # p = head
    # for i in range(2, len(arr_str) - 1):
    #     next = ListNode(arr_str[i])
    #     p.next = next
    #     p = p.next
    # k = int(arr_str[-1])
    # result = S.reverseKNode2(head, k)
    # S.print_list_node(result)




"""

【题目】

　　给定一个单链表的头节点head，实现一个调整单链表的函数，使得每K个节点之间逆序，如果最后不够K个节点，则不调整最后的节点。

【基本思路】

　　方法一。时间复杂度O(N)，空间复杂度O(K)。 
　　 
　　利用栈结构，依次遍历链表，将节点压入栈中，栈中节点每凑到k个就将这k个节点进行逆序，然后再连接入链表中。需要注意头节点的更新以及每组节点两头的连接。代码实现如下：


#python3.5
def reverseKNode(head, k):
    def reverse(stack, pre, next):
        while stack:
            cur = stack.pop()
            if pre != None:
                pre.next = cur
            pre = cur
        pre.next = next
        return pre


    if head == None or head.next == None or k < 2:
        return head
    stack = []
    cur = head
    newHead = head
    pre = None
    while cur != None:
        next = cur.next
        stack.append(cur)
        if len(stack) == k:
            pre = reverse(stack, pre, next)
            newHead = cur if newHead == head else newHead
        cur = next
    return newHead
    
    
    　方法二。时间复杂度O(N)，空间复杂度O(1)。

　　不需要利用栈，用变量记录每一组开始的第一个节点和最后一个节点，然后直接逆序调整，把这一组的节点都逆序。需要注意头节点的更新以及每组节点两头的连接。代码实现如下：

def reverseKNode2(head, k):
    def reverse2(head, left, right):
        pre = None
        start = head
        while head != right:
            next = head.next
            head.next = pre
            pre = head
            head = next
        if left != None:
            left.next = pre
        start.next = right

    if head == None or head.next == None or k < 2:
        return head
    pre = None
    cur = head
    count = 0
    while cur != None:
        count += 1
        next = cur.next
        if count == k:
            start = head if pre == None else pre.next
            head = cur if pre == None else head
            reverse2(start, pre, next)
            pre = start
            count = 0
        cur = next
    return head
"""