class Node:
    def __init__(self,v):
        self.val = v
        self.next = None

    def set_next(self,next):
        self.next = next


def get_length(node):
    if node is None:
        return 0

    p = node
    q = node

    while p.next is not None and q.next is not None and q.next.next is not None:
        p = p.next
        q = q.next.next
        if p == q:
            break

    if p!=q or p == node :  ##无环
        return 0

    length = 1
    q = p.next
    while q!=p:
        q = q.next
        length += 1

    return length


if __name__ == '__main__':
    pass