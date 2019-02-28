"""
链表回文
Description

判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值


Output

是回文则输出true，不是则输出false，一行表示一个链表的结果。


Sample Input 1

3 1 2 1
4 1 2 2 1
3 3 5 3
6 a b c d c a
Sample Output 1

true
true
true
false
"""
from  sys import stdin


class ListNode:
    def __init__(self, x, next=None):
        self.next = next
        self.val = x


class Solution(object):

    def reverse(self, head, left, right):  # left保存上一段的最后一个，right保存下一段的第一个
        pre = None  # 三个指针，pre，head，next 循环指向下一个，每次只调整一个指针
        start = head
        while head != right:
            next = head.next
            head.next = pre
            pre = head
            head = next
        if left is not None:
            left.next = pre
        start.next = right

    def isPalindrome(self, head):
        if head is None:
            return False
        if head.next is None:
            return True
        # 定义两个指针，一快一慢
        quick_pointer = head
        slow_pointer = head

        while quick_pointer is not None and quick_pointer.next is not None: ###注意两个条件缺一不可，对应奇偶个数
            quick_pointer = quick_pointer.next.next
            slow_pointer = slow_pointer.next

        # 倒置右边的
        #   pre cur next 分别是 slow cur next
        cur = slow_pointer.next

        while cur is not None:  # 注意这里是cur ！= null 而不是 pre ！= null
            next = cur.next
            cur.next = slow_pointer
            slow_pointer = cur
            cur = next

        # 比较  这里和slow指针进行比较，而不是quick
        while head != slow_pointer:
            if head.val != slow_pointer.val:
                return False
            else: #####注意偶数时无法走到统一指针
                if head.next == slow_pointer:
                    return True
            head = head.next
            slow_pointer =slow_pointer.next
        return True


if __name__ == '__main__':

    S = Solution()
    # arr_str = [0, '1']


    for line in stdin:
        if not line:
            break
        if line == '\n':
            break
        arr_str = line.split()   # 注意别写成stdin.readline了，已经循环过一次了
        list_len = int(arr_str[0])
        head = ListNode(arr_str[1])
        p = head
        for i in range(2, len(arr_str)):
            next = ListNode(arr_str[i])
            p.next = next
            p = p.next

        if S.isPalindrome(head):
            print("true")
        else:
            print("false")

"""

思路1：空间O(n)整个链表遍历两边， 开一个栈，第一遍遍历把链表中每个元素push进栈中，这样堆中的元素的pop顺序就是链表的倒序输出；第二遍就开始pop栈中数据，每pop一个数据，就把这个数据跟链表中进行对比，如果相同继续往下走，如果不同返回false。
           此种情况下，时间复杂度为O(n)，空间复杂度为O(n)。



/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};*/
class PalindromeList {
public:
    bool chkPalindrome(ListNode* A) {
        if(A==NULL)   return true;
        ListNode* B;
        stack<int> s;
        B=A;
      
        while(B!=NULL)
            {
             s.push(B->val);
             B=B->next;
        }
        
        while(A!=NULL && !s.empty())
            {
            if(A->val==s.top())
                {
                A=A->next;
                s.pop();
            }
            else return false;
        }
       return true;
        // write code here
    }
};


思路2：空间O(1)
（1）使用快慢指针法，第一步设置一个块指针和一个慢指针，快指针一次走两步，慢指针一次走一步（慢），当快指针下一步为null的时候说明慢指针已经走了一半，这就可以找到中间节点。
（2）第二步反转中间链表后面的指针，
（3）第三部从头尾向中间扫描，对比每个元素是否相等，如果都相等，则是回文数，否则不是回文数。（下面网友易水给出了代码实现，这里不再叙述）

/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};*/
class PalindromeList {
public:
    bool chkPalindrome(ListNode* A) {
        if(A==NULL)   return true;
        ListNode* mid;
        ListNode* fast;
        ListNode* temp;
       
            mid=A;
            fast=A;
      
        while(fast->next!=NULL)
             {
             temp=mid;   //temp用来存放最后mid之前的一个元素
             mid=mid->next;
             fast=fast->next;
            if(fast->next!=NULL)
                fast=fast->next;   //循环结束后，当元素个数为奇数时，mid指向中间的元素，当元素个数为偶数时，mid指向后半部分元素的第一个元素。
        }
        if(mid==A)   return true;  //链表元素个数为1时，未执行上述循环；
        ListNode* cur;
 
        temp->next=NULL;     //temp的作用完了，之后temp可以用于其他
        cur=mid->next;
        mid->next=NULL;
        while(cur!=NULL)
            {
            temp=cur->next;      //mid，cur，temp三个指针操作反转链表。
            cur->next=mid;
            mid=cur;
            cur=temp;
        }
        
        while(A!=NULL && mid!=NULL)
            {
            if(A->val==mid->val)
                {
                A=A->next;
                mid=mid->next;
            }
            else return false;
        }
       return true;
        // write code here
    }
};


注意此处：包含元素个数为2的情况，此时mid和fast都指向第二个元素

while(fast->next!=NULL)
             {
             temp=mid;   //temp用来存放最后mid之前的一个元素
             mid=mid->next;
             fast=fast->next;
            if(fast->next!=NULL)
                fast=fast->next;   //循环结束后，当元素个数为奇数时，mid指向中间的元素，当元素个数为偶数时，mid指向后半部分元素的第一个元素。
        }
        
        
        
        
不能简单写成这样：此种情况忽略了元素个数为1和2的特殊情况。
while(fast->next->next!=NULL)
{
    mid=mid->next;
    fast=fast->next->next;
}


"""
