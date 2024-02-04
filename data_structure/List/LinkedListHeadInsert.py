# 头插法实现链表
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListHeadInsert:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        # 头插法：在链表头部插入新节点
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        # 打印链表元素
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# 示例用法
if __name__ == '__main__':
    linked_list = LinkedListHeadInsert()
    linked_list.insert_at_head(3)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(1)
    
    linked_list.display()
