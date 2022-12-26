class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        if self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            
            
        elif not self.stack1 and  self.stack2:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack2.append(x)
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            
        elif not self.stack1 and not self.stack2:
            self.stack1.append(x)
        else:
            print("push error")
    def pop(self) -> int:
        if self.stack1 and not self.stack2:
            return self.stack1.pop()
        elif not self.stack1 and  self.stack2:
            return self.stack2.pop()
        else:
            print("pop error")

    def peek(self) -> int:
        if self.stack1 and not self.stack2:
            this_peek = self.stack1[-1]
            return this_peek
        elif not self.stack1 and  self.stack2:
            this_peek = self.stack2[-1]
            return this_peek
        else:
            print("peek error")

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


#push","push","push","push","pop","push","pop","pop","pop","pop"

queue = MyQueue()
print(queue.push(1))
print(queue.push(2))
print(queue.push(3))
print(queue.push(4))
print(queue.pop())
print(queue.push(5))
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())




