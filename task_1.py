class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertion_sort(self):

        prev = None
        current = self.head
        while current:
            next = current.next
            sorted_position = None
            sorted_prev = None
            temp = self.head
            while temp and temp.data < current.data:
                sorted_prev = temp
                temp = temp.next
            sorted_position = temp

            if prev:
                prev.next = next
            else:
                self.head = next

            if sorted_position:
                sorted_prev.next = current
            else:
                current.next = self.head
                self.head = current

            prev = current
            current = next

    def merge_normal_and_reversed(self, reversed_list):
    
        merged_list = LinkedList()
        current_normal = self.head
        current_reversed = reversed_list.head

        while current_normal and current_reversed:
            merged_list.insert_at_end(current_normal.data)
            merged_list.insert_at_end(current_reversed.data)
            current_normal = current_normal.next
            current_reversed = current_reversed.next

        merged_list.insert_at_end(current_normal.data) if current_normal else None
        merged_list.insert_at_end(current_reversed.data) if current_reversed else None

        self.head = merged_list.head
        
        print(merged_list)



