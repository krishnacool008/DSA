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


def revers_LinkedList(LinkedList: LinkedList):
    LinkedList.print()

    prev_node = None
    current_node = LinkedList.head
    next_node = current_node.next

    while current_node is not None:
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        if current_node is not None:
            next_node = current_node.next

    LinkedList.head = prev_node

    LinkedList.print()


def reorder(LinkedList: LinkedList):
    LinkedList.print()

    first_node = LinkedList.head
    second_first_node = first_node.next
    second_last_node = None
    last_node = first_node

    while second_last_node is not last_node:
        while last_node.next is not None:
            second_last_node = last_node
            last_node = last_node.next

        first_node.next = last_node
        last_node.next = second_first_node
        second_last_node.next = None
        first_node = second_first_node
        last_node = first_node
        second_first_node = first_node.next

    LinkedList.print()


def reorderList(LinkedList: LinkedList):
    # divide in half
    slow, fast = LinkedList.head, LinkedList.head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second hal
    second_current = second_next = slow.next
    prev_node = slow.next = None

    while second_current:
        second_next = second_current.next
        second_current.next = prev_node
        prev_node = second_current
        second_current = second_next

    # reorder
    first_start = LinkedList.head
    first_start_buff, second_start_buff = None, None
    second_start = prev_node

    while second_start:
        first_start_buff, second_start_buff = first_start.next, second_start.next
        first_start.next = second_start
        second_start.next = first_start_buff
        first_start, second_start = first_start_buff, second_start_buff

    LinkedList.print()


def DelNNodeFromEnd(LinkedList: LinkedList, N: int):
    current_node = LinkedList.head
    length = 1

    while current_node.next is not None:
        length += 1
        current_node = current_node.next

    print(f"Length -> {length}")
    index = length - N
    currentIndex = 1

    if index == 0:
        LinkedList.head = LinkedList.head.next
        LinkedList.print()
        return

    current_node = LinkedList.head
    while current_node.next is not None:
        if currentIndex == index:
            print(f"Deleting node with value {current_node.data}")
            current_node.next = current_node.next.next
            break

        currentIndex += 1
        current_node = current_node.next

    LinkedList.print()


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert_beginning(0)
linked_list.print()
# linked_list.print()  # Output: 1 2 3
# linked_list.delete(2)
# linked_list.print()  # Output: 1 3
# print(linked_list.search(1))  # Output: True
# print(linked_list.search(2))
# DelNNodeFromEnd(linked_list, 2)
