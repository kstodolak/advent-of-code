class CycledList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.prev = self.head
            node.next = self.head
        else:
            current = self.head.prev
            current.next = node
            self.head.prev = node
            node.prev = current
            node.next = self.head

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        del node


    def find(self, value):
        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next
            if current is self.head:
                return None

    def start(self):
        return self.head

    def put_after(self, node, value):
        new_node = Node(value)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        return new_node

    # def move_after(self, node_after, node):

    def put_before(self, node, value):
        new_node = Node(value)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        return new_node

    def from_array(self, input_arr):
        for el in input_arr:
            self.append(el)

    def to_nodes_array(self, reverse=False):
        arr = []
        if not reverse:
            current = self.head
            while current.next is not self.head:
                arr.append(current)
                current = current.next
            return [*arr, current]

        current = self.head.prev
        while current is not self.head:
            arr.append(current)
            current = current.prev
        return [*arr, current]

    def to_array(self, reverse=False):
        return list(map(lambda x: x.value, self.to_nodes_array(reverse)))

    def __repr__(self):
        return str(self.to_array())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.value

    def __str__(self):
        return f"({self.value})"


if __name__ == '__main__':
    clist = CycledList()
    clist.from_array([1, 3, 4, 5])
    clist.put_before(clist.start().next, 2)
    print(clist.to_array())
    print(clist.to_array(reverse=True))
    clist.delete(clist.start())
    print(clist.to_array())
    print(clist.to_array(reverse=True))
    print(clist.start())
    print(clist)
