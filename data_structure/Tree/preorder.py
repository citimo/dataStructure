# 将前序遍历算法实现为BinaryTree类的方法
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.left.preorder()
    if self.rightChild:
        self.right.preorder()