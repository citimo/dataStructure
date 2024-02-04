# 树的“列表之列表”表示法
def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    r = BinaryTree(3)
    print(r)
    print(insertLeft(r, 4))
    print(insertLeft(r, 5))
    print(insertLeft(r, 6))
    print(insertRight(r, 7))
    print(insertRight(r, 8))
    l = getLeftChild(r)
    print(l)
    t = getRightChild(r)
    print(t)
    setRootVal(l, 9)
    print(r)
    print(insertLeft(l, 11))
    print(r)
    print(getRootVal(r))
    print(getRootVal(l))
    print(getRootVal(t))
