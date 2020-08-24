class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(node):
    while node:
        print(node.val)
        node = node.next


class AddTwoNumbers:
    def add_two_nums(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        carry = 0
        total = 0
        l3 = ListNode(0)
        head = l3
        while l1 is not None or l2 is not None or carry > 0:
            total = carry
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next

            node = ListNode(total % 10)  # 取余为当前节点数值
            l3.next = node
            l3 = l3.next
            carry = total // 10  # 取整为下一节点进位
        return head.next


if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node21 = ListNode(5)
    node22 = ListNode(6)
    node23 = ListNode(4)
    node21.next = node22
    node22.next = node23
    printList(node1)
    printList(node21)
    l3 = AddTwoNumbers().add_two_nums(node1, node21)
    printList(l3)
