

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)


opened = ['(', '{', '[']
closed = [')', '}', ']']


def balance(value):
    stack = Stack()
    for item in value:
        if item in opened:
            stack.push(item)
        elif item in closed:
            num = closed.index(item)
            if not stack.is_empty() and opened[num] == stack.peek():
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


print(balance('{}{}{}[])'))

