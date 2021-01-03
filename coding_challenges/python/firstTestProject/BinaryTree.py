class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):
        if self!=None:
            print(self.get_root_val())
            if(self.get_left_child()!=None):
                self.get_left_child().preorder()
            if(self.get_right_child()!=None):
                self.get_right_child().preorder()

    def postorder(self):
        if self!=None:
            if(self.get_left_child()!=None):
                self.get_left_child().postorder()
            if(self.get_right_child()!=None):
                self.get_right_child().postorder()
            print(self.get_root_val())

    def inoder(self):
        if self!=None:
            if(self.get_left_child()!=None):
                self.get_left_child().postorder()
            print(self.get_root_val())
            if(self.get_right_child()!=None):
                self.get_right_child().postorder()

    def __str__(self):
        str_val = ""
        if self:
            str_val = '(' + str(self.get_left_child()) + ' '
            str_val = str_val + str(self.get_root_val()) + ' '
            str_val = str_val + str(self.get_right_child()) + ')'
        return str_val
