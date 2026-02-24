class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def search(self, data):
        curr = self.head

        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next

        return None

    def min(self):
        if self.head is None:
            return None

        min_node = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data < min_node.data:
                min_node = curr
            curr = curr.next

        return min_node

    def find_max(self):
        if self.head is None:
            return None

        max_node = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data > max_node.data:
                max_node = curr
            curr = curr.next

        return max_node

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev