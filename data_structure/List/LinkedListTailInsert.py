# 尾插法实现链表
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListTailInsert:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, value):
        # 尾插法：在链表尾部插入新节点
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        # 打印链表元素
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# 示例用法
if __name__ == '__main__':
    linked_list = LinkedListTailInsert()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    
    linked_list.display()
