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

    def n_delete_from_end(self, n):
        
        # Dummy we want to use to handle edge cases 
        # like deleting the head node or deleting the only node in the linked list
        dummy = Node(-1)
        dummy.next = self.head
        first = dummy
        second = dummy

        # Move second pointer n+1 steps ahead
        # Because we want first pointer to point to prev node of the node to be deleted
        for _ in range(n + 1):
            second = second.next

        # Now after getting the gap
        # Move both pointer to maintain the gap until second pointer reaches the end
        while second is not None:
            first = first.next
            second = second.next

        # Now Deleting the first.next node
        first.next = first.next.next

        # Head will always be dummy.next because dummy is the prev node of head
        self.head = dummy.next

        self.print()

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

def reOrderList(LinkedList: LinkedList) -> None:

    if LinkedList.head is None or LinkedList.head.next is None:
        LinkedList.print()
        return

    # Find the middle of the linked list
    # Middle will be slow.next box
    fast = LinkedList.head
    slow = LinkedList.head
    while fast.next and slow.next:
        slow = slow.next
        fast = fast.next.next

    # Initialize 2 pointers for reversing the second half
    # And reverse the second half of the linked list
    first_prev = None
    first = slow.next
    slow.next = None # Cut off second half from the first half
    while first:
        first_next = first.next
        first.next = first_prev
        first_prev = first
        first = first_next

    # Again initialize 2 pointers for merging the two halves of the linked list
    first = LinkedList.head
    second = first_prev
    while first and second:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next

    linked_list.print()


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

linked_list.n_delete_from_end(2)

