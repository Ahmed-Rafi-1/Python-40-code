class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} is pushed to Queue")
    def dequeue(self):
        if self.is_empty():
            return "The Queue is empty"
        return self.queue.pop(0)
    def peak(self):
        if self.is_empty():
            return "The Queue is empty"
        return self.queue[0]
    def size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element is : ", queue.peak())
print("Queue size is : ", queue.size())
print("Dequeued element is : ", queue.dequeue())
print("Queue is empty : ", queue.is_empty())