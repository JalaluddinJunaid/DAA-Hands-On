import random as rand

class Queue:
    def __init__(self, length):
        self.data = [None] * length
        self.head_index = 0
        self.tail_index = 0
        self.length = length

    def is_queue_empty(self):
        return self.head_index == self.tail_index

    def is_queue_full(self):
        return self.head_index == (self.tail_index + 1) % self.length

    def enqueue_element(self, element):
        if self.is_queue_full():
            print("Queue overflow")
            return
        self.data[self.tail_index] = element
        self.tail_index = (self.tail_index + 1) % self.length

    def dequeue_element(self):
        if self.is_queue_empty():
            print("Queue underflow")
            return None
        dequeued_element = self.data[self.head_index]
        self.head_index = (self.head_index + 1) % self.length
        return dequeued_element

    def get_head_element(self):
        if self.is_queue_empty():
            print("Queue is empty")
            return None
        return self.data[self.head_index]

    def get_tail_element(self):
        if self.is_queue_empty():
            print("Queue is empty")
            return None
        return self.data[(self.tail_index - 1 + self.length) % self.length]

    def get_element_at_index_behind_head(self, index):
        if self.is_queue_empty():
            print("Queue is empty")
            return None
        if index >= (self.tail_index - self.head_index):
            print("Index out of bounds")
            return None
        return self.data[(self.head_index + index) % self.length]

    def get_number_of_elements(self):
        return (self.tail_index - self.head_index + self.length) % self.length

    def print_queue_details(self):
        print("\n====== Queue Details: =======")
        print("Queue:", self.data[self.head_index:self.tail_index])
        print("Empty:", self.is_queue_empty())
        print("Full:", self.is_queue_full())
        print("Number of items:", self.get_number_of_elements())
        print("Head index:", self.head_index, ", Head element:", self.get_head_element())
        print("Tail index:", self.tail_index, ", Tail element:", self.get_tail_element())
        print("==============================\n")


if __name__ == '__main__':
    queue = Queue(10)

    queue.print_queue_details()

    print("Enqueuing 3 random numbers into the queue")
    for _ in range(3):
        queue.enqueue_element(rand.randint(0, 100))
    queue.print_queue_details()

    print("Enqueuing 7 more random numbers into the queue")
    for _ in range(7):
        queue.enqueue_element(rand.randint(0, 100))
    queue.print_queue_details()
    print("Item at index 5:", queue.get_element_at_index_behind_head(5))

    print("Dequeuing 5 items from the queue")
    for _ in range(5):
        queue.dequeue_element()
    queue.print_queue_details()
    print("Queue number of items after dequeue:", queue.get_number_of_elements())
