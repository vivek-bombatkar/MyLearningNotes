

class A:
    def __init__(self,a: int = None,b: str = None,c: []= None):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

class B(A):
    def __init__(self,d: float = None):
        self.d = d
    def get_d(self):
        return self.d

class D():
    def __init__(self,e: B= None):
        self.obj_b = B()
    def get_B_d(self):
        return self.obj_b.get_d()


class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

if __name__=='__main__':
    obj_A = A()
    print(obj_A.a)
    obj_A.a = 10
    print(obj_A.a)

    obj_B = B()
    obj_B.d = 20.11
    obj_B.a = 100
    print((obj_B.d, obj_B.a))
    print(obj_A.a)

    node1 = Node(11)
    node2 = Node(22)
    node3 = Node(33)
    node1.next = node2
    node2.next = node3
    while node1:
        print(node1.val)
        node1 = node1.next

    obj_D = D()
    obj_D.d = 111
    print(obj_D.get_B_d())