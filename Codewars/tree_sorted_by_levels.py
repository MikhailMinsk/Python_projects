# in process... sorry
import inspect
def func(node):
    pass


if __name__ == '__main__':
    class Node:


        def __init__(self, L, R, n):
            self.left = L
            self.right = R
            self.value = n
            self.ret()

        def ret(self):
            print(self.value)
            print(type(Node))
            print(type(self.right))
            print(inspect.isclass(self.right))
            print('________________')
            # print('{} {} {}'.format(type(self.right), type(self.left), self.value))
            return self.value


    # [1, 2, 3, 4, 5, 6]
    node = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
    # print(func(node))
