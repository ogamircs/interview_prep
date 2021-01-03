from BinHeap import BinHeap
from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Binary Tree:")
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_right_child().insert_right('hello')
    print(r)
    print("pre-order:")
    r.preorder()
    print("post-order:")
    r.postorder()
    print("in-order:")
    r.inoder()

    print("Binary Heap:")
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
