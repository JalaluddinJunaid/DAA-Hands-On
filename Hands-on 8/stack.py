import random as rand

class Stack:
    def __init__(self, length):
        self.data = [None] * length
        self.length = length
        self.top = -1

    def is_stack_empty(self):
        return self.top == -1

    def is_stack_full(self):
        return self.top == self.length - 1

    def push_element(self, item):
        if self.is_stack_full():
            print("Stack overflow")
            return
        self.top += 1
        self.data[self.top] = item

    def pop_element(self):
        if self.is_stack_empty():
            print("Stack underflow")
            return None
        popped_element = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return popped_element

    def first_element(self):
        if self.is_stack_empty():
            print("Stack underflow")
            return None
        return self.data[0]

    def last_element(self):
        if self.is_stack_empty():
            print("Stack underflow")
            return None
        return self.data[self.top]

    def element_at(self, index):
        if self.is_stack_empty():
            print("Stack underflow")
            return None
        return self.data[index]

    def number_of_elements(self):
        return self.top + 1

    def print_stack_details(self):
        print("\n====== Stack Details: =======")
        print("Stack:", self.data[:self.top + 1])
        print("Empty:", self.is_stack_empty())
        print("Full:", self.is_stack_full())
        print("Number of items:", self.number_of_elements())
        print("First item:", self.first_element())
        print("Last item:", self.last_element())
        print("==============================\n")


if __name__ == '__main__':
    stack = Stack(10)

    stack.print_stack_details()

    print("Pushing 3 random numbers into the stack")
    for _ in range(3):
        stack.push_element(rand.randint(0, 100))
    stack.print_stack_details()

    print("Pushing 7 more random numbers into the stack")
    for _ in range(7):
        stack.push_element(rand.randint(0, 100))
    stack.print_stack_details()
    print("Item at index 5:", stack.element_at(5))

    print("Popping 5 items from the stack")
    for _ in range(5):
        stack.pop_element()
    stack.print_stack_details()
    print("Stack number of items after pop:", stack.number_of_elements())
