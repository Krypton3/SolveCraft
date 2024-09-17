'''
Write a program to count how many bigger element in the list from the current
position to the left.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.right_count = 0
        self.left = None
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return 0
        return self.node_insert(self.root, val)

    def node_insert(self, node, val):
        count = 0
        while node:
            if val < node.val:
                count += node.count + node.right_count
                if node.right:
                    node = node.right
                else:
                    node.right = Node(val)
                    return count
            elif val > node.val:
                node.right_count += 1
                if node.left:
                    node = node.left
                else:
                    node.left = Node(val)
                    return count
            else:
                count += node.right_count
                node.count += 1
                return count


arr = [3, 6, 2, 8, 10, 8, 1]
bst = BT()
result = [0] * len(arr)
for i in range(len(arr)):
    result[i] = bst.insert(arr[i])
print(result)
