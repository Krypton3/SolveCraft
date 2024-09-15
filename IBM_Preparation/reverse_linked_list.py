class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next

    def reverseList(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


arr = [100, 180, 260, 310, 40, 535, 695]
linkedList = LinkedList()

for element in arr:
    linkedList.append(element)

print("before reverse: ")
linkedList.printLinkedList()
print("after reverse: ")
linkedList.reverseList()
linkedList.printLinkedList()
