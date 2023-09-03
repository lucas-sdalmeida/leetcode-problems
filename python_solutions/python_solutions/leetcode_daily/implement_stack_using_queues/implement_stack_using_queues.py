class Queue:
    def __init__(self):
        self.elements = []
        self.__size = 0

    def push(self, element):
        self.elements.append(element)
        self.__size += 1

    def peek(self):
        if self.is_empty():
            return None
        element = self.elements.pop(0)
        self.__size -= 1

        return element

    def is_empty(self):
        return self.__size == 0

    @property
    def size(self):
        return self.__size


class MyStack:
    def __init__(self):
        self.queues = Queue(), Queue()
        self.main_queue_index = 0

    def push(self, x: int) -> None:
        second_queue_index = 1 if self.main_queue_index == 0 else 0
        self.queues[second_queue_index].push(x)
        self.swap_queues()

    def pop(self) -> int:
        return self.queues[self.main_queue_index].peek()

    def top(self) -> int:
        top_element = self.pop()
        self.push(top_element)

        return top_element

    def empty(self) -> bool:
        return self.queues[self.main_queue_index].is_empty()

    def swap_queues(self):
        main_queue = self.queues[self.main_queue_index]
        second_queue_index = 1 if self.main_queue_index == 0 else 0
        second_queue = self.queues[second_queue_index]

        while not main_queue.is_empty():
            second_queue.push(main_queue.peek())

        self.main_queue_index = second_queue_index


if __name__ == '__main__':
    pass
