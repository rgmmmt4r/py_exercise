class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.temp = []


    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.temp =  self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.temp
        

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        self.queue1[0]

    def empty(self) -> bool:
        return self.queue1 == []