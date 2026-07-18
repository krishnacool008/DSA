class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_beginning(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}->", end="")
            current_node = current_node.next
        print()

def reverseList(LinkedList: LinkedList):

    # Initialize 2 pointers,
    current = LinkedList.head
    prev = None
    
    # We will initlize 3rd pointer inside loop
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Current is None and passed the list
    # So prev we will use
    LinkedList.head = prev
    LinkedList.print()


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

reverseList(linked_list)