class Queue:
    def __init__(self,size):
        self.size = size+1
        self.values = [0] * self.size
        self.read = 0
        self.write = 0
    def is_empty(self):
        return self.read == self.write
    def enqueue(self,q):
        next_position = self.write +1
        if next_position > self.size -1:
            next_position = 0
        if next_position==self.read:
            print('Error')
            return
        self.values[self.write] =q
        self.write +=1
        if self.write > self.size-1:
            self.write =0
    def dequeue(self):
        if self.read ==self.write:
            return 'Error'
        q = self.values[self.read]
        self.values[self.read] = 0
        self.read +=1
        if self.read > self.size -1:
            self.read = 0
        return q

q1 = Queue(4)
q1.enqueue(5)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1.values)
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.values)
print(q1.is_empty())

