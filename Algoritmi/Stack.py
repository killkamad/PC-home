class Stack:
    array=[]
    number_of_elements = 0
    array_size = 0
    def __init__(self , size):
            self.number_of_elements = 0
            self.array_size=size
            self.array=[]
    def push(self,a):
            if self.array_size==self.number_of_elements:
                    print ("no memory")
                    return
            self.array.append(a)
            self.number_of_elements+=1
    def pop(self):
            if len(self.array)==0:
                    return "Error"
            last = self.array[-1]
            del self.array[-1]
            self.number_of_elements-=1
            return last

st=Stack(25)
k=input("Введите слово:")
k=list(k)
n=0
for i in k:
        st.push(k[n])
        n+=1
print(st.array)
b = []
while len(st.array)>0:
        a=st.pop()
        b.append(a)
print(b)
x="".join(b)
print(x)
