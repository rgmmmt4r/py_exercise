from tkinter import N
from typing import Tuple


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.changMIn = False

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.stack)>1):
            if self.min > val:
                self.min = val
                print("min changes to ",self.min)
        else:
            self.min = val
    def pop(self) -> None:
        if self.min == self.top():
            self.changMIn = True
        self.stack.pop()
        if(self.changMIn):
            if(len(self.stack)>0):
                self.min = self.stack[0]
                for element in self.stack:
                    if element < self.min:
                        self.min = element
            self.changMIn = False
        if(len(self.stack)==0):
            self.min = None

    def top(self) -> int:
        if(len(self.stack) >0):
            return self.stack[len(self.stack)-1]
        return None

    def getMin(self) -> int:
        return self.min


obj = MinStack()

obj.push(1)
obj.push(-1)
obj.push(-3)

print(obj.getMin())
obj.pop()
print(obj.stack)

print(obj.getMin())

# obj.pop()
# print(obj.top())
