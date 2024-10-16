import random as rand

class Node:
    def __init__(self, value):
        self.data = value
        self.next_node = None
    
    def __str__(self):
        return f"{id(self)}: [{self.data} | {id(self.next_node) if self.next_node is not None else None}]"

class SinglyLinkedList:
    def __init__(self, length):
        self.length = length
        self.head_node = None

    def is_empty_list(self):
        return self.head_node is None

    def number_of_nodes(self):
        if self.is_empty_list():
            return 0
        else:
            count = 1
            node = self.head_node
            while node.next_node is not None:
                count += 1
                node = node.next_node
            return count

    def insert_node(self, node):
        if self.number_of_nodes() == self.length:
            print("Linked List is full. Length is: ", self.length)
        else:
            if self.is_empty_list():
                self.head_node = node
            else:
                empty_next = self.head_node
                while empty_next.next_node is not None:
                    empty_next = empty_next.next_node
                empty_next.next_node = node

    def delete_node(self, node):
        if self.is_empty_list():
            print("Underflow")
        else:
            if self.head_node == node:
                self.head_node = node.next_node
            else:
                previous_node = self.head_node
                while previous_node.next_node != node:
                    previous_node = previous_node.next_node
                previous_node.next_node = node.next_node

    def get_head_node(self):
        if self.is_empty_list():
            print("Underflow")
        else:
            return self.head_node

    def get_tail_node(self):
        if self.is_empty_list():
            print("Underflow")
        else:
            last_node = self.head_node
            while last_node.next_node is not None:
                last_node = last_node.next_node
            return last_node

    def get_node_at_index(self, index):
        if self.is_empty_list():
            print("Underflow")
        else:
            node = self.head_node
            for i in range(index):
                if node.next_node is not None:
                    node = node.next_node
                else:
                    print("Index out of bounds")
                    return
            return node

    def print_list_details(self):
        print("\n====== Linked List Details: =======")
        if not self.is_empty_list():
            node = self.head_node
            print(f"Nodes:\n{node}", end=" ->\n")
            while node.next_node is not None:
                node = node.next_node
                print(node, end=" ->\n")
        print("Empty: ", self.is_empty_list())
        print("Number of items: ", self.number_of_nodes())
        print(f"Head Element: ", self.get_head_node())
        print(f"Tail Element: ", self.get_tail_node())
        print("==============================\n")

if __name__ == '__main__':
    linked_list = SinglyLinkedList(10)

    linked_list.print_list_details()

    print("Pushing 3 random numbers into the list")
    for i in range(3):
        node = Node(rand.randint(0, 100))
        linked_list.insert_node(node)
    linked_list.print_list_details()

    print("Pushing 7 more random numbers into the list")
    for i in range(7):
        node = Node(rand.randint(0, 100))
        linked_list.insert_node(node)
    linked_list.print_list_details()
    print("Item at index 5: ", linked_list.get_node_at_index(5))

    print("Remove the tail Element 5 times from the list")
    for i in range(5):
        linked_list.delete_node(linked_list.get_tail_node())
    linked_list.print_list_details()
    print("Linked List's number of items after pop: ", linked_list.number_of_nodes())
