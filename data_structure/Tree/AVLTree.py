# AVL树
from BinarySearchTree import BinarySearchTree, TreeNode
class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    
    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
    
    # 左旋
    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1\
            - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1\
            + max(rotRoot.balanceFactor, 0)
    
    # 实现再平衡，先右旋，再左旋
    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
    
    def delete(self, value):
        if self.root:
            self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.leftChild = self._delete_node(node.leftChild, value)
        elif value > node.value:
            node.rightChild = self._delete_node(node.rightChild, value)
        else:
            # 要删除的节点是叶子节点或只有一个子节点
            if not node.leftChild and not node.rightChild:
                node = None
            elif not node.leftChild:
                node = node.rightChild
            elif not node.rightChild:
                node = node.leftChild
            else:
                # 要删除的节点有两个子节点
                successor = self._find_successor(node.rightChild)
                node.key = successor.key
                node.value = successor.value
                node.rightChild = self._delete_node(node.rightChild,
                                                    successor.value)

        if not node:
            return node

        node.update_height()
        node.update_balance_factor()

        balanceFactor = node.balanceFactor

        # 左子树比右子树更重
        if balanceFactor > 1:
            if node.leftChild.balanceFactor >= 0:
                node = self.rotateRight(node)
            else:
                node.leftChild = self.rotateLeft(node.leftChild)
                node = self.rotateRight(node)
        # 右子树比左子树更重
        elif balanceFactor < -1:
            if node.rightChild.balanceFactor <= 0:
                node = self.rotateLeft(node)
            else:
                node.rightChild = self.rotateRight(node.rightChild)
                node = self.rotateLeft(node)

        return node

    def _find_successor(self, node):
        while node.leftChild:
            node = node.leftChild
        return node
