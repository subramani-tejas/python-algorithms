class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head: Node = None, tail: Node = None):
        self.head = None
        self.tail = None
        self.size = 0

    # insert at the head
    def insert_first(self, value):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = self.head

        self.size += + 1

    # insert at the tail
    def insert_last(self, value):
        if not self.tail:
            self.insert_first(value=value)
            return

        new_node = Node(value=value)
        self.tail.next = new_node
        self.tail = new_node

        self.size += + 1

    # insert at index
    def insert_at_index(self, value, index):
        if index == 0:
            self.insert_first(value=value)
            return
        if index == self.size:
            self.insert_last(value=value)
            return

        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node = Node(value=value)
                temp = current.next
                current.next = new_node
                new_node.next = temp
                return
            else:
                current = current.next
                count += 1

    # display llist
    def disp(self):
        current = self.head
        while current:
            print(f"{current.value} -> ", end="")
            current = current.next
            if current is None:
                print("x")
        print(f"HEAD:{self.head.value}, TAIL:{self.tail.value}, SIZE:{self.size}")


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_first(3)
    ll.insert_first(2)
    ll.insert_first(8)
    ll.insert_first(17)
    ll.insert_last(15)
    ll.insert_at_index(value=84, index=3)
    ll.disp()
    print("DS HERO")
