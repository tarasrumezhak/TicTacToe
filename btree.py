class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def __iter__(self):
        for i in [self.left_child, self.right_child]:
            yield i

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left_child), self.height(node.right_child)) + 1


if __name__ == '__main__':
    root = LinkedBinaryTree("2")
    root.right_child = LinkedBinaryTree("3")
    node1 = root.right_child
    node1.insert_left(LinkedBinaryTree("4"))
    node2 = node1.left_child
    print(root.height(root))
