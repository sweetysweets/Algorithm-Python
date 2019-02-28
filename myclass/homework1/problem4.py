"""
汉诺塔
Description

汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。


Input

输入的第一行为N。


Output

移动步数。


Sample Input 1

2
Sample Output 1

8

"""

import sys


# ----------Stack_base_on_list-----------
class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        if self.is_empty():
            raise ValueError('stack 为空')
        else:
            data = self._stack[-1]
            self._stack.pop()
        return data

    def is_empty(self):
        return self.size() == 0

    def show_stack(self):
        return "Stack:(%s)" % self._stack

    def size(self):
        return len(self._stack)

    def top(self):
        return self._stack[-1]


from enum import Enum, unique


@unique
class Action(Enum):
    No = 0
    LToM = 1
    MToL = 2  # ValueError: duplicate values found in <enum 'Color'>: blue -> red
    MToR = 3
    RToM = 4


class Solution:
    record = Action.No  # 上一步操作，全局的

    def hanoi(self, num):
        """
        :type num: int

        """
        step = 0
        left = Stack()
        middle = Stack()
        right = Stack()

        left.push(sys.maxsize)
        middle.push(sys.maxsize)
        right.push(sys.maxsize)

        for i in range(num, 0, -1):  # 包括0，不包括num
            left.push(i)

        while right.size() < num+1:
            step += self.move(Action.MToL, Action.LToM, left, middle, 'left', 'middle')
            step += self.move(Action.LToM, Action.MToL, middle, left, 'middle', 'left')
            step += self.move(Action.MToR, Action.RToM, right, middle, 'right', 'middle')
            step += self.move(Action.RToM, Action.MToR, middle, right, 'middle', 'right')
        return step

    def move(self, action_pre, action_now, from_stack, to_stack, from_str, to_str):

        if self.record != action_pre and from_stack.top() < to_stack.top():
            to_stack.push(from_stack.pop())

            print("Move " + str(to_stack.top()) + " " + from_str + "->" + to_str)
            self.record = action_now
            return 1
        return 0

    def hanoi_recursion(self, n, a, b, c , from_where, to_where):
        if n < 1:
            return 0
        # 如果只有一个盘子
        if n == 1:  # 递归的收敛条件,当n为1,时,执行移动的操作
            # 并且其中一个端点是中间的情况只需走一步
            if from_where == b or to_where == b:
                print("Move 1 from "+from_where +" to "+to_where)
                return 1
            else:
            # 不过中点需要走两步
                print("Move 1 from " +from_where+" to " + b)
                print("Move 1 from " + b + " to " + to_where);
                return 2
        # n个盘子的时候并且其中一个端点在中间的情况有三大步骤
        if from_where == b or to_where == b:
            # another表示左端或者右端 来保证定有从左到右
            another = c if from_where == a or to_where == a else a
            # part1指n - 1从左到右走的步数
            part1 = self.hanoi_recursion(n - 1, a, b, c, from_where, another) # n - 1从左到中（或者从右到中）
            # part2指n号盘走的一步
            part2 = 1
            print("Move" + str(n) + " from " +from_where+" to " + to_where)
            part3 = self.hanoi_recursion(n - 1, a, b, c, another, to_where)# n盘移动到中间后n - 1重新返回中
            return part1 + part2 + part3 # 返回所有的步数
        else:
            # 其中没有端点在中点上，即要么从左到右 要么从右到左
            part1 = self.hanoi_recursion(n - 1, a, b, c, from_where, to_where)  # n - 1从左到右
            part2 = 1 # 底盘从左到中间
            print("Move" + str(n) + " from " +from_where+" to " + b)
            part3 = self.hanoi_recursion(n - 1, a, b, c, to_where, from_where) # n - 1从右回到左边
            part4 = 1 # 底盘从中间走到右盘
            print("Move" + str(n) + " from " + b + " to " + to_where)
            part5 = self.hanoi_recursion(n - 1, a, b, c, from_where, to_where)# n - 1从左边再到右边
            return part1 + part2 + part3 + part4 + part5


if __name__ == '__main__':
    S = Solution()
    k = int(sys.stdin.readline())
    # print(S.hanoi(k))
    # print(S.hanoi_recursion(k, 'left', 'middle', 'right', 'left', 'right'))
    result = 3 ** k - 1
    print(result)
"""
 
　　上一篇用的是递归的方法解决这个问题，这里我们用栈来模拟汉诺塔的三个塔，也就是不用递归的方法 
　　原理是这样的：修改后的汉诺塔问题不能让任何塔从左直接移动到右，也不能从右直接移动到左，而是要经过中间，也就是说，实际上能做的动作，只有四个：左->中，中->左，中->右，右->中 
　　用栈来模拟汉诺塔的移动，其实就是某一个栈弹出栈顶元素，压入到另一个栈中，作为另一个栈的栈顶，理解了这个就好说了，对于这个问题，有两个原则： 
　　一：小压大原则，也就是，要压入的元素值不能大于要压入的栈的栈顶的元素值，这也是汉诺塔的基本规则 
　　二：相邻不可逆原则，也就是，我上一步的操作如果是左->中，那么下一步的操作一定不是中->左，否则就相当于是移过去又移回来
　　有了这两个原则，就可以推导出两个非常有用的结论：
　　1、游戏的第一个动作一定是L->M 
　　2、在走出最小步数过程中的任何时刻，四个动作中只有一个动作不违反小压大和相邻不可逆原则，另外三个动作一定都会违反
【代码实现】

import java.util.Stack;
class Demo{
  public enum Action{
    No,LToM,MToL,MToR,RToM
  }

  //num是盘子的数量，left，mid，right分别代表左中右三个柱子
  public static int hanoi(int num,String left,String mid,String right){
    //lS,mS,rS代表左中右三个栈（模拟柱子）
    Stack<Integer> lS = new Stack<Integer>();
    Stack<Integer> mS = new Stack<Integer>();
    Stack<Integer> rS = new Stack<Integer>();
    lS.push(Integer.MAX_VALUE);
    mS.push(Integer.MAX_VALUE);
    rS.push(Integer.MAX_VALUE);
    for(int i=num;i>0;i--){
      lS.push(i);
    }
    Action[] record = { Action.No };
    int step = 0;
    while(rS.size() != num+1){
      step += fStackToStack(record,Action.MToL,Action.LToM,lS,mS,left,mid);
      step += fStackToStack(record,Action.LToM,Action.MToL,mS,lS,mid,left);
      step += fStackToStack(record,Action.MToR,Action.RToM,rS,mS,right,mid);
      step += fStackToStack(record,Action.RToM,Action.MToR,mS,rS,mid,right);
    }
    return step;
  }

  //preNoAct是与现在所要进行的动作相反的动作，nowAct是现在所要进行的动作
  public static int fStackToStack(Action[] record,Action preNoAct,Action nowAct,Stack<Integer> fStack,Stack<Integer> tStack,String from,String to){
    if(record[0] != preNoAct && fStack.peek() < tStack.peek()){
      tStack.push(fStack.pop());
      System.out.println("Move " + tStack.peek() + " " + from + "->" + to);
      record[0] = nowAct;
      return 1;
    }
    return 0;
  }

  public static void main(String[] args){
    int i = hanoi(3,"left","mid","right");
    System.out.println("一共走了" + i + "步");
  }
}
"""

