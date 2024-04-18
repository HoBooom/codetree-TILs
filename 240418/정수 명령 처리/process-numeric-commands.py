class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def empty(self):
        return not self.items

    def pop(self):
        if self.empty() is True:
            raise Exception("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if self.empth is True:
            raise Exception("Stack is empty")
        return self.items[-1]

stack=Stack()
iter_num=int(input())

for i in range(iter_num):
    comment=input()
    if "push" in comment:
        command, data=comment.split()
        stack.push(int(data))
    elif "size" in comment:
        print(stack.size())
    elif "empty" in comment:
        print(int(stack.empty()))
    elif "pop" in comment:
        print(stack.pop())
    elif "top" in comment:
        print(stack.top())