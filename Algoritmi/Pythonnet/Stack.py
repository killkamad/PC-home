class Stack:
    def __init__(self):
        self.values = []
    def push(self,value):
        self.values.append(value)
    def pop(self):
        if len(self.values) == 0:
            return 'Error'
        last_value = self.values[-1]
        self.values = self.values[:-1]
        return last_value
a = Stack()
b = Stack()

a.push('abc')
a.push('cde')

print(a.pop())
print(a.pop())
print(a.pop())
