class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
        print(f"{item} is pushed to stack")
    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        return self.stack.pop()
    def peak(self):
        if self.is_empty():
            return "The stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack2 = Stack()
stack2.push(1)
stack2.push(2)
print("Top element of stack1 is : ", stack1.peak())
print("Top element of stack2 is : ", stack2.peak())
print("Size of stack1 is : ", stack1.size())
print("Size of stack2 is : ", stack2.size())
print("Popped element of stack1 is : ", stack1.pop())
print("Stack is empty : ", stack2.is_empty())