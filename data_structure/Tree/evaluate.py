# 计算二叉解析树的递归函数
import operator
from data_structure.Stack.Stack1 import Stack
from BinaryTree import BinaryTree
from buildParseTree import buildParseTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


a = buildParseTree('( 3 + ( 4 * 5 ) )')
evaluate(a)
print(evaluate(a))
