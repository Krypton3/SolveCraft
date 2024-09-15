'''
Write a program to count how many bigger element in the list from the current
position to the left.
'''


def biggerElementLeft(arr):
    n = len(arr)
    if n <= 1:
        return [0]

    res = [0] * n
    stack = []

    for i in range(n):
        count = 0
        for index in stack:
            if arr[index] > arr[i]:
                count += 1
        res[i] = count

        # Push the current index onto the stack
        stack.append(i)
    return res


arr1 = [3, 4, 9, 6, 1]
print(biggerElementLeft(arr1))

# arr2 = [5, 2, 6, 1]
# print(biggerElementLeft(arr2))


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 1  # Number of times this value has appeared
        self.left = None
        self.right = None
        self.right_count = 0  # Number of nodes in the right subtree


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Insert the value into the BST, and return how many elements are
        greater than the current value
        in the BST so far.
        """
        if not self.root:
            self.root = TreeNode(val)
            return 0

        return self._insert(self.root, val)

    def _insert(self, node, val):
        count = 0
        while node:
            if val > node.val:
                # Go to the right subtree and count the current node and left
                # subtree
                count += node.count + node.right_count
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return count
            elif val < node.val:
                # Go to the left subtree
                # Increment right count as we're addinga new node to the left
                node.right_count += 1
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return count
            else:
                # If the value is equal, just update the count of the current
                # node
                count += node.right_count
                node.count += 1
                return count


def count_greater_elements(arr):
    bst = BST()
    n = len(arr)
    result = [0] * n

    # Traverse the array and insert elements into the BST
    for i in range(n):
        result[i] = bst.insert(arr[i])

    return result


# Test cases
arr1 = [3, 4, 9, 6, 1]
print(count_greater_elements(arr1))  # Expected output: [0, 0, 0, 1, 4]

arr2 = [5, 2, 6, 1]
print(count_greater_elements(arr2))  # Expected output: [0, 1, 0, 3]
